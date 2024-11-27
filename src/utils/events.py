import flet as ft
import time

class EventCatalog:
    def __init__(self):
        self.is_pressing = False
        self.count = 0
        self.check_for_send_time = False
        self.check_for_send_intensity = False

    def button_clicked(self,e,page):
        print("yupi")
        e.control.disabled = False
        e.control.update()
        page.update()
    
        
    def minus_click(self,e,page,change_value_time,Select_increment_mode,plus_button_from_time, max,setting_button):
        self.count += 1
        while (Select_increment_mode.selected_index == 0 ) and (self.count == 1):
            change_value_time.value = str(int(change_value_time.value) - 1)
            page.update()
            setting_button.disabled = True
            time.sleep(0.1)
            if(self.count >= 2) or (int(change_value_time.value) <= 0):
                setting_button.disabled = False
                self.count = 0

        if(Select_increment_mode.selected_index == 1):
            self.count = 0
            change_value_time.value = str(int(change_value_time.value) - 1)
            page.update()

        if(int(change_value_time.value) <= 0):
            e.control.disabled = True
            e.control.update()
            page.update()

        elif(int(change_value_time.value) > 0):
            e.control.disabled = False
            e.control.update()
            page.update()

        if(int(change_value_time.value) <= max):
            plus_button_from_time.disabled = False
            plus_button_from_time.update()
            page.update()


    def plus_click(self, e, page, change_value_time, Select_increment_mode,minus_button_from_time,max,setting_button):
        self.count += 1
         #hold
        while (Select_increment_mode.selected_index == 0 ) and (self.count == 1):
            change_value_time.value = str(int(change_value_time.value) + 1)
            setting_button.disabled = True
            page.update()
            time.sleep(0.1)
            if(self.count >= 2) or (int(change_value_time.value) >= max):
                setting_button.disabled = False
                self.count = 0
          #per click      
        if(Select_increment_mode.selected_index == 1):
            self.count = 0
            change_value_time.value = str(int(change_value_time.value) + 1)
            page.update()

        if(int(change_value_time.value) >= max):
            e.control.disabled = True
            e.control.update()
            page.update()

        elif(int(change_value_time.value) < max):
            e.control.disabled = False
            e.control.update()
            page.update()

        if(int(change_value_time.value) > 0):
            minus_button_from_time.disabled = False
            minus_button_from_time.update()
            page.update()

    def send_time(self, e, page, plus_button_from_time, minus_button_from_time,text_field_time):
        if (self.check_for_send_time == True):
            plus_button_from_time.disabled = False
            plus_button_from_time.update()
            minus_button_from_time.disabled = False
            minus_button_from_time.update()
            self.check_for_send_time = False
            page.update()
            return

        if (self.check_for_send_time == False):
            plus_button_from_time.disabled = True
            plus_button_from_time.update()
            minus_button_from_time.disabled = True
            minus_button_from_time.update()
            self.check_for_send_time = True
            print(f"time sent: {text_field_time.value}") # en esta parte se pondrá el enlace para enviar los datos al arduino
            page.update()
            return
        
    def send_intensity(self, e, page, plus_button_from_intensity, minus_button_from_intensity,text_field_intensity):
        if (self.check_for_send_intensity == True):
            plus_button_from_intensity.disabled = False
            plus_button_from_intensity.update()
            minus_button_from_intensity.disabled = False
            minus_button_from_intensity.update()
            self.check_for_send_intensity = False
            page.update()
            return

        if (self.check_for_send_intensity == False):
            plus_button_from_intensity.disabled = True
            plus_button_from_intensity.update()
            minus_button_from_intensity.disabled = True
            minus_button_from_intensity.update()
            self.check_for_send_intensity = True
            print(f"intensity sent: {text_field_intensity.value}") # en esta parte se pondrá el enlace para enviar los datos al arduino
            page.update()
            return
        

        












e_catalog = EventCatalog()