from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .controller.property_controller import router as property_router
from .controller.tenant_controller import router as tenant_router
from .controller.due_controller import router as due_router
from .controller.exclusion_controller import router as exclusion_router
from .controller.payment_controller import router as payment_router

app = FastAPI()

app.include_router(property_router, prefix="/api/v1", tags=["Property"])
app.include_router(tenant_router, prefix="/api/v1", tags=["Tenant"])
app.include_router(due_router, prefix="/api/v1", tags=["Due"])
app.include_router(exclusion_router, prefix="/api/v1", tags=["Exclusion"])
app.include_router(payment_router, prefix="/api/v1", tags=["Payment"])


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse(url="/docs")


@app.get("api/health")
async def health():
    return "ok"
