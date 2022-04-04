from typing import List, Optional
import hashlib
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments
from classic.app import DTO, validate_with_dto

from . import errors, interfaces
from .dataclasses import User

# разобрать что это и зачем
join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    name: str
    login: str
    password: str


@component
class UsersManager:
    users_repo: interfaces.UserRepo

    @join_point
    @validate_with_dto
    def registration(self, user_data: UserInfo):
        if self.user_repo.check_user_login(user_data.login):
            raise errors.UserAlreadyExist()
        else:
            user_data.password = hashlib.sha256(bytes(user_data.password)).hexdigest()
            user = self.users_repo.add_instance(user_data)
            return user

    @join_point
    @validate_arguments
    def get_user_by_id(self, user_id: int):
        user = self.users_repo.get_by_id(user_id)
        if not user:
            raise errors.UncorrectedParams()
        return user

    @join_point
    @validate_arguments
    def get_all_users(self):
        return self.get_all_users()

    @join_point
    @validate_arguments
    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.users_repo.delete_by_id(user_id)
        else:
            raise errors.UncorrectedParams()

    @join_point
    @validate_with_dto
    def update_user(self, user_data: UserInfo):
        pass

    @join_point
    @validate_arguments
    def login(self, login: str, password: str):
        password = hashlib.sha256(bytes(password)).hexdigest()
        user = self.users_repo.authorization(login, password)
        if user:
            return user
        else:
            raise errors.UncorrectedLoginPassword()
