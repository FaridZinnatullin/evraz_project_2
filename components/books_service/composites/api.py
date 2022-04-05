from classic.sql_storage import TransactionContext
from sqlalchemy import create_engine

from adapters import database, books_api, message_bus
from application import services

from kombu import Connection
from classic.messaging_kombu import KombuPublisher


class Settings:
    db = database.Settings()
    books_api = books_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)
    # database.metadata.drop_all(engine)
    database.metadata.create_all(engine)
    context = TransactionContext(bind=engine)

    books_repo = database.repositories.BookRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,

    )


class Application:
    books_manager = services.BooksManager(
        books_repo=DB.books_repo,
        publisher=MessageBus.publisher,
    )
    is_dev_mode = Settings.books_api.IS_DEV_MODE
    allow_origins = Settings.books_api.ALLOW_ORIGINS


class Aspects:
    services.join_points.join(DB.context)
    books_api.join_points.join(MessageBus.publisher, DB.context)


app = books_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    allow_origins=Application.allow_origins,
    books_manager=Application.books_manager,
)

# if __name__ == '__main__':
#     from wsgiref import simple_server
#
#     with simple_server.make_server('', 8000, app=app) as server:
#         server.serve_forever()
