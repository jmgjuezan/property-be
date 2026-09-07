from bson import ObjectId
from ..db.database import db
from ..util.format_helper import format_ui_field

table = "users"
collection = db[table]
fields = []


def find_by_username(username: str):
    query_filter = {
        "username": username,
        "$or": [
            {"deleted": { "$exists": False }},
            {"deleted": False}
        ]
    }
    result = collection.find_one(query_filter)
    if result is not None:
        result = format_ui_field(result, fields)
    return result


def update(model_id, uuid):
    query_filter = {"_id": ObjectId(model_id)}
    model = {"$set": {"jwt": uuid}}
    return collection.find_one_and_update(query_filter, model)