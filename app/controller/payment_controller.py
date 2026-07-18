from fastapi import APIRouter, status
from ..util.response_wrapper import api_response
from ..model.payment_model import save_payment, read_payments, read_payment, update_payment, delete_payment
from ..schema.payment_schema import PaymentSchema

router = APIRouter()


@router.get("/payments")
def get_payments():
    payments = read_payments()
    payment_list = list(payments)
    for payment_item in payment_list:
        payment_item["_id"] = str(payment_item["_id"])
    return api_response(data=payment_list, message="All payments retrieved")


@router.get("/payments/{payment_id}")
def get_payment(payment_id: str):
    payment_data = read_payment(payment_id)
    message = "Payment retrieved" if payment_data else "No payment found"
    return api_response(data=payment_data, message=message)


@router.post("/payments", status_code=status.HTTP_201_CREATED)
def create_payment(new_payment: PaymentSchema):
    payment_json = new_payment.model_dump()
    result = save_payment(payment_json)
    payment_json["_id"] = str(result.inserted_id)
    return api_response(data=payment_json, message="Payment created successfully")


@router.patch("/payments/{payment_id}")
def change_payment(payment_id: str, payment: PaymentSchema):
    payment_json = payment.model_dump()
    update_payment(payment_id, payment_json)
    payment_json["_id"] = payment_id
    return api_response(data=payment_json, message="Payment changed successfully")


@router.delete("/payments/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_payment(payment_id: str):
    delete_payment(payment_id)
    return api_response(data=None, message="Payment removed successfully")
