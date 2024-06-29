from app.domain.user.user_model import UserModel
from app.util.util_constant import Constant
from fastapi import APIRouter

router = APIRouter()
@router.get(Constant.ROOT_PATH+"/users", tags=["users"])
def fetch_user():
   
    return [
        UserModel(id=1,username="John Python"),

    ]

@router.get(Constant.ROOT_PATH+"/users/{item_id}", tags=["users"])
def fetch_user_by_id(item_id: int):
    return UserModel(id=item_id,username="John Python")
