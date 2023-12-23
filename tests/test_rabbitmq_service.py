from unittest.mock import patch, MagicMock
from src.app.services.messaging.rabbitmq_service import RabbitMQService

class TestRabbitMQService:
    @patch('pika.BlockingConnection')
    def test_publish_message(self, mock_pika):
        # Arrange
        mock_channel = MagicMock()
        mock_basic_publish = MagicMock()
        mock_channel.__enter__.return_value.basic_publish = mock_basic_publish
        mock_pika.return_value.channel.__enter__.return_value = mock_channel

        service = RabbitMQService()
        value = 'test_value'

        # Act
        service.publish_message(value)

        # Assert
        mock_pika.return_value.channel.assert_called_once()
        mock_channel.basic_publish.assert_called_once()