from machine import Pin, SoftI2C
import time
import _thread
import utime
import dev.gooz_thread

exiting_i2c_flag = 0

#I2C Library
key = ""
value = ""
key_list = []
value_list = []
registered_key = []
registered_value = []
i2c_dic = []
saved_i2cs = []

# pin var i2c -name=(asd) -scl=(123) -sda=(123) -freq=(123)
def register(cmd_arr):
    global key
    global value
    global key_list
    key_list.clear()
    global value_list
    value_list.clear()
    global registered_key
    global registered_value
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
    i2c_name = ""
    i2c_scl_pin = ""
    i2c_sda_pin = ""
    i2c_freq = "400000"
        
    for pairs in key_list:
        if pairs == "name":
            i2c_name = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "scl":
            i2c_scl_pin = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "sda":
            i2c_sda_pin = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "freq":
            i2c_freq = value_list[temp_counter]
            temp_counter += 1
    
    #Saving
    temp = {}
    temp["name"] = i2c_name
    temp["scl"] = i2c_scl_pin
    temp["sda"] = i2c_sda_pin
    temp["freq"] = i2c_freq
    saved_i2cs.append(temp)
    
    print(saved_i2cs)
   

"""
#not necessary
def i2c_dic_converter():
    global i2c_dic
    counter = 0
    temp = {"name": "asd","scl": "asd","sda": "asd", "freq": "400000"}
    for link in registered_key:
        for i in range(0,len(link)):
            if link[i] == "name":
                temp["name"] = registered_value[counter][i]
            elif link[i] == "scl":
                temp["scl"] = registered_value[counter][i]
            elif link[i] == "sda":
                temp["sda"] = registered_value[counter][i]
            elif link[i] == "freq":
                temp["freq"] = registered_value[counter][i]
        counter += 1
        i2c_dic.append(temp)
        temp = {"name": "asd","scl": "asd","sda": "asd", "freq": "400000"}"""
        
# pin i2c show
def show_registered_i2c():
    global saved_i2cs
    print(saved_i2cs)

#pin i2c write "address" "tx_data"
def write(cmd_arr):
    for i2cs in saved_i2cs:
        if cmd_arr[3] == i2cs["name"]:
            i2c_name = i2cs["name"]
            i2c_scl_pin = i2cs["scl"]
            i2c_sda_pin = i2cs["sda"]
            i2c_freg= i2cs["freq"]
            
            i2c_t = SoftI2C(scl = Pin(int(i2c_scl_pin)), sda = Pin(int(i2c_sda_pin)), freq = int(i2c_freq))
            address = cmd_arr[4]
            txData = cmd_arr[5]
            i2c.write(address ,txData)
            time.sleep(0.1)

def listen_thread_i2c(i2c_name,i2c_scl_pin,i2c_sda_pin,i2c_freg,address):
    i2c_t = SoftI2C(scl = Pin(int(i2c_scl_pin)), sda = Pin(int(i2c_sda_pin)), freq = int(i2c_freq))
    global exiting_i2c_flag
    while True:
        rxData = bytes()
        utime.sleep(1)
        while i2c_t.any() > 0:
            rxData += i2c_t.readfrom(address, 1)
        print(rxData.decode('utf-8'))
        if exiting_i2c_flag == 1:
            break
    return 0
# pin i2c listen "address"
def listen(cmd_arr):
    global exiting_i2c_flag
    if cmd_arr[3] == "stop":
        exiting_i2c_flag = 1
        return exiting_i2c_flag
    for i2cs in saved_i2cs:
        if cmd_arr[3] == i2cs["name"]:
            i2c_name = i2cs["name"]
            i2c_scl_pin = i2cs["scl"]
            i2c_sda_pin = i2cs["sda"]
            i2c_freg= i2cs["freq"]
            
            address = cmd_arr[4]
            
            _thread.start_new_thread(listen_thread_i2c,(i2c_name,i2c_scl_pin,i2c_sda_pin,i2c_freg,address))
# pin i2c p2p "address" "tx_data"

def update(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument(s)\nWhat will be updated?")
        return

    exported_pin = {"name":"","scl":"","sda":"","freq":""}
    for myi2c in saved_i2cs:
        if myi2c["name"] == cmd_arr[3]:
            exported_pin["name"] = myi2c["name"]
            exported_pin["scl"] = myi2c["scl"]
            exported_pin["sda"] = myi2c["sda"]
            exported_pin["freq"] = myi2c["freq"]
        saved_i2cs.remove(myi2c)

    if exported_pin["name"] == "":
        print(f'There is no i2c pin named "{cmd_arr[3]}!"')
        return
    
    ey = ""
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
        elif pairs == "scl":
            new_pin["scl"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "sda":
            new_pin["sda"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "freq":
            new_pin["freq"] = value_list[temp_counter]
            temp_counter += 1
    
    saved_i2cs.append(new_pin)
    print(saved_i2cs)

def p2p(cmd_arr):
    for i2cs in saved_i2cs:
        if cmd_arr[3] == i2cs["name"]:
            i2c_name = i2cs["name"]
            i2c_scl_pin = i2cs["scl"]
            i2c_sda_pin = i2cs["sda"]
            i2c_freg= i2cs["freq"]
            i2c_t = SoftI2C(scl = Pin(int(i2c_scl_pin)), sda = Pin(int(i2c_sda_pin)), freq = int(i2c_freq))
                        
            address = cmd_arr[4]
            txData = cmd_arr[5]
            i2c_t.write(address, txData)
            time.sleep(0.1)
            rxData = bytes()
            while i2c_t.any() > 0:
                rxData += i2c_t.read(adress,1)
            print(rxData.decode('utf-8'))
            
# pin i2c del "name"
def i2c_delete(cmd_arr):
    global saved_i2cs
    counter = 0
    
    for i2cs in saved_i2cs:
        if i2cs["name"] == cmd_arr[3]:
            print("removed")
            del saved_i2cs[counter]
        counter+=1
                
                


