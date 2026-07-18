from fastapi import APIRouter, status
from ..util.response_wrapper import api_response
from ..model.tenant_model import save_tenant, read_tenants, read_tenant, update_tenant, delete_tenant
from ..schema.tenant_schema import TenantSchema

router = APIRouter()

@router.get("/tenants")
def get_tenants():
    tenants = read_tenants()
    tenant_list = list(tenants)
    for tenant in tenant_list:
        tenant["_id"] = str(tenant["_id"])
    return api_response(data = tenant_list, message = "All tenants retrieved")

@router.get("/tenants/{tenant_id}")
def get_tenant(tenant_id: str):
    tenant = read_tenant(tenant_id)
    message = "Tenant retrieved" if tenant else "No tenant found"
    return api_response(data = tenant, message = message)

@router.post("/tenants", status_code = status.HTTP_201_CREATED)
def create_tenant(tenant: TenantSchema):
    tenant_json = tenant.model_dump()
    result = save_tenant(tenant_json)
    tenant_json["_id"] = str(result.inserted_id)
    return api_response(data = tenant_json, message = "Tenant created successfully")

@router.patch("/tenants/{tenant_id}")
def change_tenant(tenant_id: str, tenant: TenantSchema):
    tenant_json = tenant.model_dump()
    update_tenant(tenant_id, tenant_json)
    tenant_json["_id"] = tenant_id
    return api_response(data = tenant_json, message = "Tenant changed successfully")

@router.delete("/tenants/{tenant_id}", status_code = status.HTTP_204_NO_CONTENT)
def remove_tenant(tenant_id: str):
    delete_tenant(tenant_id)
    return api_response(data = None, message = "Tenant removed successfully")
