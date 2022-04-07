import pytest
from unittest.mock import Mock

from classic.messaging import Publisher

from application import interfaces, dataclasses


@pytest.fixture(scope='function')
def users():
    return dataclasses.User(
        id=1,
        name='user1',
        login=None,
        password=None
    )


@pytest.fixture(scope='function')
def users2():
    return dataclasses.User(
        id=2,
        name='user2',
        login=None,
        password=None
    )


@pytest.fixture(scope='function')
def users_repo(users, users2):
    users_repo = Mock(interfaces.UserRepo)
    users_repo.get_user = Mock(return_value=users)
    users_repo.get_all = Mock(return_value=[users, users2])
    return users_repo


@pytest.fixture(scope='function')
def publisher():
    publisher = Mock(Publisher)
    return publisher
