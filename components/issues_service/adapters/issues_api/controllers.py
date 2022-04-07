from classic.components import component
from classic.http_auth import (
    authenticator_needed,
    authenticate
)

from application import services
from .join_points import join_point


@authenticator_needed
@component
class Issues:
    issues_manager: services.IssuesManager

    @join_point
    @authenticate
    def on_get_issue_info(self, request, response):
        issue = self.issues_manager.get_issue_by_id(**request.params)
        result = {
            'issue_id': issue.id,
            'issue_action': issue.action,
            'issue_object_type': issue.object_type,
            'issue_object_id': issue.object_id
        }
        response.media = result

    @join_point
    @authenticate
    def on_get_issue_all(self, request, response):
        issues = self.issues_manager.get_all_issues()

        result = [{
            'issue_id': issue.id,
            'issue_action': issue.action,
            'issue_object_type': issue.object_type,
            'issue_object_id': issue.object_id
        } for issue in issues]

        response.media = result

    @join_point
    @authenticate
    def on_post_create(self, request, response):
        self.issues_manager.create(**request.media)

    @join_point
    @authenticate
    def on_post_delete(self, request, response):
        self.issues_manager.delete_issue(**request.media)

