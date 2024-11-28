import flet as ft
from src.utils.events import e_catalog

def some_cards(page, count):
        some_cards = []
        text_field_time = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=100,read_only=True)
        text_field_intensity = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=100,read_only=True)
        # buttons declarations (when is necessary)
        Select_increment_mode = ft.CupertinoSlidingSegmentedButton(
                                selected_index=1,
                                thumb_color=ft.colors.BLUE_400,
                                padding=ft.padding.symmetric(2, 5),
                                controls=[
                                        ft.Text("Mantener"),
                                        ft.Text("Por click")
                                            ])
        plus_button_from_time = ft.IconButton(ft.icons.ADD, on_click=lambda e: e_catalog.plus_click(e,page,text_field_time,Select_increment_mode,minus_button_from_time, 120, setting_time_button))
        minus_button_from_time = ft.IconButton(ft.icons.REMOVE, on_click=lambda e: e_catalog.minus_click(e,page,text_field_time,Select_increment_mode,plus_button_from_time, 120, setting_time_button))

        plus_button_from_intensity = ft.IconButton(ft.icons.ADD, on_click=lambda e: e_catalog.plus_click(e,page,text_field_intensity,Select_increment_mode,minus_button_from_intensity, 100, setting_intensity_button))
        minus_button_from_intensity = ft.IconButton(ft.icons.REMOVE, on_click=lambda e: e_catalog.minus_click(e,page,text_field_intensity,Select_increment_mode,plus_button_from_intensity, 100, setting_intensity_button))

        setting_time_button = ft.ElevatedButton("Configurar tiempo", on_click=lambda e: e_catalog.send_time(e, page, plus_button_from_time, minus_button_from_time,text_field_time, start_button))
        setting_intensity_button = ft.ElevatedButton("Configurar intensidad", on_click=lambda e: e_catalog.send_intensity(e, page, plus_button_from_intensity,  minus_button_from_intensity, text_field_intensity, start_button))

        level_1 = ft.ElevatedButton("Nivel 1", on_click=lambda e: e_catalog.level_1_(e,page,level_2,level_3,start_button), width= 200, height= 100)
        level_2 = ft.ElevatedButton("Nivel 2", on_click=lambda e: e_catalog.level_2_(e,page,level_1,level_3,start_button), width= 200, height= 100)
        level_3 = ft.ElevatedButton("Nivel 3", on_click=lambda e: e_catalog.level_3_(e,page,level_1,level_2,start_button), width= 200, height= 100)


        start_button = ft.ElevatedButton("Empezar", on_click=lambda e: e_catalog.button_clicked(e,page), width= 200, height= 300, disabled= True)

        content_cards = {'card_1': [
                                ft.Row(
                            [  Select_increment_mode
                                    ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                            ft.Row(
                            [   minus_button_from_time,
                                text_field_time,
                                plus_button_from_time],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ), 
                            ft.Row(
                            [
                                  setting_time_button
                             ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                            ft.Row(
                            [     minus_button_from_intensity,
                                  text_field_intensity,
                                plus_button_from_intensity
                                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                            ft.Row(
                            [
                                setting_intensity_button  
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                        ],
                        'card_2': [
                            ft.Row(
                            [start_button],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                        ],
                        'card_3': [
                              ft.Row(
                            [level_1],
                            alignment=ft.MainAxisAlignment.CENTER
                        ), 
                            ft.Row(
                            [level_2],
                            alignment=ft.MainAxisAlignment.CENTER
                        ), 
                            ft.Row(
                            [level_3],
                            alignment=ft.MainAxisAlignment.CENTER
                        )]
                    }
        
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