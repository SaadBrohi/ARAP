# utils/history.py

import json
import os

HISTORY_PATH = "data/chat_history.json"

def save_to_history(question, answer):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append({"question": question, "answer": answer})
    with open(HISTORY_PATH, "w") as f:
        json.dump(history[-10:], f)  # Keep only last 10

def load_history():
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "r") as f:
            return json.load(f)
    return []
