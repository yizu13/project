import flet as ft
from src.pages.Home_page import page_home_class_
from src.pages.test_information import test_information
from src.utils.verificaiton import verify

def main(page: ft.Page):
    verify.calling_def()
    if (verify.puerto_arduino == None):
        page.window.close()
    else:
        page.title = "GPNET_PULSE_SYSTEM"
        page.window.icon = "../assets/GPNET_logo.ico"
        #screen definition 
        page.window.full_screen = False
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window.always_on_top = False
        page.theme_mode = ft.ThemeMode.LIGHT

        page.window.max_width = 800
        page.window.max_height= 480
        page.window.width = 800
        page.window.height= 480
        
        
        def route_change(route):
            page.views.clear()
            page.views.append(
                ft.View(
                    "/",
                    [
                    ft.AppBar(title=ft.Text("Informaciones importantes"), bgcolor='BLUE'),
                       test_information(page)
                    ],
                )
            )
            if page.route == "/home":
                page.views.append(
                    ft.View(
                        "/home",
                        [
                            page_home_class_.main_button(page,"cards"),
                            page_home_class_.main_button(page,"content")
                        ],
                    )
                )
            page.update()

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)
    

def start():
    return ft.app(main)
    
start_page = start()
