from fastapi import FastAPI
from app.routing.firmware import router as router_firmware
from app.routing.auth import router as router_auth

app: FastAPI = FastAPI()

app.include_router(router_firmware)
app.include_router(router_auth)
