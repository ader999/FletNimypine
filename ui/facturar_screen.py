import flet as ft
from decimal import Decimal
from services.sale_service import SaleService

class FacturarScreen:
    def __init__(self, page, user):
        self.page = page
        self.user = user
        self.products = []
        self.sale_items = []
        self.total_amount = Decimal('0.0')

        # Controles de la interfaz de usuario
        self.products_dropdown = ft.Dropdown(
            label="Producto",
            options=[],
            on_change=self._on_product_select
        )
        self.quantity_field = ft.TextField(label="Cantidad", width=120)
        self.add_button = ft.IconButton(
            icon=ft.Icons.ADD,
            on_click=self._add_item,
            tooltip="Añadir producto"
        )
        self.sell_button = ft.ElevatedButton(
            text="Vender",
            on_click=self._register_sale
        )
        self.total_text = ft.Text(f"Total: C$0.00", size=20)
        
        self.sale_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Precio Unit.")),
                ft.DataColumn(ft.Text("Subtotal")),
                ft.DataColumn(ft.Text("Acciones")),
            ],
            rows=[]
        )
        
        self._load_products()

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Registrar Venta", size=30),
                ft.Row(
                    controls=[
                        self.products_dropdown,
                        self.quantity_field,
                        self.add_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                self.sale_table,
                ft.Row(
                    controls=[self.total_text, self.sell_button],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            expand=True
        )

    def _load_products(self):
        """Carga los productos desde el servicio y los añade al Dropdown."""
        self.products = SaleService.get_products()
        self.products_dropdown.options = [
            ft.dropdown.Option(key=p.id, text=p.nombre) for p in self.products
        ]
        self.page.update()

    def _on_product_select(self, e):
        """Maneja la selección de un producto en el Dropdown."""
        # Opcional: Lógica adicional al seleccionar un producto
        pass

    def _add_item(self, e):
        """Añade un producto a la tabla de venta."""
        product_id = self.products_dropdown.value
        quantity = self.quantity_field.value

        if not product_id or not quantity:
            # Mostrar un mensaje de error si faltan datos
            return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            # Mostrar un mensaje de error si la cantidad no es válida
            return

        product = next((p for p in self.products if p.id == int(product_id)), None)
        if not product:
            return

        # Añadir el item a la lista y actualizar la tabla
        subtotal = quantity * product.precio_venta
        self.sale_items.append({
            "product_id": product.id,
            "product_name": product.nombre,
            "quantity": quantity,
            "unit_price": product.precio_venta,
            "subtotal": subtotal
        })
        self._update_sale_table()
        self.quantity_field.value = ""
        self.products_dropdown.value = None
        self.page.update()

    def _update_sale_table(self):
        """Actualiza la tabla de venta y el total."""
        self.sale_table.rows.clear()
        self.total_amount = Decimal('0.0')
        
        for i, item in enumerate(self.sale_items):
            self.total_amount += item['subtotal']
            self.sale_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item['product_name'])),
                        ft.DataCell(ft.Text(str(item['quantity']))),
                        ft.DataCell(ft.Text(f"C${item['unit_price']:.2f}")),
                        ft.DataCell(ft.Text(f"C${item['subtotal']:.2f}")),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                on_click=lambda _, index=i: self._remove_item(index),
                                tooltip="Eliminar"
                            )
                        ),
                    ]
                )
            )
        
        self.total_text.value = f"Total: C${self.total_amount:.2f}"
        self.page.update()

    def _remove_item(self, index):
        """Elimina un item de la lista de venta."""
        if 0 <= index < len(self.sale_items):
            del self.sale_items[index]
            self._update_sale_table()

    def _register_sale(self, e):
        """Registra la venta a través del servicio."""
        if not self.sale_items:
            # Mostrar mensaje si no hay items
            return

        success, message = SaleService.register_sale(self.sale_items)
        
        if success:
            # Limpiar la venta y mostrar mensaje de éxito
            self.sale_items.clear()
            self._update_sale_table()
            # Aquí podrías mostrar un SnackBar de éxito
        else:
            # Mostrar mensaje de error
            pass
        
        self.page.update()
