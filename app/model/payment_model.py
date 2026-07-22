from datetime import datetime, timezone
from bson.objectid import ObjectId
from ..db.database import db

collection = db["payments"]


def read_payments(paid_by: str | None = None, property: str | None = None):
    if paid_by is None and property is None:
        return collection.find({"deleted": { "$exists": False }})
    elif paid_by is None:
        return collection.find({ "property": property, "deleted": { "$exists": False }})
    elif property is None:
        return collection.find({ "tenant": paid_by, "deleted": { "$exists": False }})
    else:
        return collection.find({
            "tenant": paid_by, "property": property, "deleted": { "$exists": False }
        })


def read_payment(payment_id: str):
    if len(payment_id) < 24:
        return None
    payment_filter = {"_id": ObjectId(payment_id), "deleted": { "$exists": False }}
    payment = collection.find_one(payment_filter)
    if payment is None:
        return None
    payment["_id"] = str(payment["_id"])
    formatted_payment = format_ui_date(payment)
    return formatted_payment


def save_payment(new_payment):
    formatted_tenant = format_db_fields(new_payment)
    return collection.insert_one(formatted_tenant)


def update_payment(payment_id: str, updated_payment):
    payment_filter = {"_id": ObjectId(payment_id)}
    formatted_payment = format_db_fields(updated_payment)
    update = {"$set": formatted_payment}
    return collection.find_one_and_update(payment_filter, update)


def delete_payment(payment_id: str):
    payment_filter = {"_id": ObjectId(payment_id)}
    update = {"$set": {"deleted": True}}
    return collection.find_one_and_update(payment_filter, update)


def format_ui_date(payment):
    payment["paymentDate"] = payment["paymentDate"].date()
    return payment

def format_db_fields(payment):
    payment = format_db_date(payment)
    clean_property = {k: v for k, v in payment.items() if v is not None}
    return clean_property

def format_db_date(payment):
    payment["paymentDate"] = datetime(
        payment["paymentDate"].year,
        payment["paymentDate"].month,
        payment["paymentDate"].day,
        tzinfo=timezone.utc
    )
    return payment