import flet as ft
from services.auth_service import AuthService

class LoginScreen:
    def __init__(self, page, on_login_success):
        self.page = page
        self.on_login_success = on_login_success
        self.username_field = ft.TextField(label="Usuario o Email", width=300)
        self.password_field = ft.TextField(label="Contraseña", password=True, width=300)
        self.error_text = ft.Text()

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("Iniciar Sesión", size=24, weight=ft.FontWeight.BOLD),
                self.username_field,
                self.password_field,
                self.error_text,
                ft.ElevatedButton(
                    "Iniciar Sesión",
                    on_click=self._handle_login
                ),
                ft.TextButton(
                    "Crear cuenta nueva",
                    on_click=lambda e: self.page.go("/register")
                )
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center
        )

    def _handle_login(self, e):
        username = self.username_field.value
        password = self.password_field.value

        if not username or not password:
            self.error_text.value = "Por favor complete todos los campos"
            self.page.update()
            return

        user, token = AuthService.login(username, password)
        if user:
            self.on_login_success(user)
        else:
            self.error_text.value = "Credenciales inválidas o email no confirmado"
            self.page.update()