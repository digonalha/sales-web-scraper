from injector import Injector
from app.crosscutting.inject import RedisModule
from app.utils.stopwatch import Stopwatch
from app.services.scraper.boletando_service import BoletandoService
from app.services.scraper.gatry_service import GatryService
from configurations.logging import config_logging
import logging

logger = logging.getLogger(__name__)
stopwatch = Stopwatch()

config_logging()

def main():
    stopwatch.start()

    injector = Injector((RedisModule()))

    boletando_service = injector.get(BoletandoService)
    gatry_service = injector.get(GatryService)

    try:
        gatry_service.scrape_sales()
        boletando_service.scrape_sales()
                
    except Exception as ex:
        logger.critical("an error occurred. closing the application. error: %s", ex)
    finally:
        stopwatch.stop()


if __name__ == "__main__":
    main()

