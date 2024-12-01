import flet as ft
from src.utils.events import e_catalog


def text_fields(reason, confirm_button,page):
        
    patient_full_name = ft.TextField(text_align=ft.TextAlign.LEFT, label="Nombre completo del pasciente", on_change= lambda e: e_catalog.save_patient_name(e,confirm_button,page),border=ft.InputBorder.NONE)
    patient_age = ft.TextField(text_align=ft.TextAlign.LEFT, label="Edad", on_change= lambda e: e_catalog.save_patient_age(e,confirm_button,page),input_filter=ft.NumbersOnlyInputFilter(),border=ft.InputBorder.NONE)
    patient_weight = ft.TextField(text_align=ft.TextAlign.LEFT, label="Peso(lb)", on_change= lambda e: e_catalog.save_patient_weight(e,confirm_button,page),input_filter=ft.NumbersOnlyInputFilter(),border=ft.InputBorder.NONE)
    doctor_full_name = ft.TextField(text_align=ft.TextAlign.LEFT, label="Nombre completo del doctor", on_change= lambda e: e_catalog.save_doctor_name(e,confirm_button,page),border=ft.InputBorder.NONE)
        
    fields = ft.Column(
        [ ft.Row([patient_full_name])
        , ft.Row([patient_age]),
            ft.Row([patient_weight]),
            ft.Row([doctor_full_name])
            ],
        alignment= ft.MainAxisAlignment.CENTER     
            )
    if (reason == "present"):
        return fields