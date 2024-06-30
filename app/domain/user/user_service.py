"""Module providing a User Service."""
import dataclasses
from app.domain.user.user_model import UserModel

@dataclasses.dataclass
class UserService:
    """Class User Service"""

    def get_users(self):
        """Get all user"""
        users:list=[
           UserModel(id=1,username="John Python"),
           UserModel(id=2,username="Jame Python"),
           UserModel(id=3,username="Bruce Python")
        ]
        return users

    def get_users_by_id(self,user_id: int):
        """Get user by id"""
        users = self.get_users()
        result = filter(lambda user: user.id == user_id, users)
        users = list(result)
        return  users[0] if len(users) > 0 else None
