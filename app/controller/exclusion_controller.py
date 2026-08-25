from fastapi import APIRouter, status
import app.model.exclusion_model as repository
from datetime import date
from ..util.response_wrapper import api_response
from ..schema.exclusion_schema import ExclusionSchema

router = APIRouter()


@router.get("/exclusions")
def find_all(
        name: str | None = None,
        property: str | None = None,
        from_date: date | None = None,
        to_date: date | None = None
):
    results = repository.find_all(name, property, from_date, to_date)
    message = "Exclusion found" if len(results) > 0 else "No exclusion found"
    return api_response(data=results, message=message)


@router.get("/exclusions/{exclusion_id}")
def find_one(exclusion_id: str):
    if len(exclusion_id) < 24:
        return api_response(data=None, message="No exclusion found")

    result = repository.find_one(exclusion_id)
    message = "Exclusion found" if result else "No exclusion found"
    return api_response(data=result, message=message)


@router.post("/exclusions", status_code=status.HTTP_201_CREATED)
def save(new_exclusion: ExclusionSchema):
    json = new_exclusion.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Exclusion saved successfully")


@router.patch("/exclusions/{exclusion_id}")
def update(exclusion_id: str, exclusion: ExclusionSchema):
    json = exclusion.model_dump()
    repository.update(exclusion_id, json)
    json["_id"] = exclusion_id
    return api_response(data=json, message="Exclusion updated successfully")


@router.delete("/exclusions/{exclusion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(exclusion_id: str):
    repository.delete(exclusion_id)
    return api_response(data=None, message="Exclusion deleted successfully")
