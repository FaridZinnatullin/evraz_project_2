from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from application import services

from .scheme import broker_scheme


# def test_function(test_data):
#     print(test_data)

# def create_consumer(connection: Connection, orders: services.Orders) -> KombuConsumer:
def create_consumer(connection: Connection, issues: services.IssuesManager) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    # consumer.register_function(
    #     orders.send_message_to_manager,
    #     'PrintOrderPlaced',
    # )

    consumer.register_function(
        issues.create,
        'LogsQueue',
    )

    return consumer
