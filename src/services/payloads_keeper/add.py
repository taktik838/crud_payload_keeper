from services.payloads_keeper.common import add_or_update


async def add_payload(payload: dict):
    return await add_or_update(payload)


async def add_payload_service(payload: dict) -> dict:
    key = await add_payload(payload)
    return {
        "key": key
    }
