from datetime import datetime, timezone
from bson.objectid import ObjectId
from ..db.database import db

collection = db["properties"]


def read_properties():
    return collection.find()


def read_property(property_id: str):
    property_filter = {"_id": ObjectId(property_id)}
    return collection.find_one(property_filter)


def save_property(new_property):
    formatted_property = format_fields(new_property)
    return collection.insert_one(formatted_property)


def update_property(property_id: str, updated_property):
    property_filter = {"_id": ObjectId(property_id)}
    formatted_property = format_fields(updated_property)
    update = {"$set": formatted_property}
    return collection.find_one_and_update(property_filter, update)


def delete_property(property_id: str):
    property_filter = {"_id": ObjectId(property_id)}
    return collection.find_one_and_delete(property_filter)


def format_fields(raw_property):
    raw_property = format_dates(raw_property)
    clean_property = {k: v for k, v in raw_property.items() if v is not None}
    return clean_property


def format_dates(raw_property):
    if raw_property["acquiredDate"] is not None:
        raw_property["acquiredDate"] = datetime(
            raw_property["acquiredDate"].year,
            raw_property["acquiredDate"].month,
            raw_property["acquiredDate"].day,
            tzinfo=timezone.utc
        )
    return raw_property
