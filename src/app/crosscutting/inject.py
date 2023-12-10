from app.services.cache.redis_service import RedisService
from app.services.messaging.rabbitmq_service import RabbitMQService
from injector import singleton, Module

class RedisModule(Module):
    def configure(self, binder):
        binder.bind(RedisService, to=RedisService(), scope=singleton)

class RabbitMQModule(Module):
    def configure(self, binder):
        binder.bind(RabbitMQService, to=RabbitMQService(), scope=singleton)