from fastapi import FastAPI
from app.routing.firmware import router as router_firmware

app: FastAPI = FastAPI()

app.include_router(router_firmware)
