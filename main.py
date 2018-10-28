import tkinter as tk
import webbrowser
from tkinter.ttk import *
from tkinter.constants import *


def transfer():
    i = entry.get()
    i = i.replace("點", ".")
    print(i)
    webbrowser.open(i)


root = tk.Tk()
root.geometry("640x480")
root.title("霸社開車網址轉換器")

entry = tk.StringVar()
Entry(root,  textvariable=entry, ).pack(pady=100)
Button(root, text="開車", command=transfer).pack()

if __name__ == "__main__":
    entry.set("輸入霸社style網址")
    root.mainloop()