import asyncio
from integrations.mongodb.models import PayloadKeeper
from services.payloads_keeper.common import add_or_update


async def decrease_count_duplicates(key: str):
    await PayloadKeeper().q().update_one(
        {
        PayloadKeeper.key.s: key,
    },
        {
            "$set": {
                PayloadKeeper.count.s: 1,
            }
        }
    )


async def update_payload_service(old_key: str, new_payload: dict) -> dict:
    _, new_key = await asyncio.gather(
        decrease_count_duplicates(old_key),
        add_or_update(new_payload),
    )

    return {"key": new_key}
