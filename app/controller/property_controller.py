from fastapi import APIRouter, status
import app.model.property_model as repository
from ..util.response_wrapper import api_response
from ..schema.property_schema import PropertySchema

router = APIRouter()


@router.get("/properties")
def find_all():
    results = repository.find_all()
    message = "Property found" if len(results) > 0 else "No property found"
    return api_response(data=results, message=message)


@router.get("/properties/{property_id}")
def find_one(property_id: str):
    if len(property_id) < 24:
        return api_response(data=None, message="No property found")

    result = repository.find_one(property_id)
    message = "Property found" if result else "No property found"
    return api_response(data=result, message=message)


@router.post("/properties", status_code=status.HTTP_201_CREATED)
def save(new_property: PropertySchema):
    json = new_property.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Property saved successfully")


@router.patch("/properties/{property_id}")
def update(property_id: str, updated_property: PropertySchema):
    json = updated_property.model_dump()
    repository.update(property_id, json)
    json["_id"] = property_id
    return api_response(data=json, message="Property updated successfully")


@router.delete("/properties/{property_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(property_id: str):
    repository.delete(property_id)
    return api_response(data=None, message="Property deleted successfully")
