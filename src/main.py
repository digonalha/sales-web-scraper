from app.utils.stopwatch import Stopwatch
from app.webscraper.boletando_webscraper import BoletandoWebscraper
from app.webscraper.gatry_webscraper import GatryWebscraper
from configurations.logging import config_logging
import logging

logger = logging.getLogger(__name__)
stopwatch = Stopwatch()

config_logging()

def main():
    stopwatch.start()

    gatry = GatryWebscraper()
    boletando = BoletandoWebscraper()

    try:
        # ping_database()

        gatry.scrape_sales()
        boletando.scrape_sales()
                
    except Exception as ex:
        logger.critical("an error occurred. closing the application. error: %s", ex)
    finally:
        stopwatch.stop()


if __name__ == "__main__":
    main()

