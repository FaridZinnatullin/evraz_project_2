import pytest
from unittest.mock import Mock

from classic.messaging import Publisher

from components.books_service.application import interfaces, dataclasses


@pytest.fixture(scope='function')
def book():
    return dataclasses.Book(
        id=1,
        name='book1',
        available=False,
    )


@pytest.fixture(scope='function')
def book_taken():
    return dataclasses.Book(
        id=1,
        name='book1',
        author='author1',
        available=True,
    )


@pytest.fixture(scope='function')
def book2():
    return dataclasses.Book(
        id=2,
        name='book2',
        author='author2',
        available=False,
    )


@pytest.fixture(scope='function')
def book3():
    return dataclasses.Book(
        id=3,
        name='book3',
        author='author3',
        available=False,

    )

@pytest.fixture(scope='function')
def book5():
    return dataclasses.Book(
        id=5,
        name='book5',
        author='author5',
        available=False,
    )



@pytest.fixture(scope='function')
def books_repo(book, book2, book3, book5, book_taken):
    books_repo = Mock(interfaces.BookRepo)
    books_repo.get_by_id = Mock(return_value=book5)
    books_repo.get_all = Mock(return_value=[book2, book3])
    books_repo.delete_by_id = Mock(return_value=book)
    books_repo.add_instance = Mock(return_value=book)
    books_repo.add_instance = Mock(return_value=book_taken)
    return books_repo


@pytest.fixture(scope='function')
def publisher():
    publisher = Mock(Publisher)
    return publisher
