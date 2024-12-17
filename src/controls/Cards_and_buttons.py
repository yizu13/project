import flet as ft
from src.utils.events import e_catalog

def some_cards(page, count):
        some_cards = []
        text_field_time = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=100,read_only=False,border=ft.InputBorder.UNDERLINE, filled=True, on_focus=lambda e: e_catalog.field_time_keyboard(e),on_blur=lambda e: e_catalog.close_keyboard(e), on_change=lambda e: e_catalog.field_text_handler_cards_and_buttons(e,page,e.control,15,plus_button_from_time,minus_button_from_time),input_filter=ft.NumbersOnlyInputFilter())
        text_field_intensity = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=100,read_only=False,border=ft.InputBorder.UNDERLINE, filled=True, on_change=lambda e: e_catalog.field_text_handler_cards_and_buttons(e,page,e.control,100,plus_button_from_intensity,minus_button_from_intensity),input_filter=ft.NumbersOnlyInputFilter())
        # buttons declarations (when is necessary)
        Select_increment_mode = ft.CupertinoSlidingSegmentedButton(
                                selected_index=1,
                                thumb_color=ft.colors.BLUE_400,
                                padding=ft.padding.symmetric(2, 5),
                                controls=[
                                        ft.Text("Mantener"),
                                        ft.Text("Por click")
                                            ])
        plus_button_from_time = ft.IconButton(ft.icons.ADD, on_click=lambda e: e_catalog.plus_click(e,page,text_field_time,Select_increment_mode,minus_button_from_time, 15))
        minus_button_from_time = ft.IconButton(ft.icons.REMOVE, on_click=lambda e: e_catalog.minus_click(e,page,text_field_time,Select_increment_mode,plus_button_from_time, 15))

        plus_button_from_intensity = ft.IconButton(ft.icons.ADD, on_click=lambda e: e_catalog.plus_click(e,page,text_field_intensity,Select_increment_mode,minus_button_from_intensity, 100))
        minus_button_from_intensity = ft.IconButton(ft.icons.REMOVE, on_click=lambda e: e_catalog.minus_click(e,page,text_field_intensity,Select_increment_mode,plus_button_from_intensity, 100))

        setting_time_button = ft.Text("Tiempo Rampa TEC Imax")
        setting_intensity_button = ft.Text("Introducir % potencia")

        level_1 = ft.ElevatedButton("NIVEL 1: 87VAC 8mW", on_click=lambda e: e_catalog.level_1_(e,page,level_2,level_3,start_button,loading_page_sign), width= 210, height= 60)
        level_2 = ft.ElevatedButton("NIVEL 2: 129VAC 162mW", on_click=lambda e: e_catalog.level_2_(e,page,level_1,level_3,start_button,loading_page_sign), width= 210, height= 60)
        level_3 = ft.ElevatedButton("NIVEL 3: 141VAC 193mW", on_click=lambda e: e_catalog.level_3_(e,page,level_1,level_2,start_button,loading_page_sign), width= 210, height= 60)


        start_button = ft.ElevatedButton(text="Habilitar", on_click=lambda e: e_catalog.button_clicked(e,page,plus_button_from_time, minus_button_from_time,text_field_time,plus_button_from_intensity, minus_button_from_intensity, text_field_intensity,warning_comunication_lost,loading_page_sign,Time_counting), width= 150, height= 60, disabled= True)
        text_checking_for_button = ft.Text("Estatus de la terapia", color="red800",theme_style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.W_700)
        warning_comunication_lost = ft.Text (value="",color="red800",weight=ft.FontWeight.W_900, theme_style=ft.TextThemeStyle.BODY_LARGE)
        Time_counting = ft.Text (value="",color="red800",weight=ft.FontWeight.W_900, theme_style=ft.TextThemeStyle.BODY_LARGE)
        loading_page_sign = ft.ProgressRing(value= 0, width=20, height=20, stroke_width = 2)

        content_cards = {'card_1': [
                                ft.Row(
                            [  Select_increment_mode
                                    ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                            ft.Row(
                            [
                                setting_time_button
                             ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                            ft.Row(
                            [   minus_button_from_time,
                                text_field_time,
                                plus_button_from_time],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ), 
                            ft.Row(
                            [
                                setting_intensity_button  
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                            ft.Row(
                            [     minus_button_from_intensity,
                                  text_field_intensity,
                                plus_button_from_intensity
                                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                        ],
                        'card_2': [
                             ft.Row(
                            [Time_counting],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                            ft.Row(
                            [text_checking_for_button],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),  
                            ft.Row(
                            [start_button],
                            alignment=ft.MainAxisAlignment.CENTER
                        ), 
                            ft.Row(
                            [warning_comunication_lost],
                            alignment=ft.MainAxisAlignment.CENTER
                        ), 
                            ft.Row(
                            [loading_page_sign],
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
                    ,alignment= ft.MainAxisAlignment.CENTER, spacing= 5
                ),
                width=240,
                height=205,
                padding=1,
            )
        )
)           
            page.update()
    
        return some_cards