import tkinter as tk

def counter():
    global count
    count += "x"
    btn1["text"] = f"{count}"

count = 0

root = tk.Tk()
root.title("menu")
root.geometry('600x600')
root.resizable(width=False, height=False)

btn1 = tk.Button(root,text=f"{count}",
                      bg ="red",
                      command=counter)

btn1.pack()
root.mainloop()