from bson.objectid  import ObjectId
from ..db.database import db
from ..schema.property_schema import PropertySchema

COLLECTION_NAME = "property"

collection = db[COLLECTION_NAME]

def read_properties():
    return collection.find()

def read_property(property_id: str):
    filter = { "_id": ObjectId(property_id) }
    return collection.find_one(filter)

def save_property(property):
    return collection.insert_one(property)

def update_property(property_id: str, property):
    filter = { "_id": ObjectId(property_id) }
    update = { "$set": property }
    return collection.find_one_and_update(filter, update)

def delete_property(property_id: str):
    filter = { "_id": ObjectId(property_id) }
    return collection.find_one_and_delete(filter)
