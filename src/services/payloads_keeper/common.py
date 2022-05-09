import base64
import hashlib
import json
from typing import Optional

from integrations.mongodb.models import PayloadKeeper


def key_from_payload(payload: dict) -> str:
    str_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    b64_payload = base64.b64encode(str_payload.encode())
    hash_payload = hashlib.md5(b64_payload)
    return hash_payload.hexdigest()


async def add_or_update(payload: dict, key: Optional[str] = None) -> str:
    if not key:
        key = key_from_payload(payload)

    await PayloadKeeper.q().update_one(
        {
            PayloadKeeper.key.s: key,
        },
        {
            "$set": {
                PayloadKeeper.key.s: key,
                PayloadKeeper.payload.s: payload,
            },
            "$inc": {
                PayloadKeeper.count.s: 1,
            },
        },
        upsert=True,
    )
    return key
