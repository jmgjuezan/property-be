import app.model.tenant_model as repository
from fastapi import APIRouter, Depends, Query, status
from ..schema.tenant_schema import Tenant
from ..schema.user_schema import User
from .security_controller import get_current_user
from typing import Annotated
from ..util.response_wrapper import api_response

router = APIRouter()


@router.delete("/tenants/{tenant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    _current_user: Annotated[User, Depends(get_current_user)],
    tenant_id: str
):
    repository.delete(tenant_id)
    return api_response(data=None, message="Tenant deleted successfully")


@router.get("/tenants")
def find_all(
    _current_user: Annotated[User, Depends(get_current_user)],
    property: Annotated[
        str | None,
        Query(description="Property ID", examples=["6a5b350a213d15cadefcd749"])
    ] = None,
    move_in_year_month: Annotated[
        str | None,
        Query(description="YYYY-MM", examples=["2026-04"])
    ] = None,
    move_out_year_month: Annotated[
        str | None,
        Query(description="YYYY-MM", examples=["2026-04"])
    ] = None,
    move_out: Annotated[
        bool | None,
        Query(description="Move out flag", examples=["true"])
    ] = None,
):
    results = repository.find_all(
        property,
        move_in_year_month,
        move_out_year_month,
        move_out
    )
    message = "Tenant found" if len(results) > 0 else "No tenant found"
    return api_response(data=results, message=message)


@router.get("/tenants/{tenant_id}")
def find_one(
    _current_user: Annotated[User, Depends(get_current_user)],
    tenant_id: str
):
    if len(tenant_id) < 24:
        return api_response(data=None, message="No tenant found")

    result = repository.find_one(tenant_id)
    message = "Tenant found" if result else "No tenant found"
    return api_response(data=result, message=message)


@router.post("/tenants", status_code=status.HTTP_201_CREATED)
def save(
    _current_user: Annotated[User, Depends(get_current_user)],
    tenant: Tenant
):
    json = tenant.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Tenant saved successfully")


@router.patch("/tenants/{tenant_id}")
def update(
    _current_user: Annotated[User, Depends(get_current_user)],
    tenant_id: str,
    tenant: Tenant
):
    json = tenant.model_dump()
    repository.update(tenant_id, json)
    json["_id"] = tenant_id
    return api_response(data=json, message="Tenant updated successfully")
