import app.model.payment_model as repository
from fastapi import APIRouter, Depends, status
from ..schema.payment_schema import Payment
from ..schema.user_schema import User
from .security_controller import get_current_user
from typing import Annotated
from ..util.response_wrapper import api_response

router = APIRouter()


@router.delete("/payments/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    _current_user: Annotated[User, Depends(get_current_user)],
    payment_id: str
):
    repository.delete(payment_id)
    return api_response(data=None, message="Payment deleted successfully")


@router.get("/payments")
def find_all(
    _current_user: Annotated[User, Depends(get_current_user)],
    paid_by: str | None = None,
    property: str | None = None
):
    results = repository.find_all(paid_by, property)
    message = "Payment found" if len(results) > 0 else "No payment found"
    return api_response(data=results, message=message)


@router.get("/payments/{payment_id}")
def find_one(
    _current_user: Annotated[User, Depends(get_current_user)],
    payment_id: str
):
    if len(payment_id) < 24:
        return api_response(data=None, message="No payment found")

    result = repository.find_one(payment_id)
    message = "Payment found" if result else "No payment found"
    return api_response(data=result, message=message)


@router.post("/payments", status_code=status.HTTP_201_CREATED)
def save(
    _current_user: Annotated[User, Depends(get_current_user)],
    new_payment: Payment
):
    json = new_payment.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Payment saved successfully")


@router.patch("/payments/{payment_id}")
def update(
    _current_user: Annotated[User, Depends(get_current_user)],
    payment_id: str,
    updated_payment: Payment
):
    json = updated_payment.model_dump()
    repository.update(payment_id, json)
    json["_id"] = payment_id
    return api_response(data=json, message="Payment updated successfully")
