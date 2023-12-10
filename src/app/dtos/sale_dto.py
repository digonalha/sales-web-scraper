from dataclasses import dataclass, asdict

@dataclass
class SaleDto:
    url: str
    product_name: str
    product_price: float
    description: str = None

    def as_dict(self):
        return {k: str(v) for k, v in asdict(self).items()}