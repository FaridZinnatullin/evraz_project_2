from pydantic import BaseSettings
import os
from dotenv import load_dotenv


class Settings(BaseSettings):

    @property
    def DB_URL(self):
        # dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        # if os.path.exists(dotenv_path):
        #     load_dotenv(dotenv_path)
        # PG_book = os.getenv('POSTGRES_book')
        # PG_PASSWORD = os.getenv('POSTGRES_PASSWORD')
        # PG_DBNAME = os.getenv('POSTGRES_NAME')
        # PG_HOST= os.getenv('POSTGRES_HOST')
        # PG_PORT = os.getenv('POSTGRES_PORT')

        PG_book = 'barash'
        PG_PASSWORD = 'test_password'
        PG_DBNAME = 'evraz_project_2_books_service'
        HOST = os.getenv('POSTGRES_DB_HOST', 'localhost')
        PG_PORT = '5432'

        return f"postgresql://{PG_book}:{PG_PASSWORD}@{HOST}:{PG_PORT}/{PG_DBNAME}"
