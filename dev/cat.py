import os
def read(path):
    try:
        f = open(path,'r',encoding='utf-8')
        print(f.read())
        f.close()
    except:
        print("File does not exist.")
    
