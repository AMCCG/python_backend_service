from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Request
from app.routes import users
from app.util.util_constant import Constant

app = FastAPI()

app.include_router(users.router)

@app.get(Constant.ROOT_PATH+"/health/liveness")
def health_liveness( request: Request):
    return {"status": "OK"}

@app.get(Constant.ROOT_PATH+"/greeting")
def greeting( request: Request):
    return {
        "greeting":"Hello World Python",
        "hostname":"http://127.0.0.1:8000",
        "version":"v1",
        "domain": request.base_url
    }