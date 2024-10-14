from fastapi import APIRouter

from app.domain.model.model_service import ModelService
from app.util.util_constant import Constant

router = APIRouter()
model_service = ModelService()


@router.get(Constant.ROOT_PATH + "/model/1/{input}", tags=["model"])
def fetch_model(input: int) -> str:
    return model_service.predict(input)
