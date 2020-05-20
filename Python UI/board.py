import os, sys
from Classes import *
from Classes import Lesson,Orientation,Direction,Department,Student,School
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from TkTreectrl import *
import TkTreectrl as treectrl
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry
none="none" # προσωρινο για μεταβαση σε frames
previous_frame="previous_frame"
frame_counter=0
init_pass=0

#Initialisation
getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])
main_window = Tk()
main_window.geometry(resolution) ###########################################resolution
main_window.title("Parmenidis")
main_window.configure()
main_window.state("zoomed")

load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)

frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")

def main():
    label_left = Label(menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames
    label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    label_ruu_up = Label(label_right, text="Καλώς ήρθατε!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Calibri", 24, "bold"))

    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext0.pack(side=TOP,pady=2,ipady=5)
    butttonNext1 = Button(label_l_down, text="Αιτήσεις", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1.pack(side=TOP,pady=2,ipady=5)
    butttonNext2 = Button(label_l_down, text="Θέσεις Τμημάτων", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2.pack(side=TOP,pady=2,ipady=5)
    butttonNext3 = Button(label_l_down, text="Πανελλήνιες", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext3.pack(side=TOP,pady=2,ipady=5)
    butttonNext4 = Button(label_l_down, text="Προβλήματα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext4.pack(side=TOP,pady=2,ipady=5)
    butttonNext4 = Button(label_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext4.pack(side=TOP,pady=2,ipady=5)
    

    label_left.pack(side=TOP)
    
    label_l_up.pack(side=TOP)#PARMENIDIS LOGO
    label_l_down.pack(side=BOTTOM)#CONTAINS BUTTONS
    label_right.pack(side=RIGHT)
    label_ruu_up.pack(side=TOP)

    raiseNdrop_frame(all_Frame,none)
    raiseNdrop_frame(menu_Frame,none)
    raiseNdrop_frame(intro_Frame,none)
    main_window.mainloop()

def raiseNdrop_frame(frameUp,frameDown):
    global frame_counter
    global init_pass #flag to see if menu frame has appeared (0 is  no, 1 is yes)
    global frame_temp #απλα οριζω οτι το frame temp εινια τυπου frame γιατι αλλιως προβλημα στο forget γτ το διαβάζει ως string
    #print(frameDown)

    if(frameDown!="none"):
        if(frameDown=="previous_frame"):#forget previous frame
            frame_counter=0
            #print("going to delete frame: ",frame_temp)
            frame_temp.pack_forget()    
        else:
            frameDown.pack_forget()
    
    if(frame_counter==0 and init_pass==1 ):   #frame to close (memory)
        temp2=0
        frame_counter=1
        frame_temp=frameUp
        #print("memory",frame_temp)
    
 

    if(frameUp==menu_Frame):
        frameUp.tkraise()
        frameUp.pack(side=LEFT, fill=Y)
        init_pass=1
    else:
        frameUp.tkraise()
        frameUp.pack(expand=1,fill=BOTH)   
        
    
    #print("temp2=",temp2)    
    #print("fcount",frame_counter)
    #print("passmenu",init_pass)
def ExitApp():
    MsgBox = messagebox.askquestion('Έξοδος Εφαρμογής!', 'Είστε σίγουροι ότι θέλετε να αποσυνδεθείτε από το σύστημα Παρμενίδης ;', icon='warning')
    if MsgBox == 'yes':
        main_window.destroy()
    else:
        messagebox.showinfo('Επιστροφή', 'Θα επιστραφείτε στην προηγούμενη σας οθόνη !') 
main()