import flet as ft
from src.utils.events import e_catalog


def text_fields(reason, confirm_button,page):
    
    patient_full_name = ft.TextField(text_align=ft.TextAlign.LEFT, width=400, label="Nombre completo del pasciente", on_change= lambda e: e_catalog.save_patient_name(e,confirm_button,page))
    patient_age = ft.TextField(text_align=ft.TextAlign.LEFT, width=200, label="Edad", on_change= lambda e: e_catalog.save_patient_age(e,confirm_button,page),input_filter=ft.NumbersOnlyInputFilter())
    patient_weight = ft.TextField(text_align=ft.TextAlign.LEFT, width=190, label="Peso(lb)", on_change= lambda e: e_catalog.save_patient_weight(e,confirm_button,page),input_filter=ft.NumbersOnlyInputFilter())
    doctor_full_name = ft.TextField(text_align=ft.TextAlign.LEFT, width=400, label="Nombre completo del doctor", on_change= lambda e: e_catalog.save_doctor_name(e,confirm_button,page))
    
    fields = ft.Column(
        [ ft.Row([patient_full_name])
        , ft.Row([patient_age, patient_weight]),
            ft.Row([doctor_full_name])
        ],
        alignment= ft.MainAxisAlignment.CENTER     
    )
    if (reason == "present"):
        return fields