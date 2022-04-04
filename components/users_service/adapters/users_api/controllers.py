import falcon
import jwt
import os
from classic.components import component
from classic.http_auth import (
    authenticate,
    authenticator_needed,
    authorize,
)
from application import services
from .auth import Groups, Permissions
from .join_points import join_point

@authenticator_needed
@component
class Users:
    users_manager: services.UsersManager

    @join_point
    def on_post_registration(self, request, response):
        self.users_manager.registration(**request.media)


    @join_point
    def on_post_login(self, request, response):
        user = self.users_manager.login(**request.media)
        token = jwt.encode(
            {
                "sub": user.id,
                "login": user.login,
                "name": user.name,
                "group": "User"
            },
            os.getenv('SECRET_JWT_KEY'),
            algorithm="HS256"
        )
        response.media = {
            "token": token
        }


#
# @authenticator_needed
# @component
# class Chat:
#     chat_manager: services.ChatManager
#
#     # создание юзера
#     # @join_point
#     # @authenticate
#     # def on_post_create_user(self, request, response):
#     #     request.media['user_id'] = request.context.client.user_id
#     #     self.chat_manager.create_user(**request.media)
#
#     @join_point
#     @authenticate
#     def on_get_user_info(self, request, response):
#         # request.params['user_id'] = request.context.client.user_id
#         user = self.chat_manager.get_user_by_id(**request.params)
#         result = {
#             'user_id': user.id,
#             'user_login': user.login,
#             'user_password': user.password,
#             'user_name': user.name
#         }
#         response.media = result
#
#
#     @join_point
#     @authenticate
#     def on_post_create_chat(self, request, response):
#         request.media['user_id'] = request.context.client.user_id
#         self.chat_manager.create_chat(**request.media)
#
#     @join_point
#     @authenticate
#     def on_get_get_chat(self, request, response):
#         request.params['user_id'] = request.context.client.user_id
#         chat = self.chat_manager.get_chat_by_id_public(**request.params)
#
#         result = {
#             'chat_id': chat.id,
#             'creator_id': chat.creator.user_id,
#             'chat_name': chat.name,
#             'chat_creator_id': chat.creator.id
#         }
#         response.media = result
#
#     @join_point
#     @authenticate
#     def on_post_delete_chat(self, request, response):
#         request.media['user_id'] = request.context.client.user_id
#         self.chat_manager.delete_chat(**request.media)
#
#
#     @join_point
#     @authenticate
#     def on_post_rename_chat(self, request, response):
#         request.media['user_id'] = request.context.client.user_id
#         self.chat_manager.rename_chat(**request.media)
#
#     @join_point
#     @authenticate
#     def on_get_all_chatusers(self, request, response):
#         request.params['user_id'] = request.context.client.user_id
#         users = self.chat_manager.get_all_chatusers(**request.params)
#
#         result = []
#         if users:
#             for user in users:
#                 user = {
#                     'chatuser_id': user.chat_id,
#                     'user_id': user.user.id,
#                     'name': user.user.name,
#                     'invite_datetime': str(user.invite_date)
#                 }
#                 result.append(user)
#         response.media = result
#
#     @join_point
#     @authenticate
#     def on_post_send_message(self, request, response):
#         request.media['user_id'] = request.context.client.user_id
#         self.chat_manager.create_message(**request.media)
#
#     @join_point
#     @authenticate
#     def on_get_chat_messages(self, request, response):
#         request.params['user_id'] = request.context.client.user_id
#         messages = self.chat_manager.get_all_chat_messages(**request.params)
#
#         result = []
#         if messages:
#             for message in messages:
#                 message = {
#                     'message_id': message.id,
#                     'user_id': message.chatuser.user.id,
#                     'chatuser_id': message.chatuser.id,
#                     'text_message': message.text
#                 }
#                 result.append(message)
#
#         response.media = result
#
#
#     @join_point
#     def on_post_registration(self, request, response):
#         user = self.chat_manager.registration(**request.media)
#         # token = jwt.encode(
#         #     {
#         #         "sub": user.id,
#         #         "login": user.login,
#         #         "name": user.name,
#         #         "group": "User"
#         #     },
#         #     os.getenv('SECRET_JWT_KEY'),
#         #     algorithm="HS256"
#         # )
#         # response.media = {
#         #     "token": token
#         # }
#
#     @join_point
#     def on_post_login(self, request, response):
#         user = self.chat_manager.login(**request.media)
#         token = jwt.encode(
#             {
#                 "sub": user.id,
#                 "login": user.login,
#                 "name": user.name,
#                 "group": "User"
#             },
#             os.getenv('SECRET_JWT_KEY'),
#             algorithm="HS256"
#         )
#         response.media = {
#             "token": token
#         }
#
#
#     @join_point
#     @authenticate
#     def on_post_ban_user(self, request, response):
#         request.media['user_id'] = request.context.client.user_id
#         self.chat_manager.ban_user(**request.media)
#
#
#     @join_point
#     @authenticate
#     def on_post_leave_chat(self, request, response):
#         request.media['user_id'] = request.context.client.user_id
#         self.chat_manager.leave_chat(**request.media)

