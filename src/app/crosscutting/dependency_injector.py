from app.services.cache.redis_service import RedisService
from app.services.messaging.rabbitmq_service import RabbitMQService
from injector import singleton, Module
from injector import Injector

class DependencyInjector:
    @staticmethod
    def setup():
        injector = Injector()
        injector.binder.install(RedisModule())
        injector.binder.install(RabbitMQModule())
        return injector


class RedisModule(Module):
    def configure(self, binder):
        binder.bind(RedisService, to=RedisService(), scope=singleton)

class RabbitMQModule(Module):
    def configure(self, binder):
        binder.bind(RabbitMQService, to=RabbitMQService(), scope=singleton)