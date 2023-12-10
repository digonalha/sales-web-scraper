import json
from injector import inject
from app.services.messaging.rabbitmq_service import RabbitMQService
from app.utils.string_helpers import str_to_float
from app.dtos.sale_dto import SaleDto
from app.services.scraper.scraper_base import ScraperBase
from app.services.cache.redis_service import RedisService
import logging

logger = logging.getLogger(__name__)

class BoletandoService(ScraperBase):
    @inject
    def __init__(self, redis_service: RedisService, rabbitmq_service: RabbitMQService):
        self.url = "https://boletando.com/"
        self.redis_service = redis_service
        self.rabbitmq_service = rabbitmq_service

    def scrape_sales(self):
        logger.info("web scraping page: %s", self.url)

        total = 0
        elements = self.soup_page(self.url).findAll("article", class_="col_item")

        for tag in elements:
            url = tag.find("a", {"class": "btn_offer_block"}).get("href")
            product_name = tag.find("h3").text
            product_price = tag.find("span", {"class": "price_count"}).text
            product_price = str_to_float(product_price)
            description = tag.find("div", {"class": "rh_custom_notice"}).text

            sale = SaleDto(url=url, product_name=product_name, product_price=product_price, description=description)

            if not self.redis_service.get_cache(sale.url):
                sale_json = json.dumps(sale.as_dict(), ensure_ascii=False)
                self.rabbitmq_service.publish_message(sale_json)
                self.redis_service.set_cache(sale.url, sale_json)
                total += 1
        
        logging.info("added a total of %s sales from %s", total, self.url)