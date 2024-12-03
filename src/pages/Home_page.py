import flet as ft
from src.controls.Cards_and_buttons import some_cards
from src.utils.events import e_catalog

class page_home_class:
    def __init__(self):
        self.text_name_patient = None
        self.text_name_doctor =None
        self.text_age_patient = None
        self.text_weight_patient = None
        self.modify_button = None
        self.finalization_button = None
        
    

    def main_button(self,page):
        self.text_name_patient = ft.Text(theme_style=ft.TextThemeStyle.BODY_LARGE)
        self.text_name_doctor = ft.Text(theme_style=ft.TextThemeStyle.BODY_LARGE)
        self.text_age_patient = ft.Text(theme_style=ft.TextThemeStyle.BODY_LARGE)
        self.text_weight_patient = ft.Text(theme_style=ft.TextThemeStyle.BODY_LARGE)
        self.modify_button = ft.TextButton(text="Modificar", on_click=lambda e: e_catalog.modify_information_function(e,page))
        self.finalization_button = ft.ElevatedButton(text="Finalizar Terapia",on_click=lambda e:e_catalog.finish_test(e,page))
        # Add controls to the page
        col = ft.Column([ft.Row(controls=some_cards(page, 3))],
                        alignment= ft.MainAxisAlignment.CENTER )
        
        col_1 = ft.Column   ([ ft.Row([ft.Text(value= "Paciente:", color="blue800",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700),self.text_name_patient]),
                                ft.Row([ft.Text(value= "Edad del paciente:",color="blue800",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700), self.text_age_patient]),
                                ft.Row([ft.Text(value= "Peso del paciente:",color="blue800",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700), self.text_weight_patient]),
                                ft.Row([ft.Text(value= "Doctor:",color="blue800",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700), self.text_name_doctor]),
                               ft.Row([self.modify_button,self.finalization_button], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
                            ],
                        alignment= ft.MainAxisAlignment.END)
        
        
        page.add(col, col_1)


page_home_class_ = page_home_class()