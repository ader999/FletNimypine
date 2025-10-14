import flet as ft
from services.auth_service import AuthService

class RegisterScreen:
    def __init__(self, page):
        self.page = page
        self.username_field = ft.TextField(label="Usuario", width=300)
        self.email_field = ft.TextField(label="Email", width=300)
        self.first_name_field = ft.TextField(label="Nombre", width=300)
        self.last_name_field = ft.TextField(label="Apellido", width=300)
        self.password_field = ft.TextField(label="Contraseña", password=True, width=300)
        self.password2_field = ft.TextField(label="Confirmar Contraseña", password=True, width=300)
        self.error_text = ft.Text()
        self.success_text = ft.Text()

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("Crear Cuenta", size=24, weight=ft.FontWeight.BOLD),
                self.username_field,
                self.email_field,
                self.first_name_field,
                self.last_name_field,
                self.password_field,
                self.password2_field,
                self.error_text,
                self.success_text,
                ft.ElevatedButton(
                    "Crear Cuenta",
                    on_click=self._handle_register
                ),
                ft.TextButton(
                    "Ya tengo cuenta",
                    on_click=lambda e: self.page.go("/login")
                )
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center
        )

    def _handle_register(self, e):
        data = {
            'username': self.username_field.value,
            'email': self.email_field.value,
            'first_name': self.first_name_field.value,
            'last_name': self.last_name_field.value,
            'password': self.password_field.value,
            'password2': self.password2_field.value
        }

        if not all(data.values()):
            self.error_text.value = "Por favor complete todos los campos"
            self.page.update()
            return

        if data['password'] != data['password2']:
            self.error_text.value = "Las contraseñas no coinciden"
            self.page.update()
            return

        response = AuthService.register(**data)
        if response and 'message' in response:
            self.success_text.value = "Cuenta creada exitosamente. Revisa tu email para confirmar."
            self.error_text.value = ""
            # Limpiar campos
            for field in [self.username_field, self.email_field, self.first_name_field,
                          self.last_name_field, self.password_field, self.password2_field]:
                field.value = ""
        else:
            self.error_text.value = "Error al crear la cuenta"
            self.success_text.value = ""

        self.page.update()