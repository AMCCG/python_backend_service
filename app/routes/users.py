"""Module providing a User Router"""
from fastapi import APIRouter
from app.domain.user.user_service import UserService
from app.routes.tags import Tags
from app.util.util_constant import Constant

router = APIRouter()
userService: UserService = UserService()


@router.get(Constant.ROOT_PATH + "/users", tags=[Tags.Users])
def fetch_user():
    """Fetch all user"""
    return userService.get_users()


@router.get(Constant.ROOT_PATH + "/users/{user_id}", tags=[Tags.Users])
def fetch_user_by_id(user_id: int):
    """Fetch user by id"""
    return userService.get_users_by_id(user_id)
