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
class Books:
    books_manager: services.BooksManager

    @join_point
    def on_get_book_info(self, request, response):
        # request.params['book_id'] = request.context.client.book_id
        book = self.books_manager.get_book_by_id(**request.params)
        result = {
            'book_id': book.id,
            'book_name': book.name,
            'book_author': book.author,
            'book_available': book.available
        }
        response.media = result

    @join_point
    def on_post_create(self, request, response):
        # request.media['book_id'] = request.context.client.book_id
        print("555")
        self.books_manager.create(**request.media)


    @join_point
    def on_post_delete(self, request, response):
        # request.media['book_id'] = request.context.client.book_id
        self.books_manager.delete_book(**request.media)

    @join_point
    def on_post_create(self, request, response):
        self.books_manager.create(**request.media)


