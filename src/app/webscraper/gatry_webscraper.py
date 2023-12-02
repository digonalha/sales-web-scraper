from app.http_clients.sale_client import SaleClient
from app.utils.string_helpers import str_to_float, sanitize_text
from app.webscraper.webscraper_base import WebscraperBase
from app.dtos.sale_dto import Sale
import logging

logger = logging.getLogger(__name__)

class GatryWebscraper(WebscraperBase):
    def __init__(self):
        self.url = "https://gatry.com"

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

            sale = Sale(url=url, product_name=product_name, product_price=product_price, description=description)
        
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