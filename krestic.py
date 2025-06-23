import tkinter as tk
from tkinter.constants import DISABLED


def block_b():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def b_winn():
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        block_b()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        block_b()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        block_b()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        block_b()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        block_b()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        block_b()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        block_b()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" or b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        block_b()


def b_clicked(b):
    global clicked
    if b["text"]==" " and clicked == True:
        b["text"] = "X"
        clicked = False
        b["state"] = tk.DISABLED
        b.config(bg="blue")
        b_winn()

    else:
        b["text"]==" " and clicked == False
        b["text"] = "O"
        clicked = True
        b["state"] = tk.DISABLED
        b.config(bg="green")
        b_winn()

clicked = True

win = tk.Tk()
win.geometry("510x550")
win.title("lol")

b1 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b1))
b2 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b2))
b3 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b3))
b4 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b4))
b5 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b5))
b6 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b6))
b7 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b7))
b8 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b8))
b9 = tk.Button(win,text=" ",height=5,width=10,font=("Helvetica",20),command=lambda : b_clicked(b9))

b1.grid(row=0,column=0,stick="wens")
b2.grid(row=0,column=1,stick="wens")
b3.grid(row=0,column=2,stick="wens")
b4.grid(row=1,column=0,stick="wens")
b5.grid(row=1,column=1,stick="wens")
b6.grid(row=1,column=2,stick="wens")
b7.grid(row=2,column=0,stick="wens")
b8.grid(row=2,column=1,stick="wens")
b9.grid(row=2,column=2,stick="wens")

win.mainloop()
