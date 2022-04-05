from pydantic import BaseSettings
import os
from dotenv import load_dotenv


class Settings(BaseSettings):

    @property
    def DB_URL(self):
        PG_issue = 'barash'
        PG_PASSWORD = 'test_password'
        PG_DBNAME = 'evraz_project_2_issues_service'
        HOST = os.getenv('POSTGRES_DB_HOST', 'localhost')
        PG_PORT = '5432'

        return f"postgresql://{PG_issue}:{PG_PASSWORD}@{HOST}:{PG_PORT}/{PG_DBNAME}"
