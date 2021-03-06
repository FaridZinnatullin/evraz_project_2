from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from application import services

from .scheme import broker_scheme


def create_consumer(connection: Connection, service: services.IssuesManager) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        service.create,
        'LogsQueue',
    )
    return consumer
