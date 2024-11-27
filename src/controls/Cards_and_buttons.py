import flet as ft
from utils.events import e_catalog

def some_cards(page, count):
        some_cards = []
        text_field_time = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
        content_cards = {'card_1': [
                                ft.Row(
                            [   ft.ElevatedButton("Mantener", on_click= lambda e: e_catalog.button_clicked_hold(e,page)),
                                ft.ElevatedButton("Por click")],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                            ft.Row(
                            [   ft.IconButton(ft.icons.REMOVE, on_click=lambda e: e_catalog.minus_click(e,page,text_field_time)),
                                text_field_time,
                                ft.IconButton(ft.icons.ADD, on_click=lambda e: e_catalog.plus_click(e,page,text_field_time))],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ), 
                            ft.Row(
                            [ft.ElevatedButton("Configurar tiempo")],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                            ft.Row(
                            [   ft.IconButton(ft.icons.REMOVE),
                                ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100),
                                ft.IconButton(ft.icons.ADD)],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                            ft.Row(
                            [ft.ElevatedButton("Configurar intensidad")],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                        ],'card_2': [
                            ft.Row(
                            [ft.ElevatedButton("yupi", on_click=lambda e: e_catalog.button_clicked(e,page), width= 200, height= 300)],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                        ],'card_3': []}
        for i in range(1,count + 1):
            some_cards.append(
                 ft.Card(
            content=ft.Container(
                content=ft.Column(
                    content_cards.get(f'card_{i}')
                    ,alignment= ft.MainAxisAlignment.CENTER, spacing= 50
                ),
                width=240,
                height= 450,
                padding=1,
            )
        )
)           
            page.update()
    
        return some_cards