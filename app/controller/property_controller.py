from fastapi import APIRouter, status
from ..util.response_wrapper import api_response
from ..model.property_model import save_property, read_properties, read_property, update_property, delete_property
from ..schema.property_schema import PropertySchema

router = APIRouter()


@router.get("/properties")
def get_properties():
    properties = read_properties()
    property_list = list(properties)
    for property_item in property_list:
        property_item["_id"] = str(property_item["_id"])
    return api_response(data=property_list, message="All properties retrieved")


@router.get("/properties/{property_id}")
def get_property(property_id: str):
    property_data = read_property(property_id)
    property_data["_id"] = str(property_data["_id"])
    message = "Property retrieved" if property_data else "No property found"
    return api_response(data=property_data, message=message)


@router.post("/properties", status_code=status.HTTP_201_CREATED)
def create_property(new_property: PropertySchema):
    property_json = new_property.model_dump()
    result = save_property(property_json)
    property_json["_id"] = str(result.inserted_id)
    return api_response(data=property_json, message="Property created successfully")


@router.put("/properties/{property_id}")
def change_property(property_id: str, property: PropertySchema):
    property_json = property.model_dump()
    update_property(property_id, property_json)
    property_json["_id"] = property_id
    return api_response(data=property_json, message="Property changed successfully")


@router.delete("/properties/{property_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_property(property_id: str):
    delete_property(property_id)
    return api_response(data=None, message="Property removed successfully")
