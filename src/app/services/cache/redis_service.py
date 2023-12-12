import redis
from os import getenv

class RedisService:
    def __init__(self):
        self.host = getenv("REDIS_HOST", "localhost")
        self.port = getenv("REDIS_PORT", "6379")
        self.database = getenv("REDIS_DATABASE", "0")

    def set_cache(self, key, value):
        with redis.Redis(host=self.host, port=self.port, db=self.database) as redis_client:
            redis_client.set(key, value)
            redis_client.expire(key, 1728 * 100)

    def get_cache(self, key):
        with redis.Redis(host=self.host, port=self.port, db=self.database) as redis_client:
            return redis_client.get(key)
