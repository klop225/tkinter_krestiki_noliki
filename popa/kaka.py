import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = vod.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    vod["state"] = tk.NORMAL
    vod.delete(0, "end")
    vod.insert(0, value + digit)
    vod["state"] = tk.DISABLED


def add_operation(operation):
    value = vod.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    elif "+" in value or '-' in value or "*" in value or "/" in value:
        calculate()
        value = vod.get()
    vod["state"] = tk.NORMAL
    vod.delete(0, "end")
    vod.insert(0, value + operation)
    vod["state"] = tk.DISABLED


def calculate():
    value = vod.get()
    if value[-1] in "+-/*":
        value = value + value[:-1]
    vod["state"] = tk.NORMAL
    vod.delete(0, "end")
    try:
        vod.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("внимание", "ток цифры")
        vod.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo("внимание", "на ноль не делим")
        vod.insert(0, 0)
    vod["state"] = tk.DISABLED


def clear():
    vod["state"] = tk.NORMAL
    vod.delete(0, "end")
    vod.insert(0, "0")
    vod["state"] = tk.DISABLED


def make_digit(digit):
    return tk.Button(win, text=digit, bd=5, command=lambda: add_digit(digit))


def make_operation(operation):
    return tk.Button(win, text=operation, bd=5, fg="red", \
                     command=lambda: add_operation(operation))


def make_ravno(operation):
    return tk.Button(win, text=operation, bd=5, fg="red", \
                     command=calculate)


def make_del(operation):
    return tk.Button(win, text=operation, bd=5, fg="red", \
                     command=clear)


def preess_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-/*":
        add_operation(event.char)
    elif event.char == '\r':
        calculate()


win = tk.Tk()
win.geometry("240x280")
win["bg"] = "blue"
win.title("калькулятор")

win.bind("<Key>", preess_key)

vod = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)
vod.insert(0, "0")
vod["state"] = tk.DISABLED
vod.grid(row=0, column=0, columnspan=4, stick="we", padx=5, pady=5)

make_digit("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

make_operation("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation("/").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation("*").grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_ravno("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_del("c").grid(row=4, column=1, stick="wens", padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
