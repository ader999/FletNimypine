from api_client import api_client
from models.product import Product

class ProductService:
    @staticmethod
    def get_products():
        response = api_client.get('/produccion/productos/')
        if response:
            return [Product.from_dict(item) for item in response]
        return []