from bson.objectid import ObjectId
from ..db.database import db

collection = db["payments"]


def read_payments():
    return collection.find()


def read_payment(payment_id: str):
    payment_filter = {"_id": ObjectId(payment_id)}
    return collection.find_one(payment_filter)


def save_payment(new_pamyent):
    return collection.insert_one(new_pamyent)


def update_payment(payment_id: str, updated_payment):
    payment_filter = {"_id": ObjectId(payment_id)}
    update = {"$set": updated_payment}
    return collection.find_one_and_update(payment_filter, update)


def delete_payment(payment_id: str):
    payment_filter = {"_id": ObjectId(payment_id)}
    return collection.find_one_and_delete(payment_filter)
