from bson.objectid import ObjectId
from ..db.database import db

collection = db["dues"]


def read_dues():
    return collection.find()


def read_due(due_id: str):
    if len(due_id) < 24:
        return None
    due_filter = {"_id": ObjectId(due_id)}
    return collection.find_one(due_filter)


def save_due(new_due):
    return collection.insert_one(new_due)


def update_due(due_id: str, updated_due):
    due_filter = {"_id": ObjectId(due_id)}
    update = {"$set": updated_due}
    return collection.find_one_and_update(due_filter, update)


def delete_due(due_id: str):
    due_filter = {"_id": ObjectId(due_id)}
    return collection.find_one_and_delete(due_filter)
