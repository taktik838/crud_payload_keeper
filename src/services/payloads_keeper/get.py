from integrations.mongodb.models import PayloadKeeper


async def get_payload(key: str) -> dict:
    result = await PayloadKeeper().q().find_one({
        PayloadKeeper.key.s: key
    })

    if isinstance(result, PayloadKeeper):
        return {
        "payload": result.payload,
        "duplicates": result.count - 1,
    }
    else:  # error
        return result


async def get_payload_service(key: str) -> dict:
    return await get_payload(key)

