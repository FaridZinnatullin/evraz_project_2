import pytest
from attr import asdict

from components.users_service.application import services, errors


@pytest.fixture(scope='function')
def service_user(users_repo, publisher):
    return services.UsersManager(users_repo=users_repo, publisher=publisher)


data_user = {
    'id': 1,
    'name': 'user1',
    'login': None,
    'password': None
}

data_user_registration = {
    'name': 'user1',
    'login': 'login1',
    'password': 'password1',
}

data_user2 = {
    'id': 2,
    'name': 'user2',
    'login': None,
    'password': None
}


def test_add_user(service_user):
    with pytest.raises(errors.UserAlreadyExist):
        service_user.registration(**data_user_registration)


def test_get_all_user(service_user):
    users = service_user.get_all_users()
    users = [asdict(user) for user in users]
    assert users == [data_user, data_user2]


def test_delete_user(service_user):
    service_user.delete_user(user_id=data_user['id'])
    service_user.users_repo.delete_by_id.assert_called_once()

