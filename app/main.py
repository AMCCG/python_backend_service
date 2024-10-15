"""Module providing a Main App"""
from fastapi import FastAPI, Request
from app.routes import users, model, actuator
from app.util.util_constant import Constant

app = FastAPI()

app.include_router(users.router)
app.include_router(model.router)
app.include_router(actuator.router)


@app.get(Constant.ROOT_PATH + "/greeting")
def greeting(request: Request):
    """Greeting"""
    return {
        "greeting": "Hello World Python",
        "hostname": "http://127.0.0.1:8000",
        "version": "v1",
        "domain": request.base_url
    }
