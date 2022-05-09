import inspect
import json
import logging
from typing import Any, Optional, OrderedDict, Union
from aiomongodel import Document
from aiomongodel.queryset import MotorQuerySet
from aiomongodel.errors import AioMongodelException
from pymongo.errors import PyMongoError
import inspect

from aiomongodel import Document
from aiomongodel.errors import AioMongodelException
from aiomongodel.queryset import MotorQuerySet
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import PyMongoError

import settings


MONGO_DB = "db1"

mongo_logger = logging.getLogger("mongo_logger")
mongo_logger.setLevel(logging.DEBUG)

class MongoClient:
    _client: AsyncIOMotorClient = None

    @classmethod
    def _init_client(cls) -> None:
        if not cls._client:
            cls._client = AsyncIOMotorClient(
                settings.MONGO_CONNECTION_STRING,
            )

    @classmethod
    async def close_client(cls) -> None:
        if cls._client:
            cls._client.close()

    @classmethod
    def get_db(cls) -> AsyncIOMotorDatabase:
        if not cls._client:
            cls._init_client()
        return cls._client[MONGO_DB]

def document_json_decoder(value: Any) -> Union[OrderedDict, str]:
    if isinstance(value, Document):
        return value.to_data()
    return str(value)


class LoggingMotorQuerySet(MotorQuerySet):
    def _log(
        self,
        query: Optional[dict] = None,
        update_payload: Optional[dict] = None,
        options: Optional[dict] = None,
        response: Any = None,
    ) -> None:
        mongo_logger.info(msg=json.dumps(
            {
                "request": {
                    "method": inspect.stack()[1].function,
                    "query": query,
                    "update_payload": update_payload,
                    "options": options,
                },
                "response": response
            },
            default=document_json_decoder,
            skipkeys=True,
            ensure_ascii=False,
            allow_nan=True,
            sort_keys=True,
            indent=4,
        ))

    @staticmethod
    def _response_from_exception(ex: Exception) -> dict:
        return {
            "error": {
                "message": str(ex),
                "code": type(ex).__name__,
            }
        }

    def find(self, query: dict = {}):
        try:
            response = super().find(query)
        except (PyMongoError, AioMongodelException) as ex:
            response = self._response_from_exception(ex)
        self._log(
            query=query,
            response=None,
        )
        return response


    async def find_one(self, query: dict):
        try:
            response = await super().find_one(query)
        except (PyMongoError, AioMongodelException) as ex:
            response = self._response_from_exception(ex)
        self._log(
            query=query,
            response=response,
        )
        return response

    async def update_one(self, query: dict, update_payload: dict, upsert: bool = False):
        try:
            response = await super().update_one(query, update_payload, upsert=upsert)
        except (PyMongoError, AioMongodelException) as ex:
            response = self._response_from_exception(ex)
        self._log(
            query=query,
            response=response,
            update_payload=update_payload,
            options={"upsert": upsert}
        )

    async def delete_one(self, query: dict):
        try:
            response = await super().delete_one(query)
        except (PyMongoError, AioMongodelException) as ex:
            response = self._response_from_exception(ex)
        self._log(
            query=query,
            response=response,
        )
