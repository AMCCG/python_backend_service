"""Module providing a Main App"""
from fastapi import FastAPI, Request
from app.routes import users
from app.util.util_constant import Constant

app = FastAPI()

app.include_router(users.router)

@app.get(Constant.ROOT_PATH+"/actuator/health/liveness")
def health_liveness():
    """Actuator health liveness"""
    return {"status": "UP"}

@app.get(Constant.ROOT_PATH+"/actuator/health/readiness")
def health_readiness():
    """Actuator health readiness"""
    return {"status": "UP"}

@app.get(Constant.ROOT_PATH+"/greeting")
def greeting( request: Request):
    """Greeting"""
    return {
        "greeting":"Hello World Python",
        "hostname":"http://127.0.0.1:8000",
        "version":"v1",
        "domain": request.base_url
    }

