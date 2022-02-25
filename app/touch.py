import os
def create(name,path=os.getcwd(),_type=".txt"):
    name_txt = path+name+_type
    with open(name_txt,'w',encoding='utf-8') as f:
        f.write("")
        f.close()

def input_create(name,path=os.getcwd(),_type=".txt",data=""):
    name_txt = path+name+_type
    with open(name_txt,'w',encoding='utf-8') as f:
        f.write(data)
        f.close()