from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pyautogui
from datetime import datetime

getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])

window = Tk()

window.title("Parmenides")
window.geometry(resolution)

lbl_logo = Label(window, text="ΠΑΡΜΕΝΙΔΗΣ", font=("Verdana", 30))
lbl_logo.pack( side=TOP )

lblUsr = Label(window, text="Username:", font=("Verdana", 15))
lblUsr.pack( side=TOP )

txtUsr = Entry(window, width=15)
txtUsr.pack( side=TOP )
txtUsr.focus()

lblPass = Label(window, text="Password:", font=("Verdana", 15))
lblPass.pack( side=TOP )

txtPass = Entry(window, width=15)
txtPass.pack( side=TOP )

btn = Button(window, text="Log in", font=("Verdana", 15), fg="blue")
btn.pack( side=TOP )

window.mainloop()
