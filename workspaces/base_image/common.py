import os
import logging

import litellm
from rocketchat_API.rocketchat import RocketChat

from config import *

logging.basicConfig(level=logging.INFO)

# messages: a list of message.
# example [{ "content": "Hello, how are you?","role": "user"}]
def llm_evaluate(messages):
    if TEST_MODE:
        return {'choices': [{'message': {"content": "Hello, how are you?","role": "user"}}]}

    return litellm.completion(
        api_key=LITELLM_API_KEY,
        base_url=LITELLM_BASE_URL,
        model=LITELLM_MODEL,
        messages=messages
    ).json()


class MockRocketChatClient:

    class JsonResponse:
        def json(self):
            return {'users': [], 'messages': []}

    def __getattr__(self, name):
        def method(*args, **kwargs):
            return self.JsonResponse()
        return method


def create_rocketchat_client(username='theagentcompany', password='theagentcompany'):
    SERVER_HOSTNAME = os.getenv('SERVER_HOSTNAME') or 'the-agent-company.com'
    ROCKETCHAT_PORT = os.getenv('ROCKETCHAT_PORT') or '3000'
    
    # Construct RocketChat URL
    ROCKETCHAT_URL = f"http://{SERVER_HOSTNAME}:{ROCKETCHAT_PORT}"
    
    try:
        return RocketChat(username, password, server_url=ROCKETCHAT_URL)
    except:
        logging.warning("Fail to connect to rocketchat")
        if TEST_MODE:
            logging.info("TEST_MODE, use mock rocketchat client")
            return MockRocketChatClient()
        else:
            raise


def get_chat_history(rocket_client, username: str):
    """
    Get chat history from RocketChat server, between:
    1) param username,
    2) and the account used to create rocket client instance

    Returns the messages as a list. If no history, returns an empty list.
    """
    id = None
    for item in rocket_client.users_list().json()['users']:
        if item['nameInsensitive'] == username.lower():
            id = item["_id"]
            break

    if id is None:
        logging.error(f'Cannot fetch chat history for {username}')
        return []

    msgs = rocket_client.im_history(room_id=id).json()['messages']
    reversed_history = [] if msgs is None else [msg['msg'] for msg in msgs]
    history = reversed_history[::-1]
    logging.info(f'Chat history with {username} is: {history}')
    return history


def evaluate_chat_history_with_llm(rocket_client, username: str, predicate: str):
    """
    Evaluates chat history from RocketChat server against a given predicate using LLM.

    Args:
        rocket_client: RocketChat client instance
        username: The username whose chat history to evaluate
        predicate: The condition to evaluate against (e.g., "Liu Qiang had average job performance")

    Returns:
        bool: True if the chat history matches the predicate, False otherwise

    Example:
        >>> result = evaluate_chat_history_with_llm(
        ...     rocket_client,
        ...     "Liu Qiang",
        ...     "the person receiving the feedback had an average job performance"
        ... )
    """
    try:
        # Retrieve chat history
        messages = get_chat_history(rocket_client, username)
        if not messages:
            logging.warning(f"No chat history found for user: {username}")
            return False

        # Construct LLM query
        llm_messages = [{
            "role": "user",
            "content": f'Does the chat history """{messages}""" indicate {predicate}? '
                      'Please answer "yes" if it does, or "no" if it does not.'
        }]

        logging.debug(f'LLM request is: {llm_messages}')

        # Call LLM for evaluation
        llm_response = llm_evaluate(llm_messages)
        logging.info(f"LLM evaluation completed, response is: {llm_response}")

        # Extract and process response
        content = llm_response["choices"][0]["message"]["content"].lower().strip()

        # Evaluate result
        result = "yes" in content
        if result:
            logging.info(f'Predicate "{predicate}" evaluated to "{result}"')
        else:
            logging.warning(f'Predicate "{predicate}" evaluated to "{result}"')

        return result

    except KeyError as e:
        logging.error("Invalid LLM response structure", exc_info=True)
        return False

    except Exception as e:
        logging.error(f"Failed to evaluate chat history for user {username}: {str(e)}", exc_info=True)
        return False
