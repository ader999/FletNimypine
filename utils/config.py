class Config:
    BASE_URL = "http://127.0.0.1:8000"  # Cambia esto para producción
    API_PREFIX = "/api"

    @classmethod
    def get_api_url(cls, endpoint):
        return f"{cls.BASE_URL}{cls.API_PREFIX}{endpoint}"