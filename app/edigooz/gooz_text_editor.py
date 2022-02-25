lines = []
flash_text = ""
text = ""
saved_text = ""
saved_pages_name = []
saved_texts = []
def text_editor():
    saved_text = ""
    while(1):
        msg = input("")
        if msg == "t_exit":
            break
        elif msg == "t_saved":
            name_input = input("Save as ? -> ")
            edit_text()
            text_save(name_input)
        lines.append(msg)
    
def edit_text():
    global text
    global lines
    for line in lines:
        text += line
        text += "\n"
        
def text_save(name):
    saved_text = text
    saved_texts.append(saved_text)
    saved_pages_name.append(name)

def clean_text():
    global saved_pages_name
    global saved_text
    global saved_texts
    saved_text = ""
    saved_pages_name.clear()
    saved_texts.clear()
    print("Edigooz files are deleted from Ram")

def show_pages():
    for i in saved_pages_name:
        print(i)

def cat_text(cmd_arr):
    page_counter = 0
    for i in range(0,len(saved_pages_name)):
        if cmd_arr[2] == saved_pages_name[i]:
            print(saved_texts[i])
            page_counter += 1
    if page_counter == 0:
        print("This page not found !!")

def save_text_flash(name):
    global saved_pages_name
    global flash_text
    global saved_texts
    name_txt = "app/edigooz/notes/"+name+".txt"
    for i in range(0,len(saved_pages_name)):
        if name == saved_pages_name[i]:
            flash_text = saved_texts[i]
    with open(name_txt,'w',encoding='utf-8') as f:
        f.write(flash_text)
        f.close()
    print(name,".txt has saved to flash memory")
  
