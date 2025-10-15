import flet as ft
from services.auth_service import AuthService
from ui.products_screen import ProductsScreen

class MainLayout:
    def __init__(self, page, user, on_product_click):
        self.page = page
        self.user = user
        self.products_screen = ProductsScreen(page, user, on_product_click)
        
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
                    icon=ft.Icons.LOGOUT,
                    label="Cerrar Sesión"
                ),
            ]
        )

    def build(self):
        """Devuelve el control raíz del layout, que es la pantalla de productos."""
        return self.products_screen.build()

    def _on_nav_change(self, e):
        """Maneja los eventos de cambio en la barra de navegación."""
        selected_index = e.control.selected_index
        if selected_index == 0:
            # Ya estamos en la vista de productos, no hacemos nada.
            # Podríamos añadir lógica si hubiera más vistas.
            pass
        elif selected_index == 1:
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