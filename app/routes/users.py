"""Module providing a User Router"""
from fastapi import APIRouter

from app.domain.user.user_reqeust import UserRequest
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


@router.post(Constant.ROOT_PATH + "/users", tags=[Tags.Users])
def create_user(user: UserRequest):
    """Create new user"""
    return userService.create_user(user)


@router.put(Constant.ROOT_PATH + "/users", tags=[Tags.Users])
def create_user(user: UserRequest):
    """Update new user"""
    return userService.update_user(user)


@router.delete(Constant.ROOT_PATH + "/users", tags=[Tags.Users])
def delete_user(user_id: int):
    """Delete new user"""
    return userService.delete_user(user_id)
