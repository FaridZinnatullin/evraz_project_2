import pytest
from attr import asdict
from unittest.mock import Mock

from components.books_service.application import services, errors


@pytest.fixture(scope='function')
def service_book(books_repo, publisher):
    return services.BooksManager(books_repo=books_repo, publisher=publisher)


data_book = {
    # 'id': 1,
    'name': 'book1',
    'author': 'author1',
    'available': False,
    # 'user_taken': 1,
}

data_book_with_id = {
    'id': 1,
    'name': 'book1',
    'author': 'author1',
    'available': True,
    # 'user_taken': 1,
}


data_book2 = {
    'id': 2,
    'name': 'book2',
    'author': 'author2',
    'available': False,
    # 'user_taken': None,
}

data_book3 = {
    'id': 3,
    'name': 'book3',
    'author': 'author3',
    'available': False,
    # 'user_taken': None,
}

data_book5 = {
    'id': 5,
    'name': 'name5',
    'author': 'author5',
    'available': True
}

def test_add_book(service_book):
    with pytest.raises(errors.BookAlreadyExist):
        service_book.create(**data_book)


def test_get_book(service_book):
    book = service_book.get_book_by_id(book_id=5)
    assert asdict(book).get('id') == 5


def test_get_all_book(service_book):
    books = service_book.get_all_books()
    books = [asdict(book) for book in books]
    assert books == [data_book2, data_book3]


def test_return_book(service_book):
    service_book.return_book(book_id=1, user_id=1)


def test_delete_book(service_book):
    service_book.delete_book(book_id=data_book_with_id['id'])
    service_book.books_repo.delete_by_id.assert_called_once()

