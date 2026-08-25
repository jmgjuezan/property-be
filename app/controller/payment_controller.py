from fastapi import APIRouter, status
import app.model.payment_model as repository
from ..util.response_wrapper import api_response
from ..schema.payment_schema import PaymentSchema

router = APIRouter()


@router.get("/payments")
def find_all(paid_by: str | None = None, property: str | None = None):
    results = repository.find_all(paid_by, property)
    message = "Payment found" if len(results) > 0 else "No payment found"
    return api_response(data=results, message=message)


@router.get("/payments/{payment_id}")
def find_one(payment_id: str):
    if len(payment_id) < 24:
        return api_response(data=None, message="No payment found")

    result = repository.find_one(payment_id)
    message = "Payment found" if result else "No payment found"
    return api_response(data=result, message=message)


@router.post("/payments", status_code=status.HTTP_201_CREATED)
def save(new_payment: PaymentSchema):
    json = new_payment.model_dump()
    result = repository.save(json)
    json["_id"] = str(result.inserted_id)
    return api_response(data=json, message="Payment saved successfully")


@router.patch("/payments/{payment_id}")
def update(payment_id: str, updated_payment: PaymentSchema):
    json = updated_payment.model_dump()
    repository.update(payment_id, json)
    json["_id"] = payment_id
    return api_response(data=json, message="Payment updated successfully")


@router.delete("/payments/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(payment_id: str):
    repository.delete(payment_id)
    return api_response(data=None, message="Payment deleted successfully")
