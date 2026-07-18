import pymongo
from datetime import datetime, timezone
from bson.objectid import ObjectId
from ..db.database import db

collection = db["properties"]


def read_properties():
    return collection.find().sort("name", pymongo.ASCENDING)


def read_property(property_id: str):
    property_filter = {"_id": ObjectId(property_id)}
    db_property = collection.find_one(property_filter)
    if db_property is None:
        return None
    db_property["_id"] = str(db_property["_id"])
    formatted_property = format_ui_date(db_property)
    return formatted_property


def save_property(new_property):
    formatted_property = format_db_fields(new_property)
    return collection.insert_one(formatted_property)


def update_property(property_id: str, updated_property):
    property_filter = {"_id": ObjectId(property_id)}
    formatted_property = format_db_fields(updated_property)
    update = {"$set": formatted_property}
    return collection.find_one_and_update(property_filter, update)


def delete_property(property_id: str):
    property_filter = {"_id": ObjectId(property_id)}
    return collection.find_one_and_delete(property_filter)


def format_ui_date(raw_property):
    if raw_property.get("acquiredDate", None) is not None:
        raw_property["acquiredDate"] = raw_property["acquiredDate"].date()
    return raw_property


def format_db_fields(raw_property):
    raw_property = format_db_date(raw_property)
    clean_property = {k: v for k, v in raw_property.items() if v is not None}
    return clean_property


def format_db_date(raw_property):
    if raw_property["acquiredDate"] is not None:
        raw_property["acquiredDate"] = datetime(
            raw_property["acquiredDate"].year,
            raw_property["acquiredDate"].month,
            raw_property["acquiredDate"].day,
            tzinfo=timezone.utc
        )
    return raw_property
