from abc import ABC, abstractmethod
from typing import List, Optional

from .dataclasses import Issue


class IssueRepo(ABC):

    @abstractmethod
    def get_by_id(self, issue_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add_instance(self, issue_data):
        pass

    @abstractmethod
    def delete_by_id(self, issue_id: int):
        pass

    @abstractmethod
    def update_by_id(self, issue: Issue):
        pass

