from unittest.mock import MagicMock, Mock
from injector import Injector, singleton
from src.app.crosscutting.dependency_injector import DependencyInjector
from src.app.services.cache.redis_service import RedisService
from src.app.services.messaging.rabbitmq_service import RabbitMQService
from unittest.mock import MagicMock
from unittest.mock import MagicMock
import pika


def test_dependency_injector_bindings():
    # Arrange
    injector = Injector()
    injector.binder.install(DependencyInjector())

    # Mock
    redis_service_mock = MagicMock(spec=RedisService)
    rabbitmq_service_mock = MagicMock(spec=RabbitMQService)
    blocking_connection_mock = MagicMock(spec=pika.BlockingConnection)
    injector.binder.bind(RedisService, to=redis_service_mock)
    injector.binder.bind(RabbitMQService, to=rabbitmq_service_mock)
    injector.binder.bind(pika.BlockingConnection, to=blocking_connection_mock)

    # Act
    redis_service = injector.get(RedisService)
    rabbitmq_service = injector.get(RabbitMQService)
    blocking_connection = injector.get(pika.BlockingConnection)

    # Assert
    assert isinstance(redis_service, RedisService)
    assert isinstance(rabbitmq_service, RabbitMQService)
    assert isinstance(blocking_connection, pika.BlockingConnection)
    assert redis_service is redis_service_mock
    assert rabbitmq_service is rabbitmq_service_mock
    assert blocking_connection is blocking_connection_mock
