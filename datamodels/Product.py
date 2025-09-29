from dataclasses import dataclass


@dataclass
class Product:
    title: str
    price: float
    description: str
    image: str
    category: str
