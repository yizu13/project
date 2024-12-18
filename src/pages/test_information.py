import flet as ft
from src.controls.information_controls_content import text_fields
from src.utils.events import e_catalog
from src.pages.Home_page import page_home_class_


def test_information(page):
    page_home_class_.main_button(page,"empty")
    confirm_button = ft.TextButton("Confirmar",icon='SEND_TO_MOBILE', on_click=lambda e: e_catalog.confirm_button_from_information_page(e,page,page_home_class_.text_name_doctor,page_home_class_.text_name_patient,page_home_class_.text_age_patient,page_home_class_.text_weight_patient))
    page_important_content = text_fields("present", confirm_button,page)
    
    # Add temporary page
    
    col = ft.Column([ ft.Row([page_important_content]),
                        ft.Row([confirm_button])
                            ],
                        alignment= ft.MainAxisAlignment.END)
    
    e_catalog.check_confirm_button(confirm_button,page)
    return col
