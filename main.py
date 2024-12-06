import flet as ft

def main(page: ft.Page):
        page.window.close()
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
        
        
        page.update()
    


ft.app(target=main)

