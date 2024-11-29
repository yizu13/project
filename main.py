import flet as ft
from src.pages.Home_page import page_home_class_
from src.pages.test_information import test_information

def main(page: ft.Page):

    page.title = "GPNET_PULSE_SYSTEM"
    page.window.icon = "../assets/GPNET_logo.ico"
    #screen definition 
    page.window.full_screen = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top = False

    page.window.min_width = 800
    page.window.min_height= 600
    page.window.width = 800
    page.window.height= 600
    
    page_home_class_.main_button(page) 
    
    test_information(page)
    
    page.update()
    

def start():
    return ft.app(main)
    
start_page = start()
