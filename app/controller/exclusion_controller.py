import app.model.exclusion_model as repository
from datetime import date
from fastapi import APIRouter, Depends, status
from ..schema.exclusion_schema import Exclusion
from ..schema.user_schema import User
from .security_controller import get_current_user
from typing import Annotated
from ..util.response_wrapper import api_response

router = APIRouter()


@router.delete("/exclusions/{exclusion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    _current_user: Annotated[User, Depends(get_current_user)],
    exclusion_id: str
):
    repository.delete(exclusion_id)
    return api_response(data=None, message="Exclusion deleted successfully")


@router.get("/exclusions")
def find_all(
    _current_user: Annotated[User, Depends(get_current_user)],
    name: str | None = None,
    property: str | None = None,
    from_date: date | None = None,
    to_date: date | None = None
):
    results = repository.find_all(name, property, from_date, to_date)
    message = "Exclusion found" if len(results) > 0 else "No exclusion found"
    return api_response(data=results, message=message)


@router.get("/exclusions/{exclusion_id}")
def find_one(
    _current_user: Annotated[User, Depends(get_current_user)],
    exclusion_id: str
):
    if len(exclusion_id) < 24:
        return api_response(data=None, message="No exclusion found")

    result = repository.find_one(exclusion_id)
    message = "Exclusion found" if result else "No exclusion found"
    return api_response(data=result, message=message)


@router.post("/exclusions", status_code=status.HTTP_201_CREATED)
def save(
    _current_user: Annotated[User, Depends(get_current_user)],
    new_exclusion: Exclusion
):
    json = new_exclusion.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Exclusion saved successfully")


@router.patch("/exclusions/{exclusion_id}")
def update(
    _current_user: Annotated[User, Depends(get_current_user)],
    exclusion_id: str,
    exclusion: Exclusion
):
    json = exclusion.model_dump()
    repository.update(exclusion_id, json)
    json["_id"] = exclusion_id
    return api_response(data=json, message="Exclusion updated successfully")
