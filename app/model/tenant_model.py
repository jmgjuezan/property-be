import calendar
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from typing import Any
from ..db.database import db
from ..util.format_helper import format_db_fields, format_ui_field, format_ui_fields

table = "tenants"
collection = db[table]
fields = ["moveInDate", "moveOutDate", "paymentDate"]


def find_all(
    property: str | None = None,
    move_in_year_month: str | None = None,
    move_out_year_month: str | None = None,
    move_out: bool | None = None
):
    where: dict[str, Any] = {"$and": [
        {"$or": [
            {"deleted": {"$exists": False}},
            {"deleted": False}
        ]}
    ]}

    if move_out is not None:
        where["$and"].append({"moveOutDate": {"$exists": move_out}})
    elif move_out_year_month is not None:
        year_month = move_out_year_month.split("-")  # Expected YYYY-MM
        year = int(year_month[0])
        month = int(year_month[1])
        move_out_date = datetime(year, month, 1, 0, 0, 0)
        where["$and"].append({"$or": [
            {"moveOutDate": {"$exists": False}},
            {"moveOutDate": {"$gte": move_out_date}}
        ]})
    if property is not None:
        where["$and"].append({"property": property})
    if move_in_year_month is not None:
        year_month = move_in_year_month.split("-")  # Expected YYYY-MM
        year = int(year_month[0])
        month = int(year_month[1])
        _, last_day = calendar.monthrange(year, month)
        move_in_date = datetime(year, month, 1, 0, 0, 0)
        move_in_date = move_in_date.replace(day=last_day)
        where["$and"].append({"moveInDate": {"$lte": move_in_date}})

    tenants = collection.find(where).sort("firstName", pymongo.ASCENDING)
    tenants = format_ui_fields(tenants, fields)
    return tenants


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
    result = format_db_name(new_model)
    result = format_db_fields(result, fields)
    return collection.insert_one(result)


def update(model_id: str, updated_model):
    query_filter = {"_id": ObjectId(model_id)}
    result = format_db_name(updated_model)
    result = format_db_fields(result, fields)
    model = {"$set": result}
    return collection.find_one_and_update(query_filter, model)


def delete(model_id: str):
    query_filter = {"_id": ObjectId(model_id)}
    model = {"$set": {"deleted": True}}
    return collection.find_one_and_update(query_filter, model)


def format_db_name(tenant):
    tenant["firstName"] = tenant["firstName"].title()
    if tenant["middleName"] is not None:
        tenant["middleName"] = tenant["middleName"].title()
    tenant["lastName"] = tenant["lastName"].title()
    if tenant["nickname"] is not None:
        tenant["nickname"] = tenant["nickname"].title()
    return tenant
