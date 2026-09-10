import json
import os
from datetime import UTC, datetime


def log_step(step: int, tool: str, args: dict | str, result: str) -> None:
    """
    Registra la ejecución de un paso del agente en logs/agent_run.jsonl (append mode).
    Cada entrada incluye: ts, step, tool, args, result_summary.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "agent_run.jsonl")

    result_str = str(result)
    result_summary = result_str[:200]

    entry = {
        "ts": datetime.now(UTC).isoformat(),
        "step": step,
        "tool": tool,
        "args": args,
        "result_summary": result_summary
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
