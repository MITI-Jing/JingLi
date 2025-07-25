import json
import os

MEMORY_FILE = "user_memory.json"

def load_memory(user_id: str) -> dict:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            all_memory = json.load(f)
        return all_memory.get(user_id, {})
    return {}

def save_memory(user_id: str, memory: dict):
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            all_memory = json.load(f)
    else:
        all_memory = {}

    all_memory[user_id] = memory
    with open(MEMORY_FILE, "w") as f:
        json.dump(all_memory, f, indent=2)
