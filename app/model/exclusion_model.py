from datetime import datetime, timezone
from bson.objectid import ObjectId
from ..db.database import db

collection = db["exclusions"]


def read_exclusions():
    return collection.find()


def read_exclusion(exclusion_id: str):
    if len(exclusion_id) < 24:
        return None
    exclusion_filter = {"_id": ObjectId(exclusion_id)}
    exclusion = collection.find_one(exclusion_filter)
    if exclusion is None:
        return None
    exclusion["_id"] = str(exclusion["_id"])
    formatted_exclusion = format_ui_date(exclusion)
    return formatted_exclusion


def save_exclusion(new_exclusion):
    formatted_exclusion = format_db_fields(new_exclusion)
    return collection.insert_one(formatted_exclusion)


def update_exclusion(exclusion_id: str, updated_exclusion):
    exclusion_filter = {"_id": ObjectId(exclusion_id)}
    formatted_exclusion = format_db_fields(updated_exclusion)
    update = {"$set": formatted_exclusion}
    return collection.find_one_and_update(exclusion_filter, update)


def delete_exclusion(exclusion_id: str):
    exclusion_filter = {"_id": ObjectId(exclusion_id)}
    return collection.find_one_and_delete(exclusion_filter)


def format_ui_date(exclusion):
    if exclusion.get("exclusionDate", None) is not None:
        exclusion["exclusionDate"] = exclusion["exclusionDate"].date()
    if exclusion.get("exclusionDateFrom", None) is not None:
        exclusion["exclusionDateFrom"] = exclusion["exclusionDateFrom"].date()
    if exclusion.get("exclusionDateTo", None) is not None:
        exclusion["exclusionDateTo"] = exclusion["exclusionDateTo"].date()
    return exclusion


def format_db_fields(exclusion):
    exclusion = format_db_date(exclusion)
    clean_property = {k: v for k, v in exclusion.items() if v is not None}
    return clean_property


def format_db_date(exclusion):
    if exclusion["exclusionDate"] is not None:
        exclusion["exclusionDate"] = datetime(
            exclusion["exclusionDate"].year,
            exclusion["exclusionDate"].month,
            exclusion["exclusionDate"].day,
            tzinfo=timezone.utc
        )
    if exclusion["exclusionDateFrom"] is not None:
        exclusion["exclusionDateFrom"] = datetime(
            exclusion["exclusionDateFrom"].year,
            exclusion["exclusionDateFrom"].month,
            exclusion["exclusionDateFrom"].day,
            tzinfo=timezone.utc
        )
    if exclusion["exclusionDateTo"] is not None:
        exclusion["exclusionDateTo"] = datetime(
            exclusion["exclusionDateTo"].year,
            exclusion["exclusionDateTo"].month,
            exclusion["exclusionDateTo"].day,
            tzinfo=timezone.utc
        )
    return exclusion