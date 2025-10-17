import flet as ft
from models.product import Product

class ProductDetailScreen:
    def __init__(self, page, product: Product, on_back):
        self.page = page
        self.product = product
        self.on_back = on_back

    def build(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.ARROW_BACK, on_click=self.on_back),
                        ft.Text("Detalles del Producto", size=24, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.ListView(
                    expand=True,
                    controls=[
                        ft.Text(f"Nombre: {self.product.nombre}", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Descripción: {self.product.descripcion}", size=16),
                        ft.Text(f"Precio de Venta: ${self.product.precio_venta}", size=18, color=ft.Colors.GREEN),
                        ft.Text(f"Precio de Producción: ${self.product.costo_de_produccion}", size=18, color=ft.Colors.RED),
                        ft.Text(f"Porcentaje de Ganancia: {self.product.porcentaje_ganancia}%", size=16),
                        ft.Text(f"Stock Actual: {self.product.stock_actual}", size=16),
                        ft.Text(f"Peso: {self.product.peso} kg" if self.product.peso else "Peso: N/A", size=16),
                        ft.Text(f"Tamaño: {self.product.tamano_largo}x{self.product.tamano_ancho}x{self.product.tamano_alto} cm" if self.product.tamano_largo and self.product.tamano_ancho and self.product.tamano_alto else "Tamaño: N/A", size=16),
                        ft.Text(f"Presentación: {self.product.presentacion}", size=16),
                        ft.Divider(),
                        ft.Text("Insumos (Formulación):", size=18, weight=ft.FontWeight.BOLD),
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(f"Insumo: {insumo.get('insumo_nombre', 'N/A')}", weight=ft.FontWeight.BOLD),
                                            ft.Text(f"Descripción: {insumo.get('insumo_descripcion', 'N/A')}"),
                                            ft.Text(f"Cantidad: {insumo.get('cantidad', 0)} {insumo.get('unidad', '')}"),
                                            ft.Text(f"Porcentaje Desperdicio: {insumo.get('porcentaje_desperdicio', 0)}%"),
                                            ft.Text(f"Costo Unitario: ${insumo.get('costo_unitario', 0)}"),
                                        ]
                                    ),
                                    padding=10,
                                    border=ft.border.all(1, ft.Colors.OUTLINE),
                                    border_radius=5,
                                    margin=ft.margin.symmetric(vertical=5),
                                )
                                for insumo in self.product.formulacion
                            ]
                        ),
                        ft.Divider(),
                        ft.Text("Procesos:", size=18, weight=ft.FontWeight.BOLD),
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(f"Proceso: {proceso.get('proceso_nombre', 'N/A')}", weight=ft.FontWeight.BOLD),
                                            ft.Text(f"Tiempo: {proceso.get('tiempo_en_minutos', 0)} minutos"),
                                            ft.Text(f"Costo por Hora: ${proceso.get('costo_por_hora', 0)}"),
                                        ]
                                    ),
                                    padding=10,
                                    border=ft.border.all(1, ft.Colors.OUTLINE),
                                    border_radius=5,
                                    margin=ft.margin.symmetric(vertical=5),
                                )
                                for proceso in self.product.procesos_detalles
                            ]
                        ),
                        ft.Divider(),
                        ft.Text("Impuestos:", size=18, weight=ft.FontWeight.BOLD),
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(f"Impuesto: {impuesto.get('nombre', 'N/A')}", weight=ft.FontWeight.BOLD),
                                            ft.Text(f"Porcentaje: {impuesto.get('porcentaje', 0)}%"),
                                            ft.Text(f"Activo: {'Sí' if impuesto.get('activo', False) else 'No'}"),
                                        ]
                                    ),
                                    padding=10,
                                    border=ft.border.all(1, ft.Colors.OUTLINE),
                                    border_radius=5,
                                    margin=ft.margin.symmetric(vertical=5),
                                )
                                for impuesto in self.product.impuestos_detalles
                            ]
                        ),
                    ],
                    spacing=10,
                ),
            ],
            expand=True,
        )