import os
import json

globaldata = {}

def find_value(path):
    path_list = path.split('/')
    config_file = open('system/config.gooz','r')
    data = json.loads(config_file.read())
    config_file.close()   
    for i in path_list:
        try:
            data = data[i]
        except KeyError:
            return KeyError
    return data 
        
def show_value(cmd_arr): #path format : "system/username"
    if not len(cmd_arr) > 2:
        print("Missing Argument(s)!")
        return
    path = ""
    data = find_value(cmd_arr[2])
    if data == KeyError:
        print(f'There is no key for "{path}"')
    else:
        print(data)

def register_value(cmd_arr):
    if not len(cmd_arr) > 3:
        print("Missing Argument(s)!")
        return
    path = cmd_arr[2]
    new_val = cmd_arr[3]
    path_list = path.split('/')
    
    data = find_value(path)
    if data == KeyError:
        print(f'There is no key for "{path}"')
        return
    elif type(data) == dict:
        print(f'The given path references a dictionary.')
        return
    
    config_file = open('system/config.gooz','r')
    global globaldata
    globaldata = json.loads(config_file.read())
    config_file.close()    
    
    code_str = "globaldata"
    for i in path_list:
        code_str += f"['{i}']"
    code_str+=f"='{new_val}'"
    exec(code_str)
    config_file = open('system/config.gooz','w',encoding="utf-8")
    json.dump(globaldata,config_file)
    config_file.close()
    print(f'The value which refers to "{path}" successfully registered as "{new_val}"')
    

