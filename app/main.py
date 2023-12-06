from fastapi import FastAPI
from app.controllers.flash import router as router_flash

app: FastAPI = FastAPI()

app.include_router(router_flash)
