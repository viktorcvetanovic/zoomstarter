from ast import arg
import tkinter as tk
from zoom.util.sysconfig import *
from zoom.classes.impl import Worker
from zoom.classes import Argument

def update_list():
    list=[]
    data=get_data()
    for key in data.keys():
        list.append(key)
    return list

def get_data():
    try:
        with open(get_config(0), 'r') as f:
            data=json.load(f)
            return data
    except EnvironmentError:
        raise FileNotFoundError("Please add config.json in this path: " + get_config(0))
  

window = tk.Tk()
worker=Worker(None)
list=update_list()
options = tk.StringVar(window)
options.set(list[0])
w = tk.OptionMenu(window,options,*list)
textBox=tk.Text(window, height=1, width=10)
textBox2=tk.Text(window, height=1, width=30)


def open_gui():
    
    window.title('Zoom starter')
    window.geometry("500x500")
    greeting = tk.Label(text="ZOOM STARTER")
    greeting.config(width=50)
    greeting.config(font=("Courier", 15))
    greeting.pack()

    message_add= tk.Label(text="Add new link for your script")
    message_add.place(x=180,y=100)
    
    textBox.place(x=50,y=150)
    
    textBox2.place(x=150,y=150)

    button_add = tk.Button(
        text="Add",
        width=10,
        height=3,
        bg="blue",
        fg="yellow",
        command=add,  
    )
    button_add.place(x=100,y=200)
    button_remove = tk.Button(
        text="Remove",
        width=10,
        height=3,
        bg="blue",
        fg="yellow",
        command=remove,  
    )
    button_remove.place(x=300,y=200)

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
    argument=Argument("s",[options.get()])
    worker.start_link(argument=argument)
    
def add():
    name=textBox.get("1.0",'end-1c')
    value=textBox2.get("1.0",'end-1c')
    argument=Argument("a",[name,value])
    worker.add_link(argument=argument)
    update_dropdown()

def remove():
    name=textBox.get("1.0",'end-1c')
    argument=Argument("d",[name])
    worker.remove_link(argument=argument)
    update_dropdown()


def update_dropdown():
    list=update_list()
    options.set('')
    w['menu'].delete(0, 'end')

    for choice in list:
        w['menu'].add_command(label=choice, command=tk._setit(options, choice))