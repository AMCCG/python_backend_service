from fastapi import APIRouter

from app.routes.tags import Tags
from app.util.util_constant import Constant

router = APIRouter()


@router.get(Constant.ROOT_PATH + "/actuator/health/liveness", tags=[Tags.Actuator])
def health_liveness():
    """Actuator health liveness"""
    return {"status": "UP"}


@router.get(Constant.ROOT_PATH + "/actuator/health/readiness", tags=[Tags.Actuator])
def health_readiness():
    """Actuator health readiness"""
    return {"status": "UP"}
