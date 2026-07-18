from bson.objectid import ObjectId
from ..db.database import db

collection = db["properties"]


def read_properties():
    return collection.find()


def read_property(property_id: str):
    property_filter = {"_id": ObjectId(property_id)}
    return collection.find_one(property_filter)


def save_property(new_property):
    return collection.insert_one(new_property)


def update_property(property_id: str, updated_property):
    property_filter = {"_id": ObjectId(property_id)}
    update = {"$set": updated_property}
    return collection.find_one_and_update(property_filter, update)


def delete_property(property_id: str):
    property_filter = {"_id": ObjectId(property_id)}
    return collection.find_one_and_delete(property_filter)
