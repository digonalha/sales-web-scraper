import logging
import httpx
from os import getenv

from app.dtos.sale_dto import Sale

logger = logging.getLogger(__name__)

class SaleClient:
    def __init__(self):
        base_url = getenv("SALE_SERVICE_URL")

        if (base_url is None):
            raise Exception("SALE_SERVICE_URL environment variable is not set")
        
        self.endpoint = f"{base_url}/sales"


    def post(self, sale: Sale):
        sale_json = sale.__dict__

        logging.info("send post with sale dto %s to %s", sale_json, self.endpoint)

        response = httpx.post(self.endpoint, json=sale_json)
        response.raise_for_status()
        return response.json()
