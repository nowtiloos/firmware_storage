from fastapi import FastAPI
from app.routing.firmwares import router as router_firmwares
from app.routing.auth import router as router_auth
from app.routing.users import router as router_user
from app.routing.modified_firmwares import router as router_modified_firmwares

app: FastAPI = FastAPI()

app.include_router(router_auth)
app.include_router(router_firmwares)
app.include_router(router_user)
app.include_router(router_modified_firmwares)

