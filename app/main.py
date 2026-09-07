import app.model.user_model as repository
from .controller.due_controller import router as due_router
from .controller.exclusion_controller import router as exclusion_router
from .controller.payment_controller import router as payment_router
from .controller.property_controller import router as property_router
from .controller.tenant_controller import router as tenant_router
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from .schema.token_schema import Token
from typing import Annotated
from .util.security_helper import create_access_token, verify_password

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(due_router, prefix="/api/v1", tags=["Due"])
app.include_router(exclusion_router, prefix="/api/v1", tags=["Exclusion"])
app.include_router(payment_router, prefix="/api/v1", tags=["Payment"])
app.include_router(property_router, prefix="/api/v1", tags=["Property"])
app.include_router(tenant_router, prefix="/api/v1", tags=["Tenant"])


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse(url="/docs")


@app.get("api/health")
async def health():
    return "ok"


@app.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = repository.find_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user["username"]})
    return Token(access_token=access_token, token_type="bearer")
