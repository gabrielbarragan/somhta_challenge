from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson.objectid import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)


class OrdersModel(BaseModel):

    id: Optional[str] = Field(default_factory=PyObjectId, alias="_id")
    account_id: Optional[int]    
    transaction_count: Optional[int] 
    bucket_start_date: Optional[datetime]
    bucket_end_date: Optional[datetime] 

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str(ObjectId)}
        schema_extra = {
            "example": {
                "id":"5ca4bbc1a2dd94ee58161cb1",
                "account_id":443178,
                "transaction_count":66,
                "bucket_start_date":"2002-08-18T04:56:07.000+00:00",
                "bucket_end_date": "2017-01-03T00:00:00.000+00:00",
            }
        }

def orderEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "account_id": item["account_id"],
        "transaction_count": item["transaction_count"],
        "bucket_start_date": item["bucket_start_date"],
        "bucket_end_date": item["bucket_end_date"],
        
    }

def ordersEntity(entity) -> list:
    return [orderEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


        


