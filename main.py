import flet as ft


def main(page: ft.Page):
    t = ft.SafeArea(ft.Text(value="Hello, Flet!",color="red"))
    page.control.append(t)
    page.update()


ft.app(main)
