from injector import inject
from app.utils.string_helpers import str_to_float, sanitize_text
from app.services.scraper.scraper_base import ScraperBase
from app.services.cache.redis_service import RedisService
from app.dtos.sale_dto import SaleDto
import logging

logger = logging.getLogger(__name__)

class GatryService(ScraperBase):
    @inject
    def __init__(self, redis_service: RedisService):
        self.url = "https://gatry.com"
        self.redis_service = redis_service

    def scrape_sales(self):
        logger.info("web scraping page: %s", self.url)

        total = 0
        elements = self.soup_page(self.url).findAll("article")

        for tag in elements:
            header = tag.find("h3")
            
            url = header.find("a").get("href")
            product_name = header.text
            product_price = tag.find("p", {"class": "price"}).text
            product_price = str_to_float(product_price)

            description = ""#self.scrape_description_if_exists(tag)

            sale = SaleDto(url=url, product_name=product_name, product_price=product_price, description=description)

            self.redis_service.set_cache(sale.url, sale.url)
        
        logging.info("added a total of %s sales from %s", total, self.url)



    def scrape_description_if_exists(self, tag: object) -> str:
            comments_elements = tag.find("p", {"class": "comment"})

            if (comments_elements):
                url = tag.find("div", {"class": "option-comment"}).find("a").get("href")
                comment_crawler = self.soup_page(self.url + url)
                comments = comment_crawler.findAll("div", {"class": "comment-content"})

                for comment in comments:
                    matches = ["CUPOM", "VISTA", "PARCELADO", "JUROS", "PIX"]
                    scraped_description = comment.text if any(x in comment.text.upper() for x in matches) else None

                    if scraped_description:
                         return sanitize_text(scraped_description)