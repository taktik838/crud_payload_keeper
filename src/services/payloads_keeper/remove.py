from integrations.mongodb.models import PayloadKeeper


async def remove_payload(key: str) -> None:
    await PayloadKeeper.q().delete_one({
        PayloadKeeper.key.s: key,
    })

async def remove_payload_service(key: str) -> None:
    await remove_payload(key)
