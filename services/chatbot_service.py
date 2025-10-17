from api_client import api_client
from models.user import User

class ChatbotService:
    @staticmethod
    def send_message(user: User, message: str, conversation_id: int = None):
        """
        Envía un mensaje al chatbot y devuelve la respuesta.
        """
        endpoint = "/asistente/chatbot/"
        data = {
            "message": message,
        }
        if conversation_id:
            data["conversacion_id"] = conversation_id
        # El token ya está configurado en la instancia global de api_client durante el login
        return api_client.post(endpoint, data)
