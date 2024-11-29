import flet as ft
from src.controls.Cards_and_buttons import some_cards

class page_home_class:
    def __init__(self):
        self.text_name_patient = None
        self.text_name_doctor =None

    def main_button(self,page):
        self.text_name_patient = ft.Text(theme_style=ft.TextThemeStyle.BODY_LARGE)
        self.text_name_doctor = ft.Text(theme_style=ft.TextThemeStyle.BODY_LARGE)
        # Add controls to the page
        col = ft.Column([ft.Row(controls=some_cards(page, 3))],
                        alignment= ft.MainAxisAlignment.CENTER )
        
        col_1 = ft.Column   ([ ft.Row([ft.Text(value= "Paciente:", color="blue200",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700),self.text_name_patient]),
                               ft.Row([ft.Text(value= "Doctor:",color="blue200",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700),self.text_name_doctor])
                            ],
                        alignment= ft.MainAxisAlignment.END )
        page.add(col, col_1)


page_home_class_ = page_home_class()