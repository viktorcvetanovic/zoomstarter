import tkinter as tk
from util.sysconfig import *
import zoom
clicked=None
add_name=None
add_value=None

def open_gui():
    global clicked
    global add_name
    global add_name

    data=zoom.get_data()
    list=getList(data)
    window = tk.Tk()
    window.title('Zoom starter')
    window.geometry("500x500")
    greeting = tk.Label(text="ZOOM STARTER")
    greeting.config(width=50)
    greeting.config(font=("Courier", 15))
    greeting.pack()

    message_add= tk.Label(text="Add new link for your script")
    message_add.place(x=180,y=100)
    textBox=tk.Text(window, height=1, width=10)
    textBox.place(x=50,y=150)
    textBox2=tk.Text(window, height=1, width=30)
    textBox2.place(x=150,y=150)

    button_add = tk.Button(
        text="Add",
        width=10,
        height=3,
        bg="blue",
        fg="yellow",
        command=add,  
    )
    button_add.place(x=200,y=200)

    clicked=tk.StringVar()
    clicked.set(list[0])
    w = tk.OptionMenu(window,clicked,*list)
    w.place(x=200,y=320)
    button_start = tk.Button(
        text="Start",
        width=10,
        height=3,
        bg="blue",
        fg="yellow",
        command=start,  
    )
    button_start.place(x=200,y=420)
    message= tk.Label(text="Start your zoom script")
    message.place(x=180,y=380)
    window.resizable(False, False)
    window.mainloop()
    

def start():
    execute_command("zoomstarter -s "+clicked.get()+" -df")

def add():
    execute_command("zoomstarter -a "+add_name+" "+add_value)    


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list    
  