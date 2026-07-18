from datetime import datetime, timezone
from bson.objectid import ObjectId
from ..db.database import db

collection = db["tenants"]


def read_tenants():
    return collection.find()


def read_tenant(tenant_id: str):
    tenant_filter = {"_id": ObjectId(tenant_id)}
    return collection.find_one(tenant_filter)


def save_tenant(tenant):
    format_fields(tenant)
    return collection.insert_one(tenant)


def update_tenant(tenant_id: str, tenant):
    tenant_filter = {"_id": ObjectId(tenant_id)}
    format_fields(tenant)
    update = {"$set": tenant}
    return collection.find_one_and_update(tenant_filter, update)


def delete_tenant(tenant_id: str):
    tenant_filter = {"_id": ObjectId(tenant_id)}
    return collection.find_one_and_delete(tenant_filter)

def format_fields(tenant):
    format_name(tenant)
    format_dates(tenant)

def format_name(tenant):
    tenant["firstName"] = tenant["firstName"].capitalize()
    if tenant["middleName"] is not None:
        tenant["middleName"] = tenant["middleName"].capitalize()
    tenant["lastName"] = tenant["lastName"].capitalize()
    return tenant

def format_dates(tenant):
    tenant["moveInDate"] = datetime(
        tenant["moveInDate"].year,
        tenant["moveInDate"].month,
        tenant["moveInDate"].day,
        tzinfo=timezone.utc
    )
    if tenant["paymentDate"] is not None:
        tenant["paymentDate"] = datetime(
            tenant["paymentDate"].year,
            tenant["paymentDate"].month,
            tenant["paymentDate"].day,
            tzinfo=timezone.utc
        )
    return tenant
