import flet as ft
import asyncio
import time

class EventCatalog:
    def __init__(self):
        self.is_pressing = False

    def button_clicked(self,e,page):
        print("yupi")
        e.control.disabled = False
        e.control.update()
        page.update()
    
    def button_clicked_hold(self,e,page):
        e.control.disable= True

    def minus_click(self,e,page,change_value_time):
        change_value_time.value = str(int(change_value_time.value) - 1)
        self.is_pressing = False
        page.update()

    def plus_click(self,e,page,change_value_time):
        self.is_pressing = True
        while (self.is_pressing):
            change_value_time.value = str(int(change_value_time.value) + 1)
            page.update()













e_catalog = EventCatalog()