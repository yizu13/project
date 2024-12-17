import flet as ft
from src.utils.events import e_catalog


def text_fields(reason, confirm_button,page):
        
    patient_full_name = ft.TextField(text_align=ft.TextAlign.LEFT, label="Nombre completo del paciente", on_change= lambda e: e_catalog.save_patient_name(e,confirm_button,page),border=ft.InputBorder.NONE, height=50)
    patient_age = ft.TextField(text_align=ft.TextAlign.LEFT, label="Edad", on_change= lambda e: e_catalog.save_patient_age(e,confirm_button,page),input_filter=ft.NumbersOnlyInputFilter(),border=ft.InputBorder.NONE, height=50)
    patient_weight = ft.TextField(text_align=ft.TextAlign.LEFT, label="Peso(lb)", on_change= lambda e: e_catalog.save_patient_weight(e,confirm_button,page),input_filter=ft.NumbersOnlyInputFilter(),border=ft.InputBorder.NONE, height=50)
    doctor_full_name = ft.TextField(text_align=ft.TextAlign.LEFT, label="Nombre completo del doctor", on_change= lambda e: e_catalog.save_doctor_name(e,confirm_button,page),border=ft.InputBorder.NONE, height=50)
        
    fields = ft.Column(
        [ ft.Row([ft.Icon(name='PERSON_ROUNDED', color="blue"),patient_full_name,ft.Icon(name='ACCESS_TIME_FILLED', color="blue"), patient_age]),
            ft.Row([ft.Icon(name='MONITOR_WEIGHT_ROUNDED', color="blue"),patient_weight,ft.Icon(name='PERSON_PIN_CIRCLE_SHARP', color="blue"),doctor_full_name])
            ],
        alignment= ft.MainAxisAlignment.CENTER     
            )
    if (reason == "present"):
        return fields