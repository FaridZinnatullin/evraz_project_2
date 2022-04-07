from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher
from pydantic import validate_arguments

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

        if not self.books_repo.get_by_name_author(author=book_data.author, name=book_data.name):
            book = self.books_repo.add_instance(book)

            self.publisher.plan(
                Message('LogsExchange', {'action': 'create',
                                         'object_type': 'book',
                                         'object_id': book.id
                                         })
            )
        else:
            raise errors.BookAlreadyExist

    @join_point
    @validate_arguments
    def get_book_by_id(self, book_id: int) -> Book:
        book = self.books_repo.get_by_id(book_id)
        if not book:
            raise errors.UncorrectedParams()
        return book

    @join_point
    @validate_arguments
    def get_all_books(self):
        return self.books_repo.get_all()

    @join_point
    @validate_arguments
    def delete_book(self, book_id: int):
        book = self.get_book_by_id(book_id)
        if book:
            self.books_repo.delete_by_id(book_id)
        else:
            raise errors.UncorrectedParams()

        self.publisher.plan(
            Message('LogsExchange', {'action': 'delete',
                                     'object_type': 'book',
                                     'object_id': book.id
                                     })
        )

    @join_point
    @validate_arguments
    def get_book(self, book_id: int, user_id: int):
        book = self.get_book_by_id(book_id)
        if book:
            if book.available:
                book.available = False
                self.books_repo.add_instance(book)
                self.publisher.plan(
                    Message('LogsExchange', {'action': 'get book',
                                             'object_type': 'book',
                                             'object_id': book_id
                                             }),

                    Message('LogsExchange', {'action': 'user get book',
                                             'object_type': 'user',
                                             'object_id': user_id
                                             })
                )
            else:
                raise errors.BookIsUnavailable
        else:
            raise errors.UncorrectedParams


    @join_point
    @validate_arguments
    def return_book(self, book_id: int, user_id: int):
        book = self.get_book_by_id(book_id)
        if book:
            book.available = True
            self.books_repo.add_instance(book)
            self.publisher.plan(
                Message('LogsExchange', {'action': 'return book',
                                         'object_type': 'book',
                                         'object_id': book_id
                                         }),

                Message('LogsExchange', {'action': 'user return book',
                                         'object_type': 'user',
                                         'object_id': user_id
                                         })
            )
