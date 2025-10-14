import requests
from utils.config import Config

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        self.token = token
        self.session.headers.update({
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        })

    def clear_token(self):
        self.token = None
        self.session.headers.pop('Authorization', None)

    def _make_request(self, method, endpoint, data=None, **kwargs):
        url = Config.get_api_url(endpoint)
        try:
            if data:
                kwargs['json'] = data
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None

    def post(self, endpoint, data=None, **kwargs):
        return self._make_request('POST', endpoint, data, **kwargs)

    def get(self, endpoint, **kwargs):
        return self._make_request('GET', endpoint, **kwargs)

# Instancia global del cliente
api_client = APIClient()