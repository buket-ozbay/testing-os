from machine import Pin
import time
import _thread
import utime
import dev.gooz_thread

saved_gpio = []
gpio_pin_list = [34,35,32,33,25,26,27,14,12,13,23,22,21,19,18,5,17,16,4,0,2,15]

def register(cmd_arr):

    try:
        key = ""
        value = ""
        key_list = []
        value_list = []
        registered_key = []
        registered_value = []
        temp = {"name":"","pin":"","type":"","mode":""}
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
        
        for pairs in key_list:
            if pairs == "name":
                temp["name"] = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "type":
                temp["type"] = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "mode":
                temp["mode"] = value_list[temp_counter]
                temp_counter += 1
            elif pairs == "pin":
                temp["pin"] = value_list[temp_counter]
                temp_counter += 1
        
        if temp["name"] == "" or temp["type"] == "" or temp["pin"] == "":
            print("Missing necessary argument(s)!\n<gpio_name>, <gpio_type> or <gpio_pin> is empty.")
            return
        
        isNameExist = False
        for myGPIO in saved_gpio:
            if myGPIO["name"] == temp["name"]:
                isNameExist = True
        if isNameExist:
            print(f'The pin named "{temp["name"]}" already exists')
            return

        if not int(temp["pin"]) in gpio_pin_list:
            print(f'The pin "{temp["pin"]}" can not be used as a GPIO')
            return
        
        """
        isPinGPIO = False
        for listcounter in gpio_pin_list:
            if listcounter == temp["pin"]:
                isPinGPIO = True
        if isPinGPIO == False:
            print("The pin" + temp["pin"] + "can not be used as a GPIO")
            return
        """
        #Saving
        saved_gpio.append(temp)
        
        print(saved_gpio)
    except:
        print("Unknown error while registering GPIO pin!")
        
def update(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument(s)\nWhat will be updated?")
        return
    
    exported_pin = {"name":"","pin":"","type":"","mode":""}
    for myGpio in saved_gpio:
        if myGpio["name"] == cmd_arr[3]:
            exported_pin["name"] = myGpio["name"]
            exported_pin["pin"] = myGpio["pin"]
            exported_pin["type"] = myGpio["type"]
            exported_pin["mode"] = myGpio["mode"]
            saved_gpio.remove(myGpio)
        
    if exported_pin["name"] == "":
        print(f'There is no GPIO pin named "{cmd_arr[3]}!"')
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
        elif pairs == "type":
            new_pin["type"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "mode":
            new_pin["mode"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "pin":
            new_pin["pin"] = value_list[temp_counter]
            temp_counter += 1
    
    if not int(new_pin["pin"]) in gpio_pin_list:
        print(f'The pin "{new_pin["pin"]}" can not be used as a GPIO')
        return
    
    saved_gpio.append(new_pin)
    print(saved_gpio)

def delete(cmd_arr):
    try:
        if not len(cmd_arr) > 3:
            print("Missing Argument!\nMissing pin name for deleting.")
            return
        
        exported_pin = {"name":"","pin":"","type":"","mode":""}
            
        for myGPIO in saved_gpio:
            if myGPIO["name"] == cmd_arr[3]:
                exported_pin["name"] = myGPIO["name"]
                exported_pin["pin"] = myGPIO["pin"]
                exported_pin["type"] = myGPIO["type"]
                exported_pin["mode"] = myGPIO["mode"]
                saved_gpio.remove(myGPIO)
                print(saved_gpio)
        if exported_pin["name"] == "":
            print('There is no ADC pin named '+'"'+cmd_arr[3]+'"')
    except:
        print("Unknown error while deleting GPIO pin!")
    
            
def write(cmd_arr):
    try:
        if not len(cmd_arr) > 4:
            print("Missing Argument!\nMissing pin name for writing.")
            return
        
        exported_pin ={"name":"","pin":"","type":"","mode":""}

        for myGPIO in saved_gpio:
            if myGPIO["name"] == cmd_arr[3]:
                exported_pin["name"] = myGPIO["name"]
                exported_pin["pin"] = myGPIO["pin"]
                exported_pin["type"] = myGPIO["type"]
                exported_pin["mode"] = myGPIO["mode"]
            
        if exported_pin["name"] == "":
            print('There is no GPIO pin named '+'"'+cmd_arr[3]+'"')
            return
        
        global type_pin
        global in_type_pin
        global gpio_t
        if exported_pin["type"] == "out":
            type_pin = Pin.OUT
        elif exported_pin["type"] == "in":
            type_pin = Pin.IN
        elif exported_pin["type"] == "alt":
            type_pin = Pin.ALT
        elif exported_pin["type"] == "opendrain":
            type_pin = Pin.OPEN_DRAIN
        elif exported_pin["type"] == "altopendrain":
            type_pin = Pin.ALT_OPEN_DRAIN
        if exported_pin["mode"] == "pullup":
            in_type_pin = Pin.PULL_UP
        elif exported_pin["mode"] == "pulldown":
            in_type_pin = Pin.PULL_DOWN
        try:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin,in_type_pin)
        except:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin)
        try:
            if cmd_arr[4] == "HIGH" or cmd_arr[4] == "1":
                gpio_t.value(1)
            elif cmd_arr[4] == "LOW" or cmd_arr[4] == "0":
                gpio_t.value(0)
        except:
            print("Your Pin:"+exported_pin["name"]+" didn't work")
    except:
        print("Unknown error while writing GPIO pin!")

def read(cmd_arr):
    try:
        if not len(cmd_arr) > 3:
            print("Missing Argument!\nMissing pin name for reading.")
            return
        
        exported_pin = {"name":"","pin":"","type":"","mode":""}
        
        for myGPIO in saved_gpio:
            if myGPIO["name"] == cmd_arr[3]:
                exported_pin["name"] = myGPIO["name"]
                exported_pin["pin"] = myGPIO["pin"]
                exported_pin["type"] = myGPIO["type"]
                exported_pin["mode"] = myGPIO["mode"]
        
        if exported_pin["name"] == "":
            print('There is no GPIO pin named '+'"'+cmd_arr[3]+'"')
            return

        global type_pin
        global in_type_pin
        global gpio_t
        if exported_pin["type"] == "out":
            type_pin = Pin.OUT
        elif exported_pin["type"] == "in":
            type_pin = Pin.IN
        elif exported_pin["type"] == "alt":
            type_pin = Pin.ALT
        elif exported_pin["type"] == "opendrain":
            type_pin = Pin.OPEN_DRAIN
        elif exported_pin["type"] == "altopendrain":
            type_pin = Pin.ALT_OPEN_DRAIN
        if exported_pin["mode"] == "pullup":
            in_type_pin = Pin.PULL_UP
        elif exported_pin["mode"] == "pulldown":
            in_type_pin = Pin.PULL_DOWN
        try:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin,in_type_pin)
        except:
            gpio_t = Pin(int(exported_pin["pin"]),type_pin)
        try:
            print(gpio_t.value())
        except:
            print("Your Pin:"+'"'+exported_pin["name"]+'"'+" didn't work")
    except:
        print("Unknown error while reading GPIO pin!")


