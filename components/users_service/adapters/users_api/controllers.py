import jwt
import os

import jwt
from classic.components import component
from classic.http_auth import (
    authenticator_needed,
)

from application import services
from .join_points import join_point


@authenticator_needed
@component
class Users:
    users_manager: services.UsersManager


    @join_point
    def on_get_user_info(self, request, response):
        # request.params['user_id'] = request.context.client.user_id
        user = self.users_manager.get_user_by_id(**request.params)
        result = {
            'user_id': user.id,
            'user_login': user.login,
            'user_password': user.password,
            'user_name': user.name
        }
        response.media = result

    @join_point
    def on_post_delete(self, request, response):
        # request.media['user_id'] = request.context.client.user_id
        self.users_manager.delete_user(**request.media)

    @join_point
    def on_post_registration(self, request, response):
        self.users_manager.registration(**request.media)

    @join_point
    def on_post_login(self, request, response):
        user = self.users_manager.login(**request.media)
        # TODO: Закинуть SECRET KEY в ENV
        token = jwt.encode(
            {
                "sub": user.id,
                "login": user.login,
                "name": user.name,
                "group": "User"
            },
            'SECRET_JWT_KEY',
            algorithm="HS256"
        )
        response.media = {
            "token": token
        }
