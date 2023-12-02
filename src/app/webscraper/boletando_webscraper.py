from app.utils.string_helpers import str_to_float
from app.dtos.sale_dto import Sale
from app.webscraper.webscraper_base import WebscraperBase
import logging

logger = logging.getLogger(__name__)

class BoletandoWebscraper(WebscraperBase):
    def __init__(self):
        self.url = "https://boletando.com/"

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

            sale = Sale(url=url, product_name=product_name, product_price=product_price, description=description)
        
        logging.info("added a total of %s sales from %s", total, self.url)