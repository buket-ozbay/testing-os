from machine import UART,Pin
import time
import _thread
import utime
import dev.gooz_thread
from system.config import find_value

exiting_uart_flag = 0

#UART Library
saved_uarts = []
def register(cmd_arr):
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
    temp = {"name":"","rx":"","tx":"","type":"","baudrate":""}
    temp["baudrate"] = find_value("uart/baudrate")
    
    for pairs in key_list:
        if pairs == "name":
            temp["name"] = value_list[temp_counter]
            temp_counter += 1
            """
        if pairs == "name":
            name_flag = 0
            print(value_list)
            while uart_name != value_list[temp_counter]:
                print("-----------------")
                for count in saved_uarts:
                    if saved_uarts[count]["name"] == value_list[temp_counter]:
                        name_flag = 1
                if name_flag == 0:
                    uart_name = value_list[temp_counter]
                    temp_counter += 1
                else:
                    print("This name is exist. Give another name for that pin.")
                    value_list[temp_counter] = input("Try another name > ")"""
        elif pairs == "baudrate":
            temp["baudrate"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "rx":
            temp["rx"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "tx":
            temp["tx"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "type":
            temp["type"] = value_list[temp_counter]
            temp_counter += 1
    
    if temp["name"] == "" or temp["type"] =="" or temp["rx"]=="" or temp["tx"] == "":
        print("Missing necessary argument(s)!\n<uart_name>, <uart_type>, <uart_rx> or <uart_tx> is empty.")
        return
        
    isNameExist =False
    for myUART in saved_uarts:
        if myUART["name"] == temp["name"]:
            isNameExist = True
    if isNameExist:
        print(f'The pin named "{temp["name"]}"" already exists!')
        return
        
    #Saving
    
    saved_uarts.append(temp)
    
    show_registered_uart()
    

"""
#not necessary
def uart_dic_converter():
    global uart_dic
    counter = 0
    temp = {"name": "asd","type": "asd","baudrate": "asd", "rx": "asd","tx": "asd"}
    for link in registered_key:
        for i in range(0,len(link)):
            if link[i] == "name":
                temp["name"] = registered_value[counter][i]
            elif link[i] == "baudrate":
                temp["baudrate"] = registered_value[counter][i]
            elif link[i] == "rx":
                temp["rx"] = registered_value[counter][i]
            elif link[i] == "tx":
                temp["tx"] = registered_value[counter][i]
            elif link[i] == "type":
                temp["type"] = registered_value[counter][i]
        counter += 1
        uart_dic.append(temp)
        temp = {"name": "asd","type": "asd","baudrate": "asd", "rx": "asd","tx": "asd"}"""
                
        
def show_registered_uart():
    print(saved_uarts)
    
def uart_delete(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument!\nMissing pin name for deleting.")
        return
        
    exported_pin ={"name":"","rx":"","tx":"","type":"","baudrate":""}
    for myUART in saved_uarts:
        if myUART["name"] == cmd_arr[3]:
            exported_pin["name"] = myUART["name"]
            exported_pin["rx"] = myUART["rx"]
            exported_pin["tx"] = myUART["tx"]
            exported_pin["baudrate"] = myUART["baudrate"]
            exported_pin["type"] = myUART["type"]
            saved_uarts.remove(myUART)
            show_registered_uart()
    if exported_pin["name"] == "":
        print('There is no UART pin named '+'"'+cmd_arr[3]+'"')

def update(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument!\nWhat will be updated?")
        return
    
    exported_pin ={"name":"","rx":"","tx":"","type":"","baudrate":""}
    for myUART in saved_uarts:
        if myUART["name"] == cmd_arr[3]:
            exported_pin["name"] = myUART["name"]
            exported_pin["rx"] = myUART["rx"]
            exported_pin["tx"] = myUART["tx"]
            exported_pin["baudrate"] = myUART["baudrate"]
            exported_pin["type"] = myUART["type"]
            saved_uarts.remove(myUART)

    if exported_pin["name"] == "":
        print(f'There is no UART pin named "{cmd_arr[3]}!"')
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
        elif pairs == "rx":
            new_pin["rx"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "tx":
            new_pin["tx"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "type":
            new_pin["type"] = value_list[temp_counter]
            temp_counter += 1
        elif pairs == "baudrate":
            new_pin["baudrate"] = value_list[temp_counter]
            temp_counter += 1
        
    saved_uarts.append(new_pin)
    print(saved_uarts)
            
def write(cmd_arr):
    if not len(cmd_arr) > 4:
        print("Missing Argument(s)!\nMissing pin name for writing.")
        return
    exported_pin ={"name":"","rx":"","tx":"","type":"","baudrate":""}
    
    for myUART in saved_uarts:
        if myUART["name"] == cmd_arr[3]:
            exported_pin["name"] = myUART["name"]
            exported_pin["rx"] = myUART["rx"]
            exported_pin["tx"] = myUART["tx"]
            exported_pin["baudrate"] = myUART["baudrate"]
            exported_pin["type"] = myUART["type"]
            
    if exported_pin["name"] == "":
        print(f'There is no UART pin named "{cmd_arr[3]}"!')
        return
        
    uart_t = UART(int(exported_pin["type"]),baudrate=int(exported_pin["baudrate"]),tx=int(exported_pin["tx"]),rx=int(exported_pin["rx"]))
    txData = cmd_arr[4]
    uart_t.write(txData)
    print(f'"{txData}" sent to "{exported_pin["name"]}"!')
    time.sleep(0.1)

def listen_thread(uart_type,uart_baudrate,uart_rx,uart_tx):
    uart_t = UART(int(uart_type),baudrate=int(uart_baudrate),tx=int(uart_tx),rx=int(uart_rx))
    global exiting_uart_flag
    while True:
        if exiting_uart_flag == 1:
            exiting_uart_flag = 0
            break
        rxData = bytes()
        while uart_t.any() > 0:
            rxData += uart_t.read(1)
        print(rxData.decode('utf-8'))
        utime.sleep(1)
    return 0
        

def listen(cmd_arr):
    global exiting_uart_flag
    if not len(cmd_arr)>3:
        print("Missing Argument(s)!\nMissing pin name for listening.")
        return
    if cmd_arr[3] == "stop":
        exiting_uart_flag = 1
        return exiting_uart_flag
    exported_pin ={"name":"","rx":"","tx":"","type":"","baudrate":""}
    
    for myUART in saved_uarts:
        if myUART["name"] == cmd_arr[3]:
            exported_pin["name"] = myUART["name"]
            exported_pin["rx"] = myUART["rx"]
            exported_pin["tx"] = myUART["tx"]
            exported_pin["baudrate"] = myUART["baudrate"]
            exported_pin["type"] = myUART["type"]
    if exported_pin["name"] == "":
        print(f'There is no UART pin named "{cmd_arr[3]}"!')
        return
    
    _thread.start_new_thread(listen_thread,(exported_pin["type"],exported_pin["baudrate"],exported_pin["rx"],exported_pin["tx"]))

def p2p(cmd_arr):
    for uarts in saved_uarts:
        if cmd_arr[3] == uarts["name"]:
            uart_name = uarts["name"]
            uart_type = uarts["type"]
            uart_baudrate = uarts["baudrate"]
            uart_rx = uarts["rx"]
            uart_tx = uarts["tx"]
            uart_t = UART(int(uart_type),baudrate=int(uart_baudrate),tx=int(uart_tx),rx=int(uart_rx))
            txData = cmd_arr[4]
            uart_t.write(txData)
            time.sleep(0.1)
            rxData = bytes()
            while uart_t.any() > 0:
                rxData += uart_t.read(1)
            print(rxData.decode('utf-8'))



