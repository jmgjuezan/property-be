from bson.objectid import ObjectId
from ..db.database import db

collection = db["exclusions"]


def read_exclusions():
    return collection.find()


def read_exclusion(exclusion_id: str):
    exclusion_filter = {"_id": ObjectId(exclusion_id)}
    return collection.find_one(exclusion_filter)


def save_exclusion(new_exclusion):
    return collection.insert_one(new_exclusion)


def update_exclusion(exclusion_id: str, updated_exclusion):
    exclusion_filter = {"_id": ObjectId(exclusion_id)}
    update = {"$set": updated_exclusion}
    return collection.find_one_and_update(exclusion_filter, update)


def delete_exclusion(exclusion_id: str):
    exclusion_filter = {"_id": ObjectId(exclusion_id)}
    return collection.find_one_and_delete(exclusion_filter)
