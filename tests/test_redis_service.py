from unittest.mock import patch
from src.app.services.cache.redis_service import RedisService

class TestRedisService:
    @patch('redis.Redis')
    def test_set_cache(self, mock_redis):
        # Arrange
        mock_client = mock_redis.return_value.__enter__.return_value
        service = RedisService()
        key = 'test_key'
        value = 'test_value'

        # Act
        service.set_cache(key, value)

        # Assert
        mock_client.set.assert_called_once_with(key, value)
        mock_client.expire.assert_called_once_with(key, 1728 * 100)
    
    @patch('redis.Redis')
    def test_get_cache(self, mock_redis):
        # Arrange
        mock_client = mock_redis.return_value.__enter__.return_value
        mock_client.get.return_value = 'cached value'
        service = RedisService()

        # Act
        result = service.get_cache('key')

        # Assert
        mock_client.get.assert_called_once_with('key')
        assert result == 'cached value'