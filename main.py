import flet as ft
from ui.login_screen import LoginScreen
from ui.register_screen import RegisterScreen
from ui.products_screen import ProductsScreen

def main(page: ft.Page):
    page.title = "NIMYPINE - Gestión MIPYMES"
    page.theme_mode = ft.ThemeMode.LIGHT
    # Remove window dimensions for mobile app

    current_user = None

    def route_change(e):
        nonlocal current_user
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
            products_screen = ProductsScreen(page, current_user)
            page.views.append(
                ft.View(
                    "/products",
                    [products_screen.build()]
                )
            )
            # Cargar productos automáticamente
            products_screen._load_products()
        else:
            page.go("/login")

        page.update()

    def on_login_success(user):
        nonlocal current_user
        current_user = user
        page.go("/products")

    page.on_route_change = route_change
    page.go("/login")

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)