"""Module providing a User model."""
from pydantic import BaseModel


class UserModel(BaseModel):
    """User Model"""
    id: int
    username: str
