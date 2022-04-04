from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from adapters import database, users_api
from application import services


class Settings:
    db = database.Settings()
    users_api = users_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)
    # database.metadata.drop_all(engine)
    database.metadata.create_all(engine)
    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)


class Application:
    users_manager = services.UsersManager(
        users_repo=DB.users_repo,
    )
    is_dev_mode = Settings.users_api.IS_DEV_MODE
    allow_origins = Settings.users_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    users_api.join_points.join(DB.context)


app = users_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    users_manager=Application.users_manager,
)

if __name__ == '__main__':
    from wsgiref import simple_server

    with simple_server.make_server('', 8000, app=app) as server:
        server.serve_forever()
