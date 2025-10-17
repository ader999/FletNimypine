from api_client import api_client
from models.user import User

class AuthService:
    @staticmethod
    def register(username, email, first_name, last_name, password, password2, rol='LECTURA', avatar=None):
        data = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
            'password2': password2,
            'rol': rol
        }
        if avatar:
            data['avatar'] = avatar

        response = api_client.post('/cuentas/register/', data)
        return response

    @staticmethod
    def login(username_or_email, password):
        data = {
            'username': username_or_email,
            'password': password
        }
        response = api_client.post('/asistente/api-token-auth/', data)
        if response and 'token' in response:
            token = response['token']
            api_client.set_token(token)
            # El endpoint de token no devuelve los datos del usuario,
            # así que creamos un objeto User con la información disponible.
            user = User(username=username_or_email, email=username_or_email, token=token)
            return user
        return None

    @staticmethod
    def logout():
        response = api_client.post('/cuentas/logout/')
        if response:
            api_client.clear_token()
            return True
        return False