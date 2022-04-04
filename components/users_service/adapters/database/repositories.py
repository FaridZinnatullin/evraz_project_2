from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
import hashlib
from application.dataclasses import User
from sqlalchemy.sql import select
from adapters.database.tables import users as USERS_TABLE
from application import interfaces


@component
class UsersRepo(BaseRepository, interfaces.UserRepo):

    def get_by_id(self, user_id: int):
        pass
        # query = select(User).where(User.id == user_id)
        # return self.session.execute(query).scalars().one_or_none()

    def get_all(self):
        pass

    def add_instance(self, user: User):
        query = USERS_TABLE.insert().values(
            name=user.name,
            login=user.login,
            password=user.password
        )
        self.session.execute(query)

    def delete_by_id(self, user_id: int):
        pass

    def update_by_id(self, user: User):
        pass

    def authorization(self, login: str, password: str):
        # query = select(User).where(and_(User.login == login, User.password == password))
        # user = self.session.execute(query).scalars().first()
        # return user
        pass