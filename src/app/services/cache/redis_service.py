from os import getenv
import redis

class RedisService:
    def __init__(self):
        host = getenv("REDIS_HOST", "localhost")
        port = getenv("REDIS_PORT", "6379")
        database = getenv("REDIS_DATABASE", "0")

        self.pool = redis.ConnectionPool(host=host, port=port, db=database)
        self.redis_client = redis.Redis(connection_pool=self.pool)

    def set_cache(self, key, value):
        self.redis_client.set(key, value)

    def get_cache(self, key):
        return self.redis_client.get(key)
