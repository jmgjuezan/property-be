from datetime import datetime, timezone, date
from bson.objectid import ObjectId
from ..db.database import db

collection = db["tenants"]


def read_tenants():
    return collection.find()


def read_tenant(tenant_id: str):
    tenant_filter = {"_id": ObjectId(tenant_id)}
    tenant = collection.find_one(tenant_filter)
    formatted_tenant = format_ui_date(tenant)
    return formatted_tenant


def save_tenant(tenant):
    formatted_tenant = format_db_fields(tenant)
    return collection.insert_one(formatted_tenant)


def update_tenant(tenant_id: str, tenant):
    tenant_filter = {"_id": ObjectId(tenant_id)}
    formatted_tenant = format_db_fields(tenant)
    update = {"$set": formatted_tenant}
    return collection.find_one_and_update(tenant_filter, update)


def delete_tenant(tenant_id: str):
    tenant_filter = {"_id": ObjectId(tenant_id)}
    return collection.find_one_and_delete(tenant_filter)


def format_ui_date(tenant):
    tenant["moveInDate"] = tenant["moveInDate"].date()
    if tenant.get("paymentDate", None) is not None:
        tenant["paymentDate"] = tenant["paymentDate"].date()
    return tenant


def format_db_fields(tenant):
    tenant = format_db_name(tenant)
    tenant = format_db_dates(tenant)
    clean_tenant = {k: v for k, v in tenant.items() if v is not None}
    return clean_tenant


def format_db_name(tenant):
    tenant["firstName"] = tenant["firstName"].title()
    if tenant["middleName"] is not None:
        tenant["middleName"] = tenant["middleName"].title()
    tenant["lastName"] = tenant["lastName"].title()
    return tenant


def format_db_dates(tenant):
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
