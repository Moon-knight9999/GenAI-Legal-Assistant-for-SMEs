import json
import datetime
import os

LOG_PATH = "data/audit_logs/log.json"

def log_action(action, metadata=None):
    os.makedirs("data/audit_logs", exist_ok=True)

    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "action": action,
        "metadata": metadata or {}
    }

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
