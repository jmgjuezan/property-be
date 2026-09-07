import app.model.due_model as repository
from fastapi import APIRouter, Depends, status
from ..schema.due_schema import Due
from ..schema.user_schema import User
from .security_controller import get_current_user
from typing import Annotated
from ..util.response_wrapper import api_response

router = APIRouter()


@router.delete("/dues/{due_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    _current_user: Annotated[User, Depends(get_current_user)],
    due_id: str
):
    repository.delete(due_id)
    return api_response(data=None, message="Due deleted successfully")


@router.get("/dues")
def find_all(_current_user: Annotated[User, Depends(get_current_user)],):
    results = repository.find_all()
    message = "Due found" if len(results) > 0 else "No due found"
    return api_response(data=results, message=message)


@router.get("/dues/{due_id}")
def find_one(
    _current_user: Annotated[User, Depends(get_current_user)],
    due_id: str
):
    if len(due_id) < 24:
        return api_response(data=None, message="No due found")

    result = repository.find_one(due_id)
    message = "Due found" if result else "No due found"
    return api_response(data=result, message=message)


@router.post("/dues", status_code=status.HTTP_201_CREATED)
def save(
    _current_user: Annotated[User, Depends(get_current_user)],
    new_due: Due
):
    json = new_due.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Due saved successfully")


@router.patch("/dues/{due_id}")
def update(
    _current_user: Annotated[User, Depends(get_current_user)],
    due_id: str,
    due: Due
):
    json = due.model_dump()
    repository.update(due_id, json)
    json["_id"] = due_id
    return api_response(data=json, message="Due updated successfully")
