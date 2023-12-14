from src.app.services.cache.redis_service import RedisService
from src.app.services.messaging.rabbitmq_service import RabbitMQService
from injector import Injector, Module, singleton


class DependencyInjector(Module):
    @staticmethod
    def setup():
        injector = Injector()
        injector.binder.install(DependencyInjector())
        return injector
    
    def configure(self, binder):
        binder.bind(RedisService, to=RedisService(), scope=singleton)
        binder.bind(RabbitMQService, to=RabbitMQService(), scope=singleton)


# class RedisModule(Module):
#     def configure(self, binder):
#         binder.bind(RedisService, to=RedisService(), scope=singleton)

# class RabbitMQModule(Module):
#     def configure(self, binder):
#         binder.bind(RabbitMQService, to=RabbitMQService(), scope=singleton)