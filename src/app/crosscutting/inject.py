from app.services.cache.redis_service import RedisService
from app.services.scraper.boletando_service import BoletandoService
from injector import singleton, Module

class RedisModule(Module):
    def configure(self, binder):
        binder.bind(RedisService, to=RedisService(), scope=singleton)