import pymongo
from bson.objectid import ObjectId
from typing import Any
from ..db.database import db
from ..util.format_helper import format_db_fields, format_ui_field, format_ui_fields

table = "payments"
collection = db[table]
fields = ["paymentDate"]


def find_all(
        paid_by: str | None = None,
        property: str | None = None
):
    where: dict[str, Any] = {"$or": [
        {"deleted": {"$exists": False}},
        {"deleted": False}
    ]}

    if paid_by is not None:
        where["tenant"] = paid_by
    if property is not None:
        where["property"] = property

    results = collection.find(where).sort("paymentDate", pymongo.ASCENDING)
    results = format_ui_fields(results, fields)
    return results


def find_one(model_id: str):
    query_filter = {
        "_id": ObjectId(model_id),
        "$or": [
            {"deleted": {"$exists": False}},
            {"deleted": False}
        ]
    }
    results = collection.find_one(query_filter)
    if results is not None:
        results = format_ui_field(results, fields)
    return results


def save(new_model):
    result = format_db_fields(new_model, fields)
    return collection.insert_one(result)


def update(model_id: str, updated_model):
    query_filter = {"_id": ObjectId(model_id)}
    result = format_db_fields(updated_model, fields)
    model = {"$set": result}
    return collection.find_one_and_update(query_filter, model)


def delete(model_id: str):
    query_filter = {"_id": ObjectId(model_id)}
    model = {"$set": {"deleted": True}}
    return collection.find_one_and_update(query_filter, model)
