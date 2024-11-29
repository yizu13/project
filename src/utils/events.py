import flet as ft
import time

class EventCatalog:
    def __init__(self):
        self.is_pressing = False
        self.count = 0
        self.check_for_send_time = False
        self.check_for_send_intensity = False
        self.check_level_1 = False
        self.check_level_2 = False
        self.check_level_3 = False
        self.patient_name = None
        self.patient_age = None
        self.patient_weight = None
        self.doctor_name = None
        self.confirm_button = None

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

    def send_time(self, e, page, plus_button_from_time, minus_button_from_time,text_field_time,start_button):
        self.plus_button_from_time = plus_button_from_time
        self.minus_button_from_time = minus_button_from_time    
        if (self.check_for_send_time == True):
            plus_button_from_time.disabled = False
            plus_button_from_time.update()
            minus_button_from_time.disabled = False
            minus_button_from_time.update()
            self.check_for_send_time = False
            self.check_start_button(page,start_button)
            page.update()
            return

        if (self.check_for_send_time == False):
            plus_button_from_time.disabled = True
            plus_button_from_time.update()
            minus_button_from_time.disabled = True
            minus_button_from_time.update()
            self.check_for_send_time = True
            print(f"time sent: {text_field_time.value}") # en esta parte se pondrá el enlace para enviar los datos al arduino
            self.check_start_button(page,start_button)
            page.update()
            return
        
    def send_intensity(self, e, page, plus_button_from_intensity, minus_button_from_intensity,text_field_intensity,start_button):
        self.plus_button_from_intensity = plus_button_from_intensity
        self.minus_button_from_intensity = minus_button_from_intensity
        if (self.check_for_send_intensity == True):
            plus_button_from_intensity.disabled = False
            plus_button_from_intensity.update()
            minus_button_from_intensity.disabled = False
            minus_button_from_intensity.update()
            self.check_for_send_intensity = False
            self.check_start_button(page,start_button)
            page.update()
            return

        if (self.check_for_send_intensity == False):
            plus_button_from_intensity.disabled = True
            plus_button_from_intensity.update()
            minus_button_from_intensity.disabled = True
            minus_button_from_intensity.update()
            self.check_for_send_intensity = True
            print(f"intensity sent: {text_field_intensity.value}") # en esta parte se pondrá el enlace para enviar los datos al arduino
            self.check_start_button(page,start_button)
            page.update()
            return
    
    def level_1_(self,e,page, level_2, level_3,start_button):
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_1 = e.control
        if (self.check_level_1  == True):
            level_2.disabled = False
            level_2.update()
            level_3.disabled = False
            level_3.update()
            self.check_level_1 = False
            self.check_start_button(page,start_button)
            page.update()
            return

        if (self.check_level_1 == False):
            level_2.disabled = True
            level_2.update()
            level_3.disabled = True
            level_3.update()
            self.check_level_1 = True
            print("Level 1 activated") # en esta parte se pondrá el enlace para enviar los datos al arduino
            self.check_start_button(page,start_button)
            page.update()
            return



    def level_2_(self,e,page, level_1, level_3,start_button):
        self.level_1 = level_1
        self.level_2 = e.control
        self.level_3 = level_3
        if (self.check_level_2  == True):
            level_1.disabled = False
            level_1.update()
            level_3.disabled = False
            level_3.update()
            self.check_level_2 = False
            self.check_start_button(page,start_button)
            page.update()
            return

        if (self.check_level_2 == False):
            level_1.disabled = True
            level_1.update()
            level_3.disabled = True
            level_3.update()
            self.check_level_2 = True
            print("Level 2 activated") # en esta parte se pondrá el enlace para enviar los datos al arduino
            self.check_start_button(page,start_button)
            page.update()
            return


    def level_3_(self,e,page, level_1, level_2,start_button):
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = e.control
        if (self.check_level_3  == True):
            level_1.disabled = False
            level_1.update()
            level_2.disabled = False
            level_2.update()
            self.check_level_3 = False
            self.check_start_button(page,start_button)
            page.update()
            return

        if (self.check_level_3 == False):
            level_1.disabled = True
            level_1.update()
            level_2.disabled = True
            level_2.update()
            self.check_level_3 = True
            print("Level 3 activated") # en esta parte se pondrá el enlace para enviar los datos al arduino
            self.check_start_button(page,start_button)
            page.update()
            return
        
    def check_start_button(self,page,start_button):
        start_button.disabled = True
        page.update()
        try:
            if (self.level_1.disabled == True or self.level_2.disabled == True or self.level_3.disabled == True ) and (self.plus_button_from_time.disabled == True) and (self.minus_button_from_time.disabled == True) and (self.plus_button_from_intensity.disabled == True) and (self.minus_button_from_intensity.disabled == True):
                start_button.disabled = False
                page.update()
                return
        except:
            None
            
            
    def confirm_button_from_information_page(self,e,page,information_window,fieldtext_doctor,fieldtext_patient):
        fieldtext_doctor.value = self.doctor_name
        fieldtext_patient.value =self.patient_name
        print(fieldtext_patient.value)
        print(self.patient_name)  
        print(self.patient_age)
        print(self.patient_weight)
        print(self.doctor_name)
        page.close(information_window)
        page.update()
        
    def save_patient_name(self,e,confirm_button,page):
        self.patient_name = e.control.value
        if (self.patient_name == ""):
            self.patient_name = None
        self.check_confirm_button(confirm_button,page)
        
    def save_patient_age(self,e,confirm_button,page):
        self.patient_age = e.control.value
        if (self.patient_age == ""):
            self.patient_age = None
        self.check_confirm_button(confirm_button,page)
        
    def save_patient_weight(self,e,confirm_button,page):
        self.patient_weight = e.control.value
        if (self.patient_weight == ""):
            self.patient_weight = None
        self.check_confirm_button(confirm_button,page)
        
    def save_doctor_name(self,e,confirm_button,page):
        self.doctor_name = e.control.value
        if (self.doctor_name == ""):
            self.doctor_name = None
        self.check_confirm_button(confirm_button,page)
    

    def check_confirm_button(self,confirm_button,page): # esto no es un evento
        self.confirm_button = confirm_button
        if (self.patient_name != None) and (self.patient_age != None) and (self.patient_weight != None) and (self.doctor_name != None):
            self.confirm_button.disabled = False
        else: 
            self.confirm_button.disabled = True
        
        page.update()







e_catalog = EventCatalog()