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

load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)

####classes#####

cur_Boardofeducation="Γεώργιος Δημητρόπουλος"

######################


###frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")
statement_Frame=Frame(all_Frame, bg="floral white")
statement_Frame1=Frame(all_Frame, bg="floral white") #aitiseis
statement_Frame2=Frame(all_Frame, bg="floral white")#pendingaitiseis
statement_Frame3=Frame(all_Frame, bg="floral white")#theseis
statement_Frame4=Frame(all_Frame, bg="floral white")#dhmiourgia
Panhellenic_Frame=Frame(all_Frame, bg="floral white")#panellhnies
statement_Frame6=Frame(all_Frame, bg="floral white")#programma
statement_Frame7=Frame(all_Frame, bg="floral white")#eksetastiko kentro
statement_Frame8=Frame(all_Frame, bg="floral white") #vathmologites
statement_Frame9=Frame(all_Frame, bg="floral white") #apodoxi aporripsi 
statement_Frame10=Frame(all_Frame, bg="floral white") #epeksergasia
statement_Frame11=Frame(all_Frame, bg="floral white") #provlimata
statement_Frame12=Frame(all_Frame, bg="floral white") #eksodos




def main():
    
    label_left = Label(menu_Frame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, text="ΦΩΤΟΓΤΑΦΙΑ\n ΠΑΡΜΕΝΊΔΗΣ", borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    label_r_up = Label(label_right, borderwidth=1, highlightthickness=0, bg="floral white")  # panw meros me perilipsh kai hmerologio
    label_ru_up = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="floral white")  # kalos orisate+ to eniaio susthma klp
    label_ruu_up = Label(label_ru_up, text="Καλώς ήρθατε στον Παρμενίδη!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Calibri", 24, "bold"))
    label_ruu_down = Label(label_ru_up, text="Το ενιαίο σύστημα για τις Πανελλήνιες Εξετάσεις.\n", borderwidth=0,highlightthickness=0, bg="floral white", font=("Calibri", 18))

    # isws na 8elei up kai oxi left
    label_ru_left = Label(label_ru_up, borderwidth=1, highlightthickness=0,bg="floral white")  # foto parmenidi+ desription parmenidi
    label_rul_left = Label(label_ru_left, borderwidth=1, highlightthickness=0,bg="floral white")  # foto parmenidi
    label_rul_right = Label(label_ru_left, borderwidth=1, highlightthickness=0,bg="floral white")  # Ο παρμενιδης ειναι bla bla

    label_ru_right = Label(label_ru_up, borderwidth=0, highlightthickness=1,bg="floral white")  # hmerologio gramma + hmerologio
    label_rur_up = Label(label_ru_right, text="Ημερολόγιο\n", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 18))  # hmerologio gramma
    label_rur_down = Label(label_ru_right, borderwidth=1, highlightthickness=0, bg="floral white")  # hmerologio

    label_r_down = Label(label_right, borderwidth=20, highlightthickness=0, relief="raised", bg="floral white")  # sunoptiko profil
    label_rd_up = Label(label_r_down, text=" Συνοπτικό προφίλ: ",relief="groove", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 18, "bold"))  # sunoptiko profil
    label_rd_down = Label(label_r_down, borderwidth=1, highlightthickness=0, bg="floral white")  # onoma xrhsth kai alla
    label_rdd_left = Label(label_rd_down, borderwidth=0, highlightthickness=0, bg="floral white")  # eikona user
    label_rdd_right = Label(label_rd_down, borderwidth=1, highlightthickness=0,bg="floral white")  # onoma xrhsth

    
    label_rddr_left = Label(label_rdd_right, borderwidth=1, highlightthickness=0,bg="floral white")  # onoma xrhsth kai anafora
    label_rddrl_up = Label(label_rddr_left, text="cur_Boardofeducation", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="floral white")  # anafora
    label_rddrld_left = Label(label_rddrl_down, text="Υπουργείο Παιδείας και Θρησκευμάτων ", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 14))  # anafora text


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
    

    label_left.pack(side=LEFT)

    

    label_l_up.pack(side=TOP)#PARMENIDIS LOGO
    label_l_down.pack(side=BOTTOM)#CONTAINS BUTTONS
    label_right.pack(side=RIGHT)
    label_ruu_up.pack(side=TOP)

    raiseNdrop_frame(all_Frame,none)
    raiseNdrop_frame(menu_Frame,none)
    raiseNdrop_frame(intro_Frame,none)

####################################statement_frame###############

    label_Statement_all = Label(statement_Frame, bg="floral white")
    label_Statement_all_top = Label(label_Statement_all, bg="floral white")
    label_Statement_all_t_top = Label(label_Statement_all_top, text="Πανελλήνιες", bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    label_Statement_all_t_down = Label(label_Statement_all_top, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="dodger blue")
    label_Statement_all_topd = Label(label_Statement_all,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")

    label_Statement_5a = Label(label_Statement_all_topd, bg="floral white")
    label_Statement_5a_left = Label(label_Statement_5a, bg="floral white")
    
    label_Statement_5b = Label(label_Statement_all_topd, bg="floral white")
    label_Statement_5b_left = Label(label_Statement_5b, bg="floral white")
   
    label_Statement_5c = Label(label_Statement_all_topd, bg="floral white")
    label_Statement_5c_left = Label(label_Statement_5c, bg="floral white")

    butttonStatementa = Button(label_Statement_5a_left, text="Πρόγραμμα Πανελληνίων", command=lambda: raiseNdrop_frame(statement_Frame1,previous_frame), bg="floral white",font=("Calibri", 16, "bold"),height = 2, width = 35)
    butttonStatementb = Button(label_Statement_5b_left, text="Υποβολή Βαθμολογικών Κέντρων", command=lambda: raiseNdrop_frame(statement_Frame2,previous_frame), bg="floral white",font=("Calibri", 16, "bold"),height = 2, width = 35)
    butttonStatementc = Button(label_Statement_5c_left, text="Υποβολή Λίστας Επιτηρητών", command=lambda: raiseNdrop_frame(statement_Frame3,previous_frame), bg="floral white",font=("Calibri", 16, "bold"),height = 2, width = 35)
    
    butttonStatementa.pack()
    butttonStatementb.pack()
    butttonStatementc.pack()






########################################################################################################

    labelboard=Label(Panhellenic_Frame,bg="floral white")

    labelboard1 = Label(labelboard, bg="floral white")
    labelboard2 = Label(labelboard, text="Υποβολή Λίστας: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    labelboard3 =  Label(labelboard, bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="blue")# η μεταβλητη εχει οριστει πανω απο την συναρτηση που καλειται browse_form
    #pdf selected from user browse

#browse_ID
    #buttton_browse_form = Button(labelboard2, text="Αναζήτηση", command=lambda:browse_form(), bg="red3",font=("Calibri", 14, "bold"))
    #buttton_confirm = Button(labelboard3, text="Επιβεβαίωση", bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)
    #buttton_back_to_statement = Button(labelboard3, text="Επιστροφή", command=lambda: raiseNdrop_frame(statement_Frame,previous_frame), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)


    labelboard.pack(side=TOP,expand=1,fill=BOTH)

    labelboard1.pack(side=TOP)
    labelboard2.pack(side=TOP)
    labelboard3.pack(side=TOP)


##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()



main()
