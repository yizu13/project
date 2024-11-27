import flet as ft
from controls.Cards_and_buttons import some_cards

def main_button(page):
    # Add controls to the page
    col = ft.Column([ft.Row(controls=some_cards(page, 3))],alignment= ft.MainAxisAlignment.CENTER )
    page.add(col)