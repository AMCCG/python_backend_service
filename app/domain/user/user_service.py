"""Module providing a User Service."""
import dataclasses
from app.domain.user.user_model import UserModel
from app.domain.user.user_reqeust import UserRequest

user_database: list[UserModel] = [
    UserModel(id=1, username="John Python"),
    UserModel(id=2, username="Jame Python"),
    UserModel(id=3, username="Bruce Python"),
    UserModel(id=4, username="Arm Python"),
    UserModel(id=5, username="Bounty Python"),
    UserModel(id=6, username="James Python"),
]


@dataclasses.dataclass
class UserService:
    """Class User Service"""

    def get_users(self):
        """Get all user"""
        users: list = user_database
        return users

    def get_users_by_id(self, user_id: int):
        """Get user by id"""
        users = self.get_users()
        result = filter(lambda user: user.id == user_id, users)
        users = list(result)
        return users[0] if len(users) > 0 else None

    def create_user(self, user_request: UserRequest):
        username = user_request.username
        user_id: int = len(user_database)
        user: UserModel = UserModel(id=user_id, username=username)
        user_database.append(user)
        user_database.sort(key=lambda x: x.id)
        return self.get_users_by_id(user_id)

    def update_user(self, user):
        fetch_user = self.get_users_by_id(user.id)
        if fetch_user is not None:
            fetch_user.username = user.username
            user_database.append(fetch_user)
            user_database.sort(key=lambda x: x.id)
            return fetch_user
        else:
            return None

    def delete_user(self, user_id: int):
        user = self.get_users_by_id(user_id)
        if user is not None:
            idx: int = user_database.index(user)
            print(idx)
            user_database.remove(user)
            return True
        return False
