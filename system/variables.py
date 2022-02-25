import gooz_engine
    
def export(cmd_arr):
    cmd_str = ' '.join(str(x) for x in cmd_arr)
    key = cmd_arr[1].split(':')[0]
    value = cmd_str[cmd_str.index(':')+1:]
    if not get_value(key) == KeyError:
        if ',' in value:
            delete_value(key)
            add_new_value(key,value)
        else:
            set_value(key,value)
    else:
        add_new_value(key,value)
        
def unset(cmd_arr):
    key = cmd_arr[1]
    if delete_value(key):
        print(f"{key} successfully deleted.")
    else:
        print(f"There is no variable named '{key}' !")

def run_command_list(com_arr):
    for com in com_arr:
        run_command(com)
        
def run_command(com):
    cmd_list = gooz_basic.command_analyzator(com)
    if not cmd_list == KeyError:
        gooz_basic.add_run_commands(cmd_list)
        gooz_basic.history.append(cmd_list)
    else:
        print("KeyError")

def delete_value(key):
    found = False
    lines=[]
    in_block = False
    is_deleting_block = False
    
    if key[0] == '$':
        key = key[1:]
    with open('system/variables.txt') as var_file:
        for line in var_file:
            if in_block:
                if not is_deleting_block:
                    lines.append(line)
                if line.rstrip() == '*/':
                    in_block = False
            else:
                var = line.rstrip().split(':')
                var_key = var[0]
                var_value = var[1]
                if var_key == key:
                    found = True
                    is_deleting_block = True
                else:
                    is_deleting_block = False
                    lines.append(line)
                if var_value == '/*':
                    in_block =True
    var_file = open("system/variables.txt", "w")
    for line in lines:
        var_file.write(line)
    var_file.close()
    return found

def get_value(key):
    found = False
    value = []
    in_block = False
    
    if key[0] == '$':
        key = key[1:]
    with open('system/variables.txt') as var_file:
        for line in var_file:
            if in_block:
                if line.rstrip() == '*/':
                    in_block = False
                    if found:
                        break
                elif found:
                    value.append(line.rstrip())
            else:
                var = line.rstrip().split(':')
                var_key = var[0]
                var_value = var[1]
                if var_key == key:
                    found = True
                if var_value == '/*':
                    in_block = True
                elif found == True:
                    value = var_value
                    break
    if found:
        if type(value) == str:
            return value
        else:
            return ','.join(str(x) for x in value)
    else:
        return KeyError                   
        
def set_value(key,value):
    lines = []
    if key[0] == '$':
        key = key[1:]
    with open('system/variables.txt') as var_file:
        for line in var_file:
            var = line.rstrip().split(':')
            if key == var[0]:
                var[1] = value
                line = var[0]+':'+var[1]+'\n'
            lines.append(line)
    var_file = open("system/variables.txt", "w")
    for line in lines:
        var_file.write(line)
    var_file.close()
    
def add_new_value(key,value):
    lines = []
    if key[0] == '$':
        key = key[1:]
    with open('system/variables.txt') as var_file:
        for i in var_file:
            pass
        if ',' in value:
            var_file.write(key+':/*\n')
            value = value.split(',')
            for val in value:
                var_file.write(val+'\n')
            var_file.write('*/\n')
        else:
            line = key+':'+value+'\n'
            var_file.write(line)    
def env():
    with open('system/variables.txt') as var_file:
        print("------")
        for line in var_file:
            print(line.rstrip())
    print("------")
    
def change_parameters(command):
    while '$' in command:
        param = command[command.index('$'):]
        if ' ' in param:
            param = param[:param.index(' ')]
            if ',' in param:
                param = param[:param.index(',')]
        command = command.split(param)
        param = get_value(param)
        if param == KeyError:
            return KeyError
        command = param.join(str(x) for x in command)
    return command