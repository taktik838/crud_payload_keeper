from functools import wraps

from aiomongodel import Document
from aiomongodel import fields
from motor.motor_asyncio import AsyncIOMotorClientSession
from motor.motor_asyncio import AsyncIOMotorDatabase
import pymongo

from .client import LoggingMotorQuerySet
from .client import MongoClient


class BaseDocument(Document):
    @classmethod
    @wraps(Document.q)
    def q(cls, db: AsyncIOMotorDatabase = None, session: AsyncIOMotorClientSession = None) -> LoggingMotorQuerySet:
        db = db or MongoClient.get_db()
        return LoggingMotorQuerySet(cls, db=db, session=session)


class PayloadKeeper(BaseDocument):
    _id = fields.StrField(required=True)

    key = fields.SynonymField(_id)
    payload = fields.AnyField(required=True)
    count = fields.IntField()

    class Meta:
        collection = "payload_keeper"
        indexes = [
            pymongo.IndexModel((("_id", pymongo.HASHED),)),
        ]
