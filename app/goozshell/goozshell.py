import gooz_engine
import dev.gooz_thread
import os
import time

def delay(second):
    time.sleep(second)

def cleaner(cmd):
    cleaner_flag = False
    for i in cmd:
        if i == "\\":
            cleaner_flag == True
            del i
        elif cleaner_flag == True:
            del i
    return cmd

def run(cmd):
    msg = cmd
    cmd_list = gooz_basic.command_analyzator(msg)
    gooz_basic.add_run_commands(cmd_list)
    
def example_shell():
    run("pin var gpio -name=(myPin) -pin=(25) -type=(out)")
    run("pin gpio write myPin HIGH")
    delay(1)
    run("pin gpio write myPin LOW")
    delay(1)
    run("pin gpio write myPin HIGH")

def read(path):
    f = open(path,'r',encoding='utf-8')
    commands = f.readlines()
    f.close()
    return commands

def for_loop(infos):
    cmds = infos[3]
    for i in range(int(infos[0]),int(infos[1]),int(infos[2])):
        for a in cmds:
            run(a)

def main(path):
    cmds = read(path)
    infos = []
    command_temp = []
    shell_flag = False
    shell_kind = ""
    for cmd1 in cmds:
        #cmd1 = cleaner(cmd1)
        cmd1 = cmd1[:len(cmd1)-2]
        if cmd1 == "--stop":
            break
        elif shell_flag == True and shell_kind == "for":
            if cmd1 == "}":
                shell_flag = False
                shell_kind = ""
                infos.append(command_temp)
                for_loop(infos)
                infos = []
                command_temp = []
            else:
                command_temp.append(cmd1)
        elif cmd1[0:3] == "for":
            total_flag = 0
            temp = ""
            temp2 = ""
            for i in cmd1:
                if i == "(":
                    total_flag = 1
                    continue
                elif i == ")":
                    total_flag = 0
                elif total_flag == 1:
                    temp += i
            for i in temp:
                if i == ",":
                    infos.append(temp2)
                    temp2 = ""
                else:    
                    temp2 += i
            infos.append(temp2)
            temp2 = ""
            shell_flag = True
            shell_kind = "for"
            
        else:
            run(cmd1)