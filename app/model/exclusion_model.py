from bson.objectid import ObjectId
from datetime import date, datetime
from typing import Any
from ..db.database import db
from ..util.format_helper import format_db_fields, format_ui_field, format_ui_fields

table = "exclusions"
collection = db[table]
fields = ["exclusionDate", "exclusionDateFrom", "exclusionDateTo"]


def find_all(
        name: str | None = None,
        property: str | None = None,
        from_date: date | None = None,
        to_date: date | None = None
):
    where: dict[str, Any] = {"$and": [
        {"$or": [
            {"deleted": {"$exists": False}},
            {"deleted": False}
        ]}
    ]}

    if property is not None:
        where["$and"].append({"property": property})
    if name is not None:
        where["$and"].append({"name": name})
    if from_date is not None and to_date is not None:
        from_datetime = datetime(
            from_date.year,
            from_date.month,
            from_date.day,
            0, 0, 0
        )
        to_datetime = datetime(
            to_date.year,
            to_date.month,
            to_date.day,
            0, 0, 0)
        where["$and"].append({"$or": [
            {"exclusionDateFrom": {"$gte": from_datetime}},
            {"exclusionDateFrom": {"$lte": to_datetime}},
            {"exclusionDate": from_datetime},
            {"exclusionDate": to_datetime}
        ]})

    results = collection.find(where)
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
    result = collection.find_one(query_filter)
    if result is not None:
        result = format_ui_field(result, fields)
    return result


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
