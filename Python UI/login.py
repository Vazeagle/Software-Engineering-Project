import os, sys
from Classes import *
from Classes import Lesson,Orientation,Direction,Department,Student,School
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
#from TkTreectrl import *
#import TkTreectrl as treectrl
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry
none="none" # προσωρινο για μεταβαση σε frames
previous_frame="previous_frame"
frame_counter=0
init_pass=0

def ExitApp():
    MsgBox = messagebox.askquestion('Έξοδος Εφαρμογής!', 'Είστε σίγουροι ότι θέλετε να αποσυνδεθείτε από το σύστημα Παρμενίδης ;', icon='warning')
    if MsgBox == 'yes':
        main_window.destroy()
    else:
        messagebox.showinfo('Επιστροφή', 'Θα επιστραφείτε στην προηγούμενη σας οθόνη !') 

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



#Initialisation
getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])
main_window = Tk()
main_window.geometry(resolution) ###########################################resolution
main_window.title("Parmenidis")
main_window.configure()
main_window.state("zoomed")
month_options=[]
date_options=[]
year_options=[]

    
load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)



###frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")
application_Frame=Frame(all_Frame, bg="floral white")
pending_applic_Frame=Frame(all_Frame, bg="floral white") #aitiseis
applic_verify_Frame=Frame(all_Frame, bg="floral white")#pendingaitiseis
department_application_Frame=Frame(all_Frame, bg="floral white")#dhlwsh thesewn
statement_Frame4=Frame(all_Frame, bg="floral white")#dhmiourgia
page_Frame=Frame(all_Frame, bg="floral white")#panellhnies
page_edit_Frame=Frame(all_Frame, bg="floral white")
capacity_Frame=Frame(all_Frame, bg="floral white")#programma
capacity_submit_Frame=Frame(all_Frame, bg="floral white")#eksetastiko kentro
graderslist_frame=Frame(all_Frame, bg="floral white") #vathmologites
acceptdeny_frame=Frame(all_Frame, bg="floral white") #apodoxi aporripsi 
processing_frame=Frame(all_Frame, bg="floral white") #epeksergasia
problems_frame=Frame(all_Frame, bg="floral white") #provlimata
exit_frame=Frame(all_Frame, bg="floral white") #eksodos


def main():
    
    login_all=Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")
    
    label_top = Label(login_all, borderwidth=1, highlightthickness=0,bg="floral white")  # kalos orisate+ to eniaio susthma klp
    label_pic = Label(label_top, image=render2, borderwidth=1, highlightthickness=0, bg="floral white")
    label_parmen = Label(label_top, text="ΣΥΣΤΗΜΑ ΠΑΡΜΕΝΙΔΗΣ\n", borderwidth=0,highlightthickness=0, bg="floral white", font=("Times New Roman (Times)", 24, "bold"))
    label_top3 = Label(login_all,bg="white", borderwidth=2, highlightthickness=2, relief="groove")

    
    login_usr = Label(label_top3, bg="white")
    login_usr1 = Label(login_usr, text="Όνομα Χρήστη:",  bg="white",font=("Times New Roman (Times)", 16, "bold"),fg="black")
    login_usr2 = Text(login_usr, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    
    login_passw = Label(label_top3, bg="white")
    login_passw1 = Label(login_passw, text="Κωδικός Πρόσβασης:",  bg="white",font=("Times New Roman (Times)", 16, "bold"),fg="black")
    login_passw2 = Text(login_passw, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))

    label_buttons = Label(label_top3, bg="floral white")
    btn_acccept = Button(label_buttons, text="Σύνδεση", bg="green3",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)
    btn_exit = Button(label_buttons, text="Έξοδος", command=lambda: ExitApp(), bg="gray",font=("Calibri", 14, "bold"),height=1 ,width=12)


    login_all.pack(side = TOP, fill=BOTH, expand=1)


    label_top.pack(side=TOP,fill=X,expand=1)
    label_pic.pack(side=TOP)
    label_parmen.pack(side=TOP)
    label_top3.pack(side=TOP,fill=Y,expand=1)

    
    login_usr.pack(side=TOP)
    login_usr1.pack(side = LEFT, padx=10)
    login_usr2.pack(side = LEFT, padx=10)
    
    login_passw.pack(side=TOP)
    login_passw1.pack(side = LEFT, padx=10)
    login_passw2.pack(side = LEFT, padx=10)

    label_buttons.pack(side=TOP)
    btn_acccept.pack(side = LEFT, padx=10)
    btn_exit.pack(side = LEFT, padx=10)


    raiseNdrop_frame(all_Frame,none)
    raiseNdrop_frame(menu_Frame,none)
    raiseNdrop_frame(intro_Frame,none)

    
    

##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()

main()

