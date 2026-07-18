from fastapi import APIRouter, status
from ..util.response_wrapper import api_response
from ..model.due_model import save_due, read_dues, read_due, update_due, delete_due
from ..schema.due_schema import DueSchema

router = APIRouter()


@router.get("/dues")
def get_dues():
    dues = read_dues()
    due_list = list(dues)
    for due_item in due_list:
        due_item["_id"] = str(due_item["_id"])
    return api_response(data=due_list, message="All dues retrieved")


@router.get("/dues/{due_id}")
def get_due(due_id: str):
    due_data = read_due(due_id)
    due_data["_id"] = str(due_data["_id"])
    message = "Due retrieved" if due_data else "No due found"
    return api_response(data=due_data, message=message)


@router.post("/dues", status_code=status.HTTP_201_CREATED)
def create_due(new_due: DueSchema):
    due_json = new_due.model_dump()
    result = save_due(due_json)
    due_json["_id"] = str(result.inserted_id)
    return api_response(data=due_json, message="Due created successfully")


@router.put("/dues/{due_id}")
def change_due(due_id: str, due: DueSchema):
    due_json = due.model_dump()
    update_due(due_id, due_json)
    due_json["_id"] = due_id
    return api_response(data=due_json, message="Due changed successfully")


@router.delete("/dues/{due_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_due(due_id: str):
    delete_due(due_id)
    return api_response(data=None, message="Due removed successfully")
