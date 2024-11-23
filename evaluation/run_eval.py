import asyncio
import os
from typing import List
import yaml
import requests
import json

from openhands.controller.state.state import State
from openhands.core.config import (
    AppConfig,
    SandboxConfig,
    LLMConfig,
    get_llm_config_arg,
    get_parser,
)
from openhands.core.logger import openhands_logger as logger
from openhands.core.main import create_runtime, run_controller
from openhands.events.action import CmdRunAction, MessageAction
from openhands.events.observation import CmdOutputObservation
from openhands.runtime.base import Runtime
from openhands.utils.async_utils import call_async_from_sync

from browsing import pre_login


def get_config(
    base_container_image: str,
    outputs_path: str,
    llm_config: LLMConfig
) -> AppConfig:
    config = AppConfig(
        run_as_openhands=False,
        max_budget_per_task=4,
        max_iterations=100,
        trajectories_path=os.path.join(outputs_path, f'traj_{base_container_image}.json'),
        sandbox=SandboxConfig(
            base_container_image=base_container_image,
            enable_auto_lint=True,
            use_host_network=False,
            # large enough timeout, since some testcases take very long to run
            timeout=300,
            api_key=os.environ.get('ALLHANDS_API_KEY', None),
        ),
        # we mount trajectories path so that trajectories, generated by OpenHands
        # controller, can be accessible to the evaluator file in the runtime container
        workspace_mount_path=outputs_path,
        workspace_mount_path_in_sandbox='/outputs',
    )
    config.set_llm_config(llm_config)
    return config


def load_dependencies(runtime: Runtime) -> List[str]:
    """
    Every task has a dependencies.yml file, which lists all the services that the
    task depends on. This function loads the file and returns all dependent service names.
    """
    command = (
        "cat /utils/dependencies.yml"
    )
    action = CmdRunAction(command=command)
    logger.info(action, extra={'msg_type': 'ACTION'})
    obs: CmdOutputObservation = runtime.run_action(action)
    logger.info(obs, extra={'msg_type': 'OBSERVATION'})
    assert obs.exit_code == 0
    dependencies = yaml.safe_load(obs.content)
    if dependencies is None:
        dependencies = []
    return dependencies


def init_task_env(runtime: Runtime, hostname: str, llm_config: LLMConfig):
    command = (
        f"SERVER_HOSTNAME={hostname} "
        f"LITELLM_API_KEY={llm_config.api_key} "
        f"LITELLM_BASE_URL={llm_config.base_url} "
        f"LITELLM_MODEL={llm_config.model} "
        # TODO: remove this once ready for release
        "RESET_ENV=true "
        "bash /utils/init.sh"
    )
    action = CmdRunAction(command=command)
    action.timeout = 900
    logger.info(action, extra={'msg_type': 'ACTION'})
    obs = runtime.run_action(action)
    logger.info(obs, extra={'msg_type': 'OBSERVATION'})
    assert obs.exit_code == 0


def codeact_user_response(state: State) -> str:
    msg = (
        'Please continue working on the task on whatever approach you think is suitable.\n'
        'If you think you have solved the task, please finish the interaction.\n'
        'IMPORTANT: YOU SHOULD NEVER ASK FOR HUMAN HELP.\n'
    )

    if state.history:
        # check if the agent has tried to talk to the user 3 times, if so, let the agent know it can give up
        user_msgs = [
            event
            for event in state.history
            if isinstance(event, MessageAction) and event.source == 'user'
        ]
        if len(user_msgs) >= 2:
            # let the agent know that it can give up when it has tried 3 times
            return (
                msg
                + 'If you want to give up, run: <execute_bash> exit </execute_bash>.\n'
            )
    return msg


def run_solver(runtime: Runtime, task_name: str, config: AppConfig, dependencies: List[str]) -> State:
    instruction = "Complete the task in /instruction/task.md"

    if 'gitlab' in dependencies:
        instruction += "\n\nGitlab username is 'root' and password is 'theagentcompany'"

    # TODO: OpenHands should optionally, save browser screenshots to a place
    state: State | None = asyncio.run(
        run_controller(
            config=config,
            sid=task_name,
            initial_user_action=MessageAction(content=instruction),
            runtime=runtime,
            fake_user_response_fn=codeact_user_response,
        )
    )
    logger.info(state)
    return state


def run_evaluator(runtime: Runtime, llm_config: LLMConfig, trajectory_path: str, result_path: str):
    command = (
        f"LITELLM_API_KEY={llm_config.api_key} "
        f"LITELLM_BASE_URL={llm_config.base_url} "
        f"LITELLM_MODEL={llm_config.model} "
        f"python_default /utils/eval.py --trajectory_path {trajectory_path} --result_path {result_path}"
    )
    action = CmdRunAction(command=command)
    action.timeout = 600
    logger.info(action, extra={'msg_type': 'ACTION'})
    obs = runtime.run_action(action)
    logger.info(obs, extra={'msg_type': 'OBSERVATION'})
    assert obs.exit_code == 0


if __name__ == '__main__':
    parser = get_parser()
    parser.add_argument(
        '--task-image-name',
        type=str,
        default='example-image',
        help='Task image name',
    )
    parser.add_argument(
        '--outputs-path',
        type=str,
        default='./outputs',
        help='Folder path to save trajectories and evaluation results'
    )
    parser.add_argument(
        '--server-hostname',
        type=str,
        default='ogma.lti.cs.cmu.edu',
        help='Server hostname, e.g. ogma.lti.cs.cmu.edu'
    )
    args, _ = parser.parse_known_args()

    llm_config: LLMConfig | None = None
    if args.llm_config:
        llm_config = get_llm_config_arg(args.llm_config)

    if llm_config is None:
        raise ValueError(f'Could not find LLM config: --llm_config {args.llm_config}')

    if llm_config.api_key is None:
        raise ValueError(f'LLM API key is not set')

    logger.info(f"Task image name is {args.task_image_name}")
    config: AppConfig = get_config(args.task_image_name, os.path.abspath(args.outputs_path), llm_config)
    runtime: Runtime = create_runtime(config)
    call_async_from_sync(runtime.connect)

    init_task_env(runtime, args.server_hostname, llm_config)

    dependencies = load_dependencies(runtime)
    logger.info(f"Service dependencies: {dependencies}")

    try:
        pre_login(runtime, dependencies)
    except Exception as e:
        logger.error(f"Failed to pre-login: {e}")

        # before giving up, let's try to init and login again
        init_task_env(runtime, args.server_hostname, llm_config)
        pre_login(runtime, dependencies)

    state = run_solver(runtime, args.task_image_name, config, dependencies)

    # this path is the absolute path in the runtime container
    trajectory_path = f'/outputs/traj_{args.task_image_name}.json'
    result_path = f'/outputs/eval_{args.task_image_name}.json'

    run_evaluator(runtime, llm_config, trajectory_path, result_path)
