import flet as ft
from services.auth_service import AuthService
from ui.products_screen import ProductsScreen
from ui.chatbot_screen import ChatbotScreen
from ui.facturar_screen import FacturarScreen


class MainLayout:
    def __init__(self, page, user, on_product_click):
        self.page = page
        self.user = user
        self.products_screen = ProductsScreen(page, user, on_product_click)
        self.chatbot_screen = ChatbotScreen(page, user)
        self.facturar_screen = FacturarScreen(page, user)
        
        self.products_view = self.products_screen.build()
        self.chatbot_view = self.chatbot_screen.build()
        self.facturar_view = self.facturar_screen.build()
        self.chatbot_view.visible = False # Ocultar la vista del chatbot inicialmente
        self.facturar_view.visible = False

        self.view = ft.Column(
            controls=[
                self.products_view,
                self.chatbot_view,
                self.facturar_view,
            ],
            expand=True,
        )

        # Definir la barra de navegación
        self.navigation_bar = ft.NavigationBar(
            on_change=self._on_nav_change,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.INVENTORY_2_OUTLINED,
                    selected_icon=ft.Icons.INVENTORY_2,
                    label="Productos"
                ),
                ft.NavigationBarDestination(
                    icon=ft.Image(src="assets/chatbot.png", width=38, height=38),
                    label="Chatbot"
                ),
               ft.NavigationBarDestination(
                   icon=ft.Icons.RECEIPT_LONG_OUTLINED,
                   selected_icon=ft.Icons.RECEIPT_LONG,
                   label="Facturar"
               ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.LOGOUT,
                    label="Cerrar Sesión"
                ),
            ]
        )

    def build(self):
        """Devuelve el control raíz del layout, que es la pantalla de productos."""
        return self.view

    def _on_nav_change(self, e):
        """Maneja los eventos de cambio en la barra de navegación."""
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.products_view.visible = True
            self.chatbot_view.visible = False
            self.facturar_view.visible = False
        elif selected_index == 1:
            self.products_view.visible = False
            self.chatbot_view.visible = True
            self.facturar_view.visible = False
        elif selected_index == 2:
           self.products_view.visible = False
           self.chatbot_view.visible = False
           self.facturar_view.visible = True
        elif selected_index == 3:
            self._handle_logout()
        
        self.page.update()

    def _handle_logout(self):
        """Cierra la sesión del usuario."""
        if AuthService.logout():
            # Limpiar la barra de navegación al salir
            # La vista de login no tendrá navigation_bar, no es necesario limpiarla aquí.
            self.page.go("/login")

    def load_products(self):
        """Carga los productos en la pantalla de productos."""
        self.products_screen._load_products()