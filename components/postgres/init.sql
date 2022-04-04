CREATE user barash WITH PASSWORD 'test_password';

CREATE DATABASE evraz_project_2_users_service;
CREATE DATABASE evraz_project_2_books_service;
CREATE DATABASE evraz_project_2_issues_service;

GRANT ALL PRIVILEGES ON DATABASE evraz_project_2_users_service TO barash;
GRANT ALL PRIVILEGES ON DATABASE evraz_project_2_books_service TO barash;
GRANT ALL PRIVILEGES ON DATABASE evraz_project_2_issues_service TO barash;