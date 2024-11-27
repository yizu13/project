import flet as ft


def main_button(page):
    # Create the button and text
    time_set_button = ft.ElevatedButton("Configurar tiempo")
    time_set_button.aligment = ft.alignment.center
    # Add controls to the page
    page.add(time_set_button)