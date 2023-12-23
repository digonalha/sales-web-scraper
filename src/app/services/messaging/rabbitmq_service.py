import pika
import logging
from os import getenv

logger = logging.getLogger(__name__)

class RabbitMQService:
    def __init__(self):
        host = getenv("RABBITMQ_HOST", "localhost")
        port = getenv("RABBITMQ_PORT", 5672)
        user = getenv("RABBITMQ_USER", "guest")
        password = getenv("RABBITMQ_PASSWORD", "guest")

        self.rabbitmq_connection = self.__create_connection(host, port, user, password)

    def __create_connection(self, host, port, user, password):
        credentials = pika.PlainCredentials(user, password)
        connection_params = pika.ConnectionParameters(host=host, port=port, credentials=credentials)

        return pika.BlockingConnection(connection_params)

    def publish_message(self, message):
        with self.rabbitmq_connection.channel() as channel:
            channel.basic_publish("", "sales", message)
            logging.info("message published successfully with content %s", message)
