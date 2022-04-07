import pytest
from attr import asdict

from application import services


@pytest.fixture(scope='function')
def service_issue(issues_repo):
    return services.IssuesManager(issues_repo=issues_repo)


data_issue = {
    'action': 'create',
    'object_type': 'user',
    'object_id': 1
}

data_issue1 = {
    'id': 1,
    'action': 'create',
    'object_type': 'user',
    'object_id': 1
}

data_issue2 = {
    'id': 2,
    'action': 'create',
    'object_type': 'book',
    'object_id': 1
}

data_issue3 = {
    'id': 3,
    'action': 'get book',
    'object_type': 'book',
    'object_id': 1
}

data_issue4 = {
    'id': 4,
    'action': 'user return book',
    'object_type': 'user',
    'object_id': 1
}


def test_add_issue(service_issue):
    service_issue.create(**data_issue)
    service_issue.issues_repo.add_instance.assert_called_once()


def test_get_issue(service_issue):
    issue = service_issue.get_issue_by_id(issue_id=data_issue1['id'])
    assert asdict(issue) == data_issue1


def test_get_all_issue(service_issue):
    issues = service_issue.get_all_issues()
    issues = [asdict(issue) for issue in issues]
    assert issues == [data_issue1, data_issue2, data_issue3, data_issue4]


def test_delete_issue(service_issue):
    service_issue.delete_issue(issue_id=data_issue1['id'])
    service_issue.issues_repo.delete_by_id.assert_called_once()

