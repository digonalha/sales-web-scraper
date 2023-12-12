import pika
import logging
from os import getenv

logger = logging.getLogger(__name__)

class RabbitMQService:
    def __init__(self):
        host = getenv("RABBITMQ_HOST", "localhost")
        port = getenv("RABBITMQ_PORT", "5672")
        user = getenv("RABBITMQ_USER", "guest")
        password = getenv("RABBITMQ_PASSWORD", "guest")

        credentials = pika.PlainCredentials(user, password)

        self.connection_params = pika.ConnectionParameters(host=host, port=port, credentials=credentials)

    def publish_message(self, message):
        with pika.BlockingConnection(self.connection_params) as connection:
            channel = connection.channel()
            channel.basic_publish("", "sales", message)
            logging.info("message published successfully with content %s", message)
