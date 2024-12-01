import flet as ft
from src.controls.information_controls_content import text_fields
from src.utils.events import e_catalog
from src.pages.Home_page import page_home_class_


def test_information(page):
    confirm_button = ft.TextButton("Confirmar", on_click=lambda e: e_catalog.confirm_button_from_information_page(e,page,dlg_modal,page_home_class_.text_name_doctor,page_home_class_.text_name_patient))
    page_important_content = text_fields("present", confirm_button,page)
    
    # Add temporary page
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("  Informaciones importantes  "),
        content= ft.SafeArea(page_important_content, height=300),
        actions=[# here you will put the fuctions of controls  
            ft.SafeArea(ft.Container(confirm_button ,alignment=ft.alignment.bottom_right),expand=True)
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER
    )
    e_catalog.check_confirm_button(confirm_button,page)
    page.open(dlg_modal)
