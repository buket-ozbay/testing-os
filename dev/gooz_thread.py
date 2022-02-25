import machine
import utime
import _thread

internal_led = machine.Pin(25,machine.Pin.OUT)
exit_flag = 0

def toggle():
    global exit_flag
    while True:
        internal_led.toggle()
        utime.sleep(1)
        if exit_flag == 1:
            print("Toggle App Closed")
            break
    internal_led.value(0)
    return 0

def listen_uart(uart_t):
    global exit_flag
    while True:
        rxData = bytes()
        utime.sleep(1)
        while uart_t.any() > 0:
            rxData += uart_t.read(1)
        print(rxData)
        if rxData != b'':
            print(rxData.decode('utf-8'))
        if exit_flag == 1 or rxData == b'close':
            print("Uart no more listen")
            break
    return 0

def print_t():
    global exit_flag
    while True:
        print("deneme")
        utime.sleep(1)
        if exit_flag == 1:
            break
    return 0

def start(cmd_arr):
    global exit_flag
    exit_flag = 0
    if cmd_arr[1] == "toggle":
        _thread.start_new_thread(toggle,())
    elif cmd_arr[1] == "print_t":
        _thread.start_new_thread(print_t,())
    
def stop():
    global exit_flag
    exit_flag = 1
"""    
print("->")
a = input("")
if a == "start":
    _thread.start_new_thread(toggle,())
elif a == "stop":
    _thread.exit()"""
"""
while True:
    a = input("->")
    if a == "start":
        _thread.start_new_thread(toggle,())
    elif a == "stop":
        exit_flag = 1
        break"""
    