import logging
from os import getenv
import pika

logger = logging.getLogger(__name__)

class RabbitMQService:
    def __init__(self):
        self.host = getenv("RABBITMQ_HOST", "localhost")
        self.port = getenv("RABBITMQ_PORT", "5672")
        self.user = getenv("RABBITMQ_USER", "guest")
        self.password = getenv("RABBITMQ_PASSWORD", "guest")

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, 
                                                                            port=self.port, 
                                                                            credentials=pika.PlainCredentials(self.user, self.password)))
        self.channel = self.connection.channel()

    def publish_message(self, message):
        self.channel.basic_publish("", "sales", message)
        logging.info("message published successfully with content %s", message)
