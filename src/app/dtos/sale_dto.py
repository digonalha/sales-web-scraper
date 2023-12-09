from dataclasses import dataclass

@dataclass
class SaleDto:
    url: str
    product_name: str
    product_price: float
    description: str = None
    status: int = 0