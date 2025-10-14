import flet as ft
from services.product_service import ProductService

class ProductsScreen:
    def __init__(self, page, user):
        self.page = page
        self.user = user
        self.products = []
        self.products_list = ft.Column(scroll=ft.ScrollMode.AUTO)

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(f"Bienvenido, {self.user.first_name}!", size=20),
                    ft.ElevatedButton("Cerrar Sesión", on_click=self._handle_logout)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Text("Mis Productos", size=24, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Actualizar", on_click=self._load_products),
                self.products_list
            ]),
            padding=20
        )

    def _load_products(self, e=None):
        self.products = ProductService.get_products()
        self._render_products()
        self.page.update()

    def _render_products(self):
        self.products_list.controls.clear()
        if not self.products:
            self.products_list.controls.append(
                ft.Text("No hay productos disponibles", italic=True)
            )
        else:
            for product in self.products:
                self.products_list.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(product.nombre, size=18, weight=ft.FontWeight.BOLD),
                                ft.Text(f"Precio: ${product.precio_venta}", size=16),
                                ft.Text(f"Stock: {product.stock_actual}", size=14),
                                ft.Text(product.descripcion, size=12, color=ft.Colors.GREY)
                            ]),
                            padding=10
                        )
                    )
                )

    def _handle_logout(self, e):
        from services.auth_service import AuthService
        if AuthService.logout():
            self.page.go("/login")