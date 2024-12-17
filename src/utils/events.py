import flet as ft
import time
from src.utils.script_communication import communication
import threading
import asyncio

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
        self.information_window = None
        self.check_start = False
        self.warning_comunication_lost=None
        self.loading_page_sign = None
        self.threat_state = None
        self.level_1 = None
        self.level_2 = None
        self.level_3 = None
        self.text_field_intensity = None
        self.text_field_time = None
        self.finalization_button = None
        self.modify_button = None
        
        
    def set_buttons_from_home_page(self,modify_button,finalization_button):
        self.finalization_button = finalization_button
        self.modify_button = modify_button
           
    
    def field_time_keyboard(self,e):
        None

    def close_keyboard(self,e):
        None

    def button_clicked(self,e,page,plus_button_from_time, minus_button_from_time,text_field_time,plus_button_from_intensity, minus_button_from_intensity, text_field_intensity,warning_comunication_lost,loading_page_sign,Time_counting):
        self.start_button = e.control
        self.warning_comunication_lost = warning_comunication_lost
        self.loading_page_sign = loading_page_sign
        self.Time_counting = Time_counting
        count_thread = threading.Thread(target=self.count__, args=(page,))
        
        if (self.check_start == False):
            print("Habilitado")
            self.loading_page_sign.value = None
            self.start_button.text = "Deshabilitar"
            e.control.update()
            self.finalization_button.disabled = True
            self.modify_button.disabled = True
            page.update()
            self.check_start = True
        elif (self.check_start == True):
            self.threat_state = "stop"
            self.disable_all_buttons(page,True,"no_level")
            print("Deshabilitado")
            self.loading_page_sign.value = None
            self.start_button.text = "Habilitar"
            page.update()
            e.control.update()
            communication.Stop_test("Stop test",self.warning_comunication_lost)
            time.sleep(3)
            self.finalization_button.disabled = False
            self.modify_button.disabled = False
            self.disable_all_buttons(page,False,"level")
            self.check_start = False
            
        if(self.start_button.text == "Deshabilitar"):
            self.disable_all_buttons(page,True,"no_level")
            self.threat_state = "count"
            count_thread.start()
            
        self.send_time(page, plus_button_from_time, minus_button_from_time,text_field_time,e.control,warning_comunication_lost)
        self.send_intensity(page, plus_button_from_intensity, minus_button_from_intensity,text_field_intensity,e.control,warning_comunication_lost)
        time.sleep(3)
        self.loading_page_sign.value = 0
        self.disable_all_buttons(page,False,"no_level")
        
        

    def disable_all_buttons(self,page,boolian,state):
       
        if (boolian == True):
            self.level_3.disabled = boolian
            self.level_1.disabled = boolian
            self.level_2.disabled = boolian

        if (self.check_level_1  == True) and (boolian == False) and (state == "level"):
            self.level_1.disabled = boolian

        if (self.check_level_2  == True) and (boolian == False) and (state == "level"):
            self.level_2.disabled = boolian

        if (self.check_level_3  == True) and (boolian == False) and (state == "level"):
            self.level_3.disabled = boolian
        
        self.start_button.disabled = boolian
        page.update()
        
    def count__(self,page):
        start_time = 20
        for i in range(start_time,-1,-1):
            self.Time_counting.value= str(i)
            time.sleep(1)
            page.update()
            if(i == 0):
                print("Warning: time finish")
            elif(self.threat_state == "stop"):
                break
                
        self.Time_counting.value= ""
            
        
        
        
        
    def minus_click(self,e,page,change_value_time,Select_increment_mode,plus_button_from_time, max):
        self.count += 1
        while (Select_increment_mode.selected_index == 0 ) and (self.count == 1):
            change_value_time.value = str(int(change_value_time.value) - 1)
            change_value_time.disabled = True
            page.update()
            time.sleep(0.1)
            if(self.count >= 2) or (int(change_value_time.value) <= 0):
                change_value_time.disabled = False
                self.count = 0

        if(Select_increment_mode.selected_index == 1):
            self.count = 0
            change_value_time.value = str(int(change_value_time.value) - 1)
            page.update()

        if(int(change_value_time.value) <= 0):
            e.control.disabled = True
            change_value_time.disabled = True
            e.control.update()
            page.update()

        elif(int(change_value_time.value) > 0):
            e.control.disabled = False
            change_value_time.disabled = False
            e.control.update()
            page.update()

        if(int(change_value_time.value) <= max):
            plus_button_from_time.disabled = False
            plus_button_from_time.update()
            page.update()


    def plus_click(self, e, page, change_value_time, Select_increment_mode,minus_button_from_time,max):
        self.count += 1
         #hold
        while (Select_increment_mode.selected_index == 0 ) and (self.count == 1):
            change_value_time.value = str(int(change_value_time.value) + 1)
            change_value_time.disabled = True
            page.update()
            time.sleep(0.1)
            if(self.count >= 2) or (int(change_value_time.value) >= max):
                change_value_time.disabled = False
                self.count = 0
          #per click      
        if(Select_increment_mode.selected_index == 1):
            self.count = 0
            change_value_time.value = str(int(change_value_time.value) + 1)
            page.update()

        if(int(change_value_time.value) >= max):
            e.control.disabled = True
            change_value_time.disabled = True
            e.control.update()
            page.update()

        elif(int(change_value_time.value) < max):
            e.control.disabled = False
            change_value_time.disabled = False
            e.control.update()
            page.update()

        if(int(change_value_time.value) > 0):
            minus_button_from_time.disabled = False
            minus_button_from_time.update()
            page.update()

    def field_text_handler_cards_and_buttons(self,e,page,changed_value,max,plus_button,minus_button):
        try:
            if(int(changed_value.value) > 0) and (int(changed_value.value) < max):
                changed_value.disabled = False
                minus_button.disabled = False
                plus_button.disabled = False

            if(int(changed_value.value) <= 0):
                changed_value.disabled = True
                minus_button.disabled = True
                changed_value.value = "0"
            
            if(int(changed_value.value) >= max):
                changed_value.disabled = True
                plus_button.disabled = True
                changed_value.value = str(max)
        except:
            None
        
        page.update()

    def send_time(self, page, plus_button_from_time, minus_button_from_time,text_field_time,start_button,warning_comunication_lost):
        self.text_field_time = text_field_time
        self.plus_button_from_time = plus_button_from_time
        self.minus_button_from_time = minus_button_from_time   

        if (self.check_for_send_time == True):
            plus_button_from_time.disabled = False
            plus_button_from_time.update()
            minus_button_from_time.disabled = False
            minus_button_from_time.update()
            text_field_time.disabled = False
            text_field_time.update()
            self.check_for_send_time = False
            page.update()

            if(int(text_field_time.value) <= 0):
                minus_button_from_time.disabled = True
                minus_button_from_time.update()
                text_field_time.disabled = True
            
            if(int(text_field_time.value) >= 15):
                plus_button_from_time.disabled = True
                plus_button_from_time.update()
                text_field_time.disabled = True

            return

        if (self.check_for_send_time == False):

            plus_button_from_time.disabled = True
            plus_button_from_time.update()
            minus_button_from_time.disabled = True
            minus_button_from_time.update()
            text_field_time.disabled = True
            text_field_time.update()
            print(f"time sent: {text_field_time.value}") # en esta parte se pondrá el enlace para enviar los datos al arduino
            communication.send_time_to_arduino(text_field_time.value,warning_comunication_lost)
            page.update()
            self.check_for_send_time = True

            return
    
        
        
    def send_intensity(self, page, plus_button_from_intensity, minus_button_from_intensity,text_field_intensity,start_button,warning_comunication_lost):
        self.text_field_intensity = text_field_intensity
        self.plus_button_from_intensity = plus_button_from_intensity
        self.minus_button_from_intensity = minus_button_from_intensity

        if (self.check_for_send_intensity == True):
            plus_button_from_intensity.disabled = False
            plus_button_from_intensity.update()
            minus_button_from_intensity.disabled = False
            minus_button_from_intensity.update()
            text_field_intensity.disabled = False
            text_field_intensity.update()
            page.update()
            self.check_for_send_intensity = False

            if(int(text_field_intensity.value) <= 0):
                minus_button_from_intensity.disabled = True
                minus_button_from_intensity.update()
                text_field_intensity.disabled = True
            
            if(int(text_field_intensity.value) >= 100):
                plus_button_from_intensity.disabled = True
                plus_button_from_intensity.update()
                text_field_intensity.disabled = True

            return

        if (self.check_for_send_intensity == False):
            plus_button_from_intensity.disabled = True
            plus_button_from_intensity.update()
            minus_button_from_intensity.disabled = True
            minus_button_from_intensity.update()
            text_field_intensity.disabled = True
            text_field_intensity.update()
            print(f"intensity sent: {text_field_intensity.value}") # en esta parte se pondrá el enlace para enviar los datos al arduino
            communication.send_intensity_to_arduino(text_field_intensity.value,warning_comunication_lost)
            page.update()
            self.check_for_send_intensity = True

            return
    
    def level_1_(self,e,page, level_2, level_3,start_button,loading_page_sign):
        loading_page_sign.value = None
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
            communication.turn_off_level_1("Level 1 desactivated")
            time.sleep(2)
            loading_page_sign.value = 0
            page.update()
            return

        if (self.check_level_1 == False):
            level_2.disabled = True
            level_2.update()
            level_3.disabled = True
            level_3.update()
            self.check_level_1 = True
            self.check_start_button(page,start_button)
            print("Level 1 activated") # en esta parte se pondrá el enlace para enviar los datos al arduino
            communication.turn_on_level_1("Level 1 activated")
            time.sleep(2)
            loading_page_sign.value = 0
            page.update()
            return



    def level_2_(self,e,page, level_1, level_3,start_button,loading_page_sign):
        loading_page_sign.value = None
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
            communication.turn_off_level_2("Level 2 desactivated")
            time.sleep(2)
            loading_page_sign.value = 0
            page.update()
            return

        if (self.check_level_2 == False):
            level_1.disabled = True
            level_1.update()
            level_3.disabled = True
            level_3.update()
            self.check_level_2 = True
            self.check_start_button(page,start_button)
            print("Level 2 activated") # en esta parte se pondrá el enlace para enviar los datos al arduino
            communication.turn_on_level_2("Level 2 activated")
            time.sleep(2)
            loading_page_sign.value = 0
            page.update()
            return


    def level_3_(self,e,page, level_1, level_2,start_button,loading_page_sign):
        loading_page_sign.value = None
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
            communication.turn_off_level_3("Level 3 desactivated")
            time.sleep(2)
            loading_page_sign.value = 0
            page.update()
            return

        if (self.check_level_3 == False):
            level_1.disabled = True
            level_1.update()
            level_2.disabled = True
            level_2.update()
            self.check_level_3 = True
            self.check_start_button(page,start_button)
            print("Level 3 activated") # en esta parte se pondrá el enlace para enviar los datos al arduino
            communication.turn_on_level_3("Level 3 activated")
            time.sleep(2)
            loading_page_sign.value = 0
            page.update()
            return
        
    def check_start_button(self,page,start_button):
        self.start_button = start_button
        start_button.disabled = True
        page.update()
        try:
            if (self.level_1.disabled == True or self.level_2.disabled == True or self.level_3.disabled == True ):
                start_button.disabled = False
                page.update()
                return
        except:
            None
            
            
    def confirm_button_from_information_page(self,e,page,fieldtext_doctor,fieldtext_patient,fieldtext_age_patient,fieldtext_weight_patient):
        fieldtext_doctor.value = self.doctor_name
        fieldtext_patient.value =self.patient_name
        fieldtext_age_patient.value = self.patient_age
        fieldtext_weight_patient.value =self.patient_weight
        print(self.patient_name)  
        print(self.patient_age)
        print(self.patient_weight)
        print(self.doctor_name)
        page.update()
        page.go("/home")
        
    def modify_information_function(self,e,page):
       page.go("/")
        
    def save_patient_name(self,e,confirm_button,page):
        self.patient_name = e.control.value
        self.patient_name_value = e.control
        if (self.patient_name == ""):
            self.patient_name = None
        self.check_confirm_button(confirm_button,page)
        
    def save_patient_age(self,e,confirm_button,page):
        self.patient_age = e.control.value
        self.patient_age_value = e.control
        if (self.patient_age == ""):
            self.patient_age = None
        self.check_confirm_button(confirm_button,page)
        
    def save_patient_weight(self,e,confirm_button,page):
        self.patient_weight = e.control.value
        self.patient_weight_value = e.control
        if (self.patient_weight == ""):
            self.patient_weight = None
        self.check_confirm_button(confirm_button,page)
        
    def save_doctor_name(self,e,confirm_button,page):
        self.doctor_name = e.control.value
        self.doctor_value = e.control
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

    def restart_some_variables_to_disable_start_button(self,page):
        try:
            self.start_button.text = "Habilitar"
            communication.Stop_test("Stop test",self.warning_comunication_lost)
            self.check_start = False
            self.check_for_send_intensity = False
            self.check_for_send_time = False 
            self.plus_button_from_intensity.disabled = False
            self.minus_button_from_intensity.disabled = False
            self.plus_button_from_time.disabled = False
            self.minus_button_from_time.disabled = False
            self.text_field_time.disabled =False
            self.text_field_intensity.disabled = False

            if(int(self.text_field_intensity.value) <= 0):
                self.minus_button_from_intensity.disabled = True
                self.minus_button_from_intensity.update()
                self.text_field_intensity.disabled = True
            
            if(int(self.text_field_intensity.value) >= 100):
                self.plus_button_from_intensity.disabled = True
                self.plus_button_from_intensity.update()
                self.text_field_intensity.disabled = True

            if(int(self.text_field_time.value) <= 0):
                self.minus_button_from_time.disabled = True
                self.minus_button_from_time.update()
                self.text_field_time.disabled = True
            
            if(int(self.text_field_time.value) >= 15):
                self.plus_button_from_time.disabled = True
                self.plus_button_from_time.update()
                self.text_field_time.disabled = True

            
        except:
            None

        page.update()
        
    
    def finish_test(self,e,page):
        try:
            self.level_1.disabled = False #Aquí se mandará al arduino a desactivar bobina 1
            self.level_2.disabled = False #Aquí se mandará al arduino a desactivar bobina 2
            self.level_3.disabled = False #Aquí se mandará al arduino a desactivar bobina 3
        except AttributeError:
            print ("warning: sent without test")
        try:
            self.patient_name_value.value = None
            self.patient_age_value.value = None
            self.patient_weight_value.value = None
            self.doctor_value.value = None
        except:
            print ("warning: sent without test")
        
        try:
            self.text_field_time.value = "1" #Se le mandará este valor al arduino
            self.text_field_intensity.value = "1" #Se le mandará este valor al arduino
            self.plus_button_from_intensity.disabled = False
            self.minus_button_from_intensity.disabled = False
            self.plus_button_from_time.disabled = False
            self.minus_button_from_time.disabled = False
            self.check_for_send_intensity = False
            self.check_for_send_time = False 
        except AttributeError:
             print ("warning: sent without test")
             
        self.check_level_1 = False
        self.check_level_2 = False
        self.check_level_3 = False
        try:
            self.start_button.disabled = True
            self.start_button.text = "Habilitar"
        except AttributeError:
            print ("warning: sent without test")
            
        communication.Stop_test("Stop test",self.warning_comunication_lost)
        page.update()
        
        try:
            self.text_field_time.disabled = False #Se le mandará este valor al arduino
            self.text_field_intensity.disabled = False #Se le mandará este valor al arduino
        except AttributeError:
            print ("warning: sent without test")
            
        try: 
            self.check_start = False
        except AttributeError:
            print ("warning: sent without test")
            
            
        communication.restart_arduino("Restart arduino")
       
        page.update()
        page.go("/")
        
        
    







e_catalog = EventCatalog()