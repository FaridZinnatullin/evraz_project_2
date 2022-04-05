from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Issue

# разобрать что это и зачем
join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    action: str
    object_type: str
    object_id: int


@component
class IssuesManager:
    issues_repo: interfaces.IssueRepo

    @join_point
    # @validate_with_dto
    def create(self, action, object_type, object_id):

        issue = Issue(
            action=action,
            object_type=object_type,
            object_id=object_id,
        )

        self.issues_repo.add_instance(issue)

    @join_point
    @validate_arguments
    def get_issue_by_id(self, issue_id: int):
        issue = self.issues_repo.get_by_id(issue_id)
        if not issue:
            raise errors.UncorrectedParams()
        return issue

    @join_point
    @validate_arguments
    def get_all_issues(self):
        return self.issues_repo.get_all()

    @join_point
    @validate_arguments
    def delete_issue(self, issue_id: int):
        issue = self.get_issue_by_id(issue_id)
        if issue:
            self.issues_repo.delete_by_id(issue_id)
        else:
            raise errors.UncorrectedParams()

    @join_point
    @validate_with_dto
    def update_issue(self, issue_data: IssueInfo):
        pass
