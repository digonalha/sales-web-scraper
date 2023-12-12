import pika
import logging
from os import getenv

logger = logging.getLogger(__name__)

class RabbitMQService:
    def __init__(self):
        # Suppress pika logging
        logging.getLogger("pika").setLevel(logging.WARNING)

        host = getenv("RABBITMQ_HOST", "localhost")
        port = getenv("RABBITMQ_PORT", 5672)
        user = getenv("RABBITMQ_USER", "guest")
        password = getenv("RABBITMQ_PASSWORD", "guest")

        credentials = pika.PlainCredentials(user, password)
        connection_params = pika.ConnectionParameters(host=host, port=port, credentials=credentials)

        self.connection = pika.BlockingConnection(connection_params)

    def publish_message(self, message):
        with self.connection.channel() as channel:
            channel.basic_publish("", "sales", message)
            logging.info("message published successfully with content %s", message)
