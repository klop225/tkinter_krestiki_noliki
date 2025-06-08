import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("empty")

def del_entry():
    name.delete(0,"end")

def submit():
    print(name.get())
    print(password.get())
    del_entry()
    password.delete(0,"end")

win = tk.Tk()
win.geometry("600x600")
win.title("lol")

tk.Label(win,text="Имя").grid(row=0,column=0,stick="w")
tk.Label(win,text="Пароль").grid(row=1,column=0,stick="w")

name = tk.Entry(win)
password = tk.Entry(win,show="*")
name.grid(row=0,column=1)
password.grid(row=1,column=1)


tk.Button(win,text="shhhhhh",command=get_entry).grid(row=2,column=0,stick="we")
tk.Button(win,text="del",command=del_entry).grid(row=2,column=1,stick="we")
tk.Button(win,text="knopka",command=submit).grid(row=3,column=0,stick="we")
tk.Button(win,text="looool",command=lambda:name.insert(0,"hello"))\
    .grid(row=0,column=2,rowspan=4,stick="ns")

win.mainloop()