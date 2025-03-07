# Evaluation Instructions

## Running Evaluation on All Tasks (Except Specified Ones)

To run the evaluation on all tasks except for:
- `riscv-general`
- `neural-network-general`
- `d-flip-flop-openlane`
- `multiplier-4bit-unsigned-pipelined-openlane`

Navigate to the evaluation directory:

```bash
cd TheAgentCompany/evaluation
```

Run the following command:

```bash
export LLM_CACHING_PROMPT=true \
       SANDBOX_LLM_CACHING_PROMPT=true \
       SANDBOX_ENV_PINECONE_API_KEY="******" \
       DEBUG=false \
       SANDBOX_ENV_OPENAI_API_KEY="******" && \
bash run_eval.sh \
  --agent-llm-config group2 \
  --env-llm-config group1 \
  --outputs-path outputs \
  --server-hostname localhost \
  --version 1.0.0
```

### Model Group Definitions
- **group2** → Claude
- **group1** → GPT-4o

To define groups, create a `config.toml` file inside the `evaluation` directory:

```toml
[llm.group1]
model="gpt-4o"
base_url="https://api.openai.com/v1"
api_key="******"

[llm.group2]
model="anthropic/claude-3-5-sonnet-20241022"
api_key="*****"
```

## Running All Tasks (Including OpenLane, RISC-V, and NN)
To include all tasks in the evaluation, remove the exception conditions from `TheAgentCompany/evaluation/run_eval.sh`:

```bash
if [[ "$task_name" == "riscv-general" ||
      "$task_name" == "multiplier-4bit-unsigned-pipelined-openlane" ||
      "$task_name" == "neural-network-general" ||
      "$task_name" == "d-flip-flop-openlane" ]]; then
    continue
fi
```

## Running a Specific Task
To evaluate a single specific task, modify `run_eval.sh`:

1. Replace this line:
   ```bash
   task_name=$(basename "$task_dir")
   ```
   with:
   ```bash
   task_name="ipm-caravel"  # Example task
   ```
2. Add `break` at the end of the loop to stop execution after this task.

## Running a Specific Group of Tasks
To evaluate a specific set of tasks, modify `run_eval.sh`:

1. Replace this line:
   ```bash
   for task_dir in "$TASKS_DIR"/*/; do
   ```
   with:
   ```bash
   for task_name in "name1" "name2"; do
   ```
2. Comment out this line:
   ```bash
   task_name=$(basename "$task_dir")
   ```

---
Follow these instructions to configure and run evaluations as needed.

