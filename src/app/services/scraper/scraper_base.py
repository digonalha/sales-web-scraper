import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

logger = logging.getLogger(__name__)

class ScraperBase:
    def start_driver(self):
        service = Service("./geckodriver.exe")
        options = Options()

        options.add_argument("--headless")
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

        self.driver = webdriver.Firefox(service=service, options=options)

    def soup_page(self, url: str) -> BeautifulSoup:
        self.start_driver()

        logger.debug("requesting page: %s", url)

        self.driver.get(url)

        parsed_page = BeautifulSoup(self.driver.page_source, features="lxml")

        logger.debug("result: %s ", parsed_page.prettify())
        
        self.driver.close()

        return parsed_page
