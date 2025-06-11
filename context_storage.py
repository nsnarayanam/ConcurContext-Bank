# Context Storage Example
import json
import os

def store_context(user_id, context_blob):
    file_path = f"./vault/{user_id}_context.json"
    os.makedirs("./vault", exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(context_blob, f)
    return file_path
