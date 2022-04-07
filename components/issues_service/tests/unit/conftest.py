import pytest
from unittest.mock import Mock

from components.issues_service.application import interfaces, dataclasses


@pytest.fixture(scope='function')
def issue():
    return dataclasses.Issue(
        id=1,
        action='create',
        object_type='user',
        object_id=1,
    )


@pytest.fixture(scope='function')
def issue2():
    return dataclasses.Issue(
        id=2,
        action='create',
        object_type='book',
        object_id=1,
    )


@pytest.fixture(scope='function')
def issue3():
    return dataclasses.Issue(
        id=3,
        action='get book',
        object_type='book',
        object_id=1,
    )

@pytest.fixture(scope='function')
def issue4():
    return dataclasses.Issue(
        id=4,
        action='user return book',
        object_type='user',
        object_id=1,
    )


@pytest.fixture(scope='function')
def issues_repo(issue, issue2, issue3, issue4):
    issues_repo = Mock(interfaces.IssueRepo)
    issues_repo.get_by_id = Mock(return_value=issue)
    issues_repo.get_all = Mock(return_value=[issue, issue2, issue3, issue4])
    return issues_repo
