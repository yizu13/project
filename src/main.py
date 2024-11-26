import flet as ft
from pages.Home_page import main_button

def main(page: ft.Page):
    page.title = "GPNET_PULSE_SYSTEM"
    
    #screen definition 
    page.window.full_screen = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    main_button(page)
    
    page.update()
    


ft.app(main)
