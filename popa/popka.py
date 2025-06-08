import tkinter as tk

win = tk.Tk()
win.geometry("600x600")
win.title("lol")

# btn1 = tk.Button(win,text="hello 1")
# btn2 = tk.Button(win,text="hello 2")
# btn3 = tk.Button(win,text="popka")
# btn4 = tk.Button(win,text="shopka")
#
# btn1.grid(row=0,column=0)
# btn2.grid(row=2,column=0,columnspan=2,stick="we")
# btn3.grid(row=0,column=1,)
# btn4.grid(row=0,column=2,rowspan=3,stick="ns")

for i in range(5):
    for j in range(2):
        tk.Button(win,text=f"popki {i} {j}").grid(row=i,column=j,)

win.mainloop()