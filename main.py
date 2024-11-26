import flet as ft
import time


def main(page: ft.Page):
    t = ft.Text(value="Hello, Flet!",color="red")
    page.controls.append(t)
    page.update()
    
    for i in range(10):
        t.value = f"counting {i}"
        page.update()
        time.sleep(1)


ft.app(main)
