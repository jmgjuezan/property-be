from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .controller.property_controller import router as property_router

app = FastAPI()

app.include_router(property_router, prefix="/api/v1", tags=["Property"])

@app.get("/")
async def index():
   return RedirectResponse(url="/docs")

@app.get("api/health")
async def health():
   return "ok"