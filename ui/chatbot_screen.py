import flet as ft
from services.chatbot_service import ChatbotService

class ChatMessage(ft.Row):
    def __init__(self, message: str, is_user: bool):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text("U" if is_user else "A"),
                color=ft.Colors.WHITE if is_user else ft.Colors.BLACK,
                bgcolor=ft.Colors.BLUE_GREY_400 if is_user else ft.Colors.GREEN_200,
            ),
            ft.Column(
                [
                    ft.Text(
                        "Tú" if is_user else "Asistente",
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(message, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
        ]

class ChatbotScreen:
    def __init__(self, page, user):
        self.page = page
        self.user = user
        self.conversation_id = None
        self.chat_history = ft.ListView(expand=True, spacing=10, auto_scroll=True)
        self.new_message = ft.TextField(
            hint_text="Escribe un mensaje...",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
        )
        self.send_button = ft.IconButton(
            icon=ft.Icons.SEND_ROUNDED,
            tooltip="Enviar mensaje",
            on_click=self._send_message_click,
        )

    def build(self):
        """Construye la vista del chatbot."""
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.chat_history,
                    border=ft.border.all(1, ft.Colors.OUTLINE),
                    border_radius=ft.border_radius.all(5),
                    padding=10,
                    expand=True,
                ),
                ft.Row(
                    controls=[
                        self.new_message,
                        self.send_button,
                    ],
                ),
            ],
            expand=True,
        )

    def _send_message_click(self, e):
        """Maneja el evento de clic en el botón de enviar."""
        message_text = self.new_message.value
        if not message_text:
            return

        # Muestra el mensaje del usuario en el chat
        self.chat_history.controls.append(ChatMessage(message_text, is_user=True))
        self.new_message.value = ""
        self.page.update()

        # Muestra un indicador de carga (opcional)
        loading_message = ChatMessage("Escribiendo...", is_user=False)
        self.chat_history.controls.append(loading_message)
        self.page.update()

        # Llama a la API
        try:
            response = ChatbotService.send_message(self.user, message_text, self.conversation_id)
            
            # Elimina el indicador de carga
            self.chat_history.controls.pop()

            if response and 'mensajes' in response:
                self.conversation_id = response.get('id')
                
                # Añade solo el último mensaje del asistente
                last_assistant_message = next((msg for msg in reversed(response['mensajes']) if not msg['es_usuario']), None)
                if last_assistant_message:
                    self.chat_history.controls.append(ChatMessage(last_assistant_message['contenido'], is_user=False))

            else:
                if response:
                    error_content = f"Error: {response.get('detail', 'No se pudo obtener respuesta.')}"
                else:
                    error_content = "Error de conexión: No se pudo contactar al servidor."
                self.chat_history.controls.append(ChatMessage(error_content, is_user=False))

        except Exception as ex:
            self.chat_history.controls.pop() # Elimina el indicador de carga
            self.chat_history.controls.append(ChatMessage(f"Error de conexión: {ex}", is_user=False))
        
        self.page.update()