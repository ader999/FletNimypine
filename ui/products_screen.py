import flet as ft
from services.product_service import ProductService

class ProductsScreen:
    def __init__(self, page, user, on_product_click):
        self.page = page
        self.user = user
        self.on_product_click = on_product_click
        self.products = []
        self.products_list = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )

    def build(self):
        return ft.Column([
            ft.Text("Mis Productos", size=24, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Actualizar", on_click=self._load_products),
            self.products_list,
        ])

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
                            padding=10,
                            on_click=lambda e, p=product: self.on_product_click(p)
                        )
                    )
                )

    def _handle_logout(self, e):
        # This method is now handled by MainLayout
        pass