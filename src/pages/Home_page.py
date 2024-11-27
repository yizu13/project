import flet as ft


def main_button(page):
    def some_cards(count):
        some_cards = []
        for i in range(1,count + 1):
            some_cards.append(
                 ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [ft.ElevatedButton("Buy tickets")],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],alignment= ft.MainAxisAlignment.CENTER
                ),
                width=240,
                height= 450,
                padding=1,
            )
        )
)           
            page.update()
    
        return some_cards
    # Add controls to the page
    col = ft.Column([ft.Row(controls=some_cards(3))],alignment= ft.MainAxisAlignment.CENTER )
    page.add(col)