from classic.sql_storage import TransactionContext
from kombu import Connection
from sqlalchemy import create_engine
from threading import Thread
from adapters import database, message_bus, issues_api
from application import services


class Settings:
    db = database.Settings()
    # issue_api = issues_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine, expire_on_commit=False)
    issues_repo = database.repositories.IssueRepo(context=context)


class Application:
    issues = services.IssuesManager(
        issues_repo=DB.issues_repo,
    )
    # is_dev_mode = Settings.issue_api.IS_DEV_MODE
    # allow_origins = Settings.issue_api.ALLOW_ORIGINS


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    consumer = message_bus.create_consumer(connection, Application.issues)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


class Aspects:
    services.join_points.join(DB.context)
    issues_api.join_points.join(DB.context)


MessageBus.declare_scheme()
consumer = Thread(target=MessageBus.consumer.run, daemon=True)
consumer.start()


app = issues_api.create_app(
    # is_dev_mode=Application.is_dev_mode,
    # allow_origins=Application.allow_origins,
    issues_manager=Application.issues,
)

