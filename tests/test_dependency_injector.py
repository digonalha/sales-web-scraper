from unittest.mock import MagicMock, Mock
from injector import Injector, singleton
from src.app.crosscutting.dependency_injector import DependencyInjector
from src.app.services.cache.redis_service import RedisService
from src.app.services.messaging.rabbitmq_service import RabbitMQService
from unittest.mock import MagicMock


def test_dependency_injector_setup():
    # Arrange
    injector = DependencyInjector.setup()

    # Assert
    assert isinstance(injector, Injector)

def test_dependency_injector_bindings():
    # Arrange
    injector = Injector()
    injector.binder.install(DependencyInjector())

    # Mock
    redis_service_mock = MagicMock(spec=RedisService)
    rabbitmq_service_mock = MagicMock(spec=RabbitMQService)
    injector.binder.bind(RedisService, to=redis_service_mock)
    injector.binder.bind(RabbitMQService, to=rabbitmq_service_mock)

    # Act
    redis_service = injector.get(RedisService)
    rabbitmq_service = injector.get(RabbitMQService)

    # Assert
    assert isinstance(redis_service, RedisService)
    assert isinstance(rabbitmq_service, RabbitMQService)
    assert redis_service is redis_service_mock
    assert rabbitmq_service is rabbitmq_service_mock
