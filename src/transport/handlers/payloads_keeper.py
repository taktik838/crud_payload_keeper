import json
from tornado.web import RequestHandler
from services.payloads_keeper.add import add_payload_service

from services.payloads_keeper.get import get_payload_service
from services.payloads_keeper.remove import remove_payload_service
from services.payloads_keeper.statistic import statistic_service
from services.payloads_keeper.update import update_payload_service


class PayloadsKeeper(RequestHandler):
    async def get(self):
        key = self.get_query_argument("key")
        response = await get_payload_service(key)
        self.write(response)

    async def post(self):
        response = await add_payload_service(json.loads(self.request.body))
        self.write(response)

    async def delete(self):
        await remove_payload_service(json.loads(self.request.body)["key"])
        self.write({})

    async def put(self):
        body = json.loads(self.request.body)
        response = await update_payload_service(
            old_key=body["key"],
            new_payload=body["newPayload"],
        )
        self.write(response)


class PayloadsKeeperStatistic(RequestHandler):
    async def get(self):
        response = await statistic_service()
        self.write(response)
