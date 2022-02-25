#gooz_pin_pwm.py v1
from machine import PWM,Pin
import utime
from system.config import find_value

saved_pwms = []

def register(cmd_arr):
    key = ""
    value = ""
    key_list = []
    value_list = []
    registered_key = []
    registered_value = []
    global saved_pwms
    
    for i in cmd_arr:
        if i[0] == "-":
            for a in range(1,len(i)):
                if i[a] == "=":
                    break
                key += i[a]
            key_list.append(key)
            door = 0
            for index in range(1,len(i)):
                if i[index] == ")":
                    door = 0
                if door == 1:
                    value += i[index]
                elif i[index] == "(":
                    door = 1
            value_list.append(value)
            key = ""
            value = ""
    registered_key.append(key_list)
    registered_value.append(value_list)
    temp_counter = 0
    
    temp = {"name":"","freq":"","pin":""}
    temp["freq"]= find_value("pwm/freq")
    
    for pairs in key_list:
        if pairs == "name":
            temp["name"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "freq":
            temp["freq"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "pin":
            temp["pin"] = value_list[temp_counter]
            temp_counter += 1
    if temp["name"] == "" or temp["pin"] == "":
        print("Missing necessary argument(s)!\n<pwm_name> or <pwm_pin> is empty.")
        return
    #Saving
    isNameExist =False
    for myPWM in saved_pwms:
        if myPWM["name"] == temp["name"]:
            isNameExist = True
    if isNameExist:
        print(f'The pin named "{temp["name"]}" already exists')
        return    
    
    saved_pwms.append(temp)
    print(saved_pwms)
        
def write(cmd_arr):
    exported_pin = {"name":"","freq":"","pin":""}
    if not len(cmd_arr) > 4:
        print("Missing Argument!\nMissing pin name for writing.")
        return
        
    for myPWM in saved_pwms:
        if cmd_arr[3] == myPWM["name"]:
            exported_pin["name"] = myPWM["name"]
            exported_pin["freq"] = myPWM["freq"]
            exported_pin["pin"] = myPWM["pin"]
            
    if exported_pin["name"] == "":
        print(f'There is no PWM pin named "{cmd_arr[3]}"!')
        return
    pwm_t = PWM(Pin(int(exported_pin["pin"],Pin.OUT)),freq=int(exported_pin["freq"]))
    pwm_t.duty(int(cmd_arr[4]))
        
def update(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument(s)\nWhat will be updated?")
        return
    
    exported_pin = {"name":"","freq":"","pin":""}
    for myPWM in saved_pwms:
        if myPWM["name"] == cmd_arr[3]:
            exported_pin["name"] = myPWM["name"]
            exported_pin["freq"] = myPWM["freq"]
            exported_pin["pin"] = myPWM["pin"]
            saved_pwms.remove(myPWM)
        
    if exported_pin["name"] == "":
        print(f'There is no PWM pin named "{cmd_arr[3]}"!')
        return
    
    key = ""
    value = ""
    key_list = []
    value_list = []
    registered_key = []
    registered_value = []
    for i in cmd_arr:
        if i[0] == "-":
            for a in range(1,len(i)):
                if i[a] == "=":
                    break
                key += i[a]
            key_list.append(key)
            door = 0
            for index in range(1,len(i)):
                if i[index] == ")":
                    door = 0
                if door == 1:
                    value += i[index]
                elif i[index] == "(":
                    door = 1
            value_list.append(value)
            key = ""
            value = ""
    registered_key.append(key_list)
    registered_value.append(value_list)
    temp_counter = 0
    
    new_pin = exported_pin
    
    for pairs in key_list:
        if pairs == "name":
            new_pin["name"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "pin":
            new_pin["pin"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "freq":
            new_pin["freq"]= value_list[temp_counter]
            temp_counter += 1
    
    saved_pwms.append(new_pin)
    print(saved_pwms)
        
def close(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument!\nMissing pin name for closing.")
        return
    exported_pin = {"name":"","freq":"","pin":""}
    for myPWM in saved_pwms:
        if cmd_arr[3] == myPWM["name"]:
            exported_pin["name"] = myPWM["name"]
            exported_pin["freq"] = myPWM["freq"]
            exported_pin["pin"] = myPWM["pin"]
    if exported_pin["name"] == "":
        print(f'There is no PWM pin named "{cmd_arr[3]}"!')
        return
    pwm_t = PWM(Pin(int(exported_pin["pin"],Pin.OUT)),freq=int(exported_pin["freq"]))
    pwm_t.deinit()
    print(f'"{exported_pin["name"]}" closed.')

def delete(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument!\nMissing pin name for deleting.")
        return
    
    exported_pin = {"name":"","freq":"","pin":""}
    for myPWM in saved_pwms:
        if cmd_arr[3] == myPWM["name"]:
            exported_pin["name"] = myPWM["name"]
            exported_pin["freq"] = myPWM["freq"]
            exported_pin["pin"] = myPWM["pin"]
            saved_pwms.remove(myPWM)
            print(saved_pwms)
    if exported_pin["name"] == "":
        print(f'There is no PWM pin named "{cmd_arr[3]}"!')
        return