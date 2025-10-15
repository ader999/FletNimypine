import flet as ft
from ui.login_screen import LoginScreen
from ui.register_screen import RegisterScreen
from ui.products_screen import ProductsScreen
from ui.product_detail_screen import ProductDetailScreen
from ui.main_layout import MainLayout

def main(page: ft.Page):
    page.title = "Nimypine"
    page.theme_mode = ft.ThemeMode.LIGHT
    # Remove window dimensions for mobile app

    current_user = None
    selected_product = None

    def route_change(e):
        nonlocal current_user, selected_product
        page.views.clear()

        if page.route == "/login" or page.route == "/":
            login_screen = LoginScreen(page, on_login_success)
            page.views.append(
                ft.View(
                    "/login",
                    [login_screen.build()]
                )
            )
        elif page.route == "/register":
            register_screen = RegisterScreen(page)
            page.views.append(
                ft.View(
                    "/register",
                    [register_screen.build()]
                )
            )
        elif page.route == "/products" and current_user:
            main_layout = MainLayout(page, current_user, on_product_click)
            # La AppBar se elimina, la navegación ahora está en el layout
            page.views.append(
                ft.View(
                    "/products",
                    [main_layout.build()],
                    navigation_bar=main_layout.navigation_bar
                )
            )
            # Cargar productos automáticamente
            main_layout.load_products()
        elif page.route == "/product_detail" and current_user and selected_product:
            product_detail_screen = ProductDetailScreen(page, selected_product, lambda e: page.go("/products"))
            page.views.append(
                ft.View(
                    "/product_detail",
                    [product_detail_screen.build()]
                )
            )
        else:
            page.go("/login")

        page.update()

    def on_login_success(user):
        nonlocal current_user
        current_user = user
        page.go("/products")

    def on_product_click(product):
        nonlocal selected_product
        selected_product = product
        page.go("/product_detail")

    page.on_route_change = route_change
    page.go("/login")

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)