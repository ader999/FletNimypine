import flet as ft

class FacturarScreen:
    def __init__(self, page, user):
        self.page = page
        self.user = user

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Pantalla de Facturación", size=30),
                # Agrega aquí los controles para la facturación
            ]
        )