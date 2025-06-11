# Token Issuance Logic
def issue_ctk(user_id, context_data):
    # Hash context for uniqueness
    import hashlib, json
    context_hash = hashlib.sha256(json.dumps(context_data).encode()).hexdigest()

    # Dummy CTK record
    ctk = {
        "user_id": user_id,
        "context_hash": context_hash,
        "issued_at": "2025-06-11",
        "ctk_id": f"CTK-{context_hash[:8]}"
    }
    return ctk
