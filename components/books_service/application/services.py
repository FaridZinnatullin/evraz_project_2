from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher
from classic.messaging_kombu import BrokerScheme, KombuPublisher
from kombu import Exchange, Queue, Connection
from pydantic import validate_arguments
from attr import asdict

from . import errors, interfaces
from .dataclasses import Book

# разобрать что это и зачем
join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    name: str
    author: str
    available: bool


@component
class BooksManager:
    books_repo: interfaces.BookRepo
    publisher: Publisher

    @join_point
    @validate_with_dto
    def create(self, book_data: BookInfo):

        book = Book(name=book_data.name,
                    author=book_data.author,
                    available=book_data.available)
        self.books_repo.add_instance(book)

        self.publisher.plan(
            Message('LogsExchange', {'action': 'create',
                                     'object_type': 'book',
                                     'object_info': book_data.__dict__
                                     })
        )


    @join_point
    @validate_arguments
    def get_book_by_id(self, book_id: int):
        book = self.books_repo.get_by_id(book_id)
        if not book:
            raise errors.UncorrectedParams()
        return book

    @join_point
    @validate_arguments
    def get_all_books(self):
        return self.get_all_books()

    @join_point
    @validate_arguments
    def delete_book(self, book_id: int):
        book = self.get_book_by_id(book_id)
        if book:
            self.books_repo.delete_by_id(book_id)
        else:
            raise errors.UncorrectedParams()

    @join_point
    @validate_with_dto
    def update_book(self, book_data: BookInfo):
        pass
