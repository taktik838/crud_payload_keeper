from integrations.mongodb.models import PayloadKeeper


async def get_persent_of_duplicates() -> float:
    all_count = duplicate_count = 0
    document: PayloadKeeper
    async for document in PayloadKeeper().q().find():
        all_count += document.count
        duplicate_count += document.count - 1
    return duplicate_count / all_count * 100



async def statistic_service() -> dict:
    persent_of_duplicates = await get_persent_of_duplicates()
    return {
        "persent_of_duplicates": f"{round(persent_of_duplicates, 2)}%"
    }
