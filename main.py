import gooz_engine
import dev.gooz_thread
import os
import json
from system.config import find_value

username = find_value('system/username')
password = find_value('system/password')

login_flag = True
"""
print("Welcome to GoozOS")
usr = input("Username: ")
if usr == username:
    paswd = input("Password: ")
    if paswd == password:
        login_flag = True
    else:
        print("Wrong Password")
else:
    print("User not found")
"""  
while(login_flag):
    print(username+"@RPi_Pico:",end="")
    print(os.getcwd(),end=" ")
    msg = input(">> ")
    cmd_list = gooz_engine.command_analyzator(msg)
    if not cmd_list == KeyError:
        gooz_engine.add_run_commands(cmd_list)
        gooz_engine.history.append(cmd_list)
    
        if cmd_list[0] == "shutdown":
            os.chdir("/")
            print("System will be shutdown")
            dev.gooz_thread.exit_flag = 1
            break