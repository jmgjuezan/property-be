from fastapi import APIRouter, status
from ..util.response_wrapper import api_response
from ..model.exclusion_model import save_exclusion, read_exclusions, read_exclusion, update_exclusion, delete_exclusion
from ..schema.exclusion_schema import ExclusionSchema

router = APIRouter()


@router.get("/exclusions")
def get_exclusions():
    exclusions = read_exclusions()
    exclusion_list = list(exclusions)
    for exclusion_item in exclusion_list:
        exclusion_item["_id"] = str(exclusion_item["_id"])
    return api_response(data=exclusion_list, message="All exclusions retrieved")


@router.get("/exclusions/{exclusion_id}")
def get_exclusion(exclusion_id: str):
    exclusion_data = read_exclusion(exclusion_id)
    exclusion_data["_id"] = str(exclusion_data["_id"])
    message = "Exclusion retrieved" if exclusion_data else "No exclusion found"
    return api_response(data=exclusion_data, message=message)


@router.post("/exclusions", status_code=status.HTTP_201_CREATED)
def create_exclusion(new_exclusion: ExclusionSchema):
    exclusion_json = new_exclusion.model_dump()
    result = save_exclusion(exclusion_json)
    exclusion_json["_id"] = str(result.inserted_id)
    return api_response(data=exclusion_json, message="Exclusion created successfully")


@router.patch("/exclusions/{exclusion_id}")
def change_exclusion(exclusion_id: str, exclusion: ExclusionSchema):
    exclusion_json = exclusion.model_dump()
    update_exclusion(exclusion_id, exclusion_json)
    exclusion_json["_id"] = exclusion_id
    return api_response(data=exclusion_json, message="Exclusion changed successfully")


@router.delete("/exclusions/{exclusion_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_exclusion(exclusion_id: str):
    delete_exclusion(exclusion_id)
    return api_response(data=None, message="Exclusion removed successfully")
