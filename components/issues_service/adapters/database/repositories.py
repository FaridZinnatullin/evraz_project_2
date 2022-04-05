from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy.sql import select, and_

from application import interfaces
from application.dataclasses import Issue


@component
class IssueRepo(BaseRepository, interfaces.IssueRepo):

    def get_by_id(self, issue_id: int):
        query = select(Issue).where(Issue.id == issue_id)
        issue = self.session.execute(query).scalars().one_or_none()
        return issue

    def get_all(self):
        query = select(Issue)
        issues = self.session.execute(query).scalars().all()
        return issues

    def add_instance(self, issue: Issue):
        self.session.add(issue)
        self.session.flush()

    def delete_by_id(self, issue_id: int):
        issue = self.get_by_id(issue_id)
        self.session.delete(issue)

    def update_by_id(self, issue: Issue):
        pass

