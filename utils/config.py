class Config:
    BASE_URL = "https://nimypine.codeader.com"  # Cambia esto para producción
    API_PREFIX = "/api"

    @classmethod
    def get_api_url(cls, endpoint):
        return f"{cls.BASE_URL}{cls.API_PREFIX}{endpoint}"