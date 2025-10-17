import requests
from models.product import Product
from services.auth_service import AuthService
from utils.config import Config

class SaleService:
    @staticmethod
    def get_products():
        """Obtiene todos los productos de la API."""
        token = AuthService.get_token()
        if not token:
            return []

        headers = {'Authorization': f'Token {token}'}
        api_url = Config.get_api_url("/produccion/productos/")
        
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            products_data = response.json()
            return [Product.from_dict(p) for p in products_data]
        except requests.RequestException as e:
            print(f"Error al obtener productos: {e}")
            return []

    @staticmethod
    def register_sale(items):
        """Registra una nueva venta en la API."""
        token = AuthService.get_token()
        if not token:
            return False, "No se encontró el token de autenticación."

        headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        }
        api_url = Config.get_api_url("/produccion/registrar-venta/")
        
        # Prepara los datos para la API
        sale_data = {
            "items": [
                {
                    "producto": item['product_id'],
                    "cantidad": item['quantity'],
                    "precio_unitario": str(item['unit_price'])
                } for item in items
            ]
        }

        try:
            response = requests.post(api_url, json=sale_data, headers=headers)
            response.raise_for_status()
            return True, "Venta registrada exitosamente."
        except requests.RequestException as e:
            error_message = f"Error al registrar la venta: {e}"
            if e.response:
                error_message += f" - {e.response.text}"
            print(error_message)
            return False, error_message
