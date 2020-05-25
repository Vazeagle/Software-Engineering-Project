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

####classes#####

cur_Boardofeducation="Γεώργιος Δημητρόπουλος"

######################


###frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")
application_Frame=Frame(all_Frame, bg="floral white")
pending_applic_Frame=Frame(all_Frame, bg="floral white") #aitiseis
statement_Frame2=Frame(all_Frame, bg="floral white")#pendingaitiseis
statement_Frame3=Frame(all_Frame, bg="floral white")#theseis
statement_Frame4=Frame(all_Frame, bg="floral white")#dhmiourgia
Panhellenic_Frame=Frame(all_Frame, bg="floral white")#panellhnies
panexams_program_Frame=Frame(all_Frame, bg="floral white")
department_Frame=Frame(all_Frame, bg="floral white")#programma
department_submit_Frame=Frame(all_Frame, bg="floral white")#eksetastiko kentro
statement_Frame8=Frame(all_Frame, bg="floral white") #vathmologites
statement_Frame9=Frame(all_Frame, bg="floral white") #apodoxi aporripsi 
statement_Frame10=Frame(all_Frame, bg="floral white") #epeksergasia
statement_Frame11=Frame(all_Frame, bg="floral white") #provlimata
statement_Frame12=Frame(all_Frame, bg="floral white") #eksodos

folder_path_form = StringVar()#(ypovoli programmatos)
folder_path_ID = StringVar()#(label_Statement1_all_mt9l_left)
folder_path_form.set("")
folder_path_ID.set("")


def datetime_initialise(): #### χρειάζεται για το drop down menu στο ui δηλωση συμμετοχης
    i=0
    global month_options
    global date_options
    global year_options

    while (i<=12):  #month
        if(i==0):
            month_options.insert(0,"-")
        else:
            month_options.append(i)
        i=i+1

    i=0
    while (i<=31):  #date
        if(i==0):
            date_options.insert(0,"-")
        else:
            date_options.append(i)
        i=i+1

    now = datetime.now() ##current
    current_year=int(now.year)
    start_year=current_year-100
    i=current_year-16   #-16 επειδη ειναι το μιν για επιλογη κατευθυνσης κλπ  για να βαλει αρχικα μια - στην λιστα
    while (i>=start_year):  #year 
        if(i==current_year-16  ):
            year_options.insert(0,"-")
        else:
            year_options.append(i)
        i=i-1


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
    butttonNext1 = Button(label_l_down, text="Αιτήσεις", command=lambda: raiseNdrop_frame(application_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1.pack(side=TOP,pady=2,ipady=5)
    butttonNext2 = Button(label_l_down, text="Θέσεις Τμημάτων", command=lambda: raiseNdrop_frame(department_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2.pack(side=TOP,pady=2,ipady=5)
    butttonNext3 = Button(label_l_down, text="Πανελλήνιες", command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
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

    # -------------------------------First Frame END, Start of ΑΙΤΗΣΕΙΣ------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    application_all=Label(application_Frame,bg="floral white")

    application_all_top = Label(application_all, bg="floral white")
    application_at_top = Label(application_all_top, text="Αιτήσεις:",  bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    application_all_mid =  Label(application_all, bg="floral white")
    application_am_top = Label(application_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="black")
    application_am_bot = Label(application_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    application_all_mid_top= Label(application_all, bg="floral white")

    btn_application_list = Button(application_am_bot, text="Εκκρεμείς Αιτήσεις", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_application_history = Button(application_am_bot, text="Ιστορικό Αιτήσεων", command=lambda: raiseNdrop_frame(application_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    
    application_all.pack(side=TOP,expand=1,fill=BOTH)

    application_all.pack(side = TOP, fill=BOTH, expand=1)
    application_all_top.pack(side = TOP, fill=X, ipady=50)
    application_at_top.pack(side = TOP)
    application_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    application_am_top.pack(side = TOP)
    application_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    btn_application_list.pack(side = TOP,pady=80)
    btn_application_history.pack(side = TOP,pady=100)

    # -------------------------------ΑΙΤΗΣΕΙΣ END, Start of ΕΚΡΕΜΜΕΙΣ ΑΙΤΗΣΕΙΣ--------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    
    pending_applic_all = Label(pending_applic_Frame, bg="floral white")
    pending_applic_a_top = Label(pending_applic_all, bg="floral white")
    pending_applic_at_top = Label(pending_applic_a_top, bg="floral white", text="Εκκρεμείς Αιτήσεις",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    pending_applic_at_bottom = Label(pending_applic_a_top, bg="floral white")
    pending_applic_a_bottom = Label(pending_applic_at_bottom, bg="floral white")



    btn2_return_program = Button(pending_applic_a_bottom, text="Επιστροφή", command=lambda: raiseNdrop_frame(application_Frame,previous_frame), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)

    pending_applic_all.pack(side=TOP,fill=BOTH, expand=1)
    pending_applic_a_top.pack(side=TOP,fill=BOTH, expand=1)
    pending_applic_at_top.pack(side=TOP)
    pending_applic_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    pending_applic_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)
    btn2_return_program.pack(side=RIGHT)




    # -------------------------------ΕΚΚΡΕΜΕΙΣ ΑΙΤΗΣΕΙΣ END, Start of ΘΕΣΕΙΣ ΤΜΗΜΑΤΩΝ-------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    department_all=Label(department_Frame,bg="floral white")

    department_all_top = Label(department_all, bg="floral white")
    department_at_top = Label(department_all_top, text="Θέσεις Τμημάτων:",  bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    department_all_mid =  Label(department_all, bg="floral white")
    department_am_top = Label(department_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="black")
    department_am_bot = Label(department_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    #department_all_mid_top= Label(department_all, bg="floral white")

    btn_department_submit = Button(department_am_bot, text="Υποβολή Ημερομηνίας", command=lambda: raiseNdrop_frame(department_submit_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_department_history = Button(department_am_bot, text="Τελικές Θέσεις Τμημάτων", command=lambda: raiseNdrop_frame(department_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    department_all.pack(side=TOP,expand=1,fill=BOTH)

    department_all.pack(side = TOP, fill=BOTH, expand=1)
    department_all_top.pack(side = TOP, fill=X, ipady=50)
    department_at_top.pack(side = TOP)
    department_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    department_am_top.pack(side = TOP)
    department_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    btn_department_submit.pack(side = TOP,pady=80)
    btn_department_history.pack(side = TOP,pady=100)



    # -------------------------------ΘΕΣΕΙΣ ΤΜΗΜΑΤΩΝ END, Start of ΗΜΕΡΟΜΗΝΙΑ---------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------


    department_sumbit= Label(department_submit_Frame, bg="floral white")
    department_sumbit_a_top = Label(department_sumbit, bg="floral white")
    department_sumbit_at_top = Label(department_sumbit_a_top, bg="floral white", text="Ημερομηνία Υποβολής",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    department_sumbit_at_bottom = Label(department_sumbit_a_top, bg="floral white")
    #department_sumbit_a_bottom = Label(department_sumbit_at_bottom, bg="floral white")

    
    #department_date = Label(department_sumbit, text="Ημερομηνία Υποβολής: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    department_date_l = Label(department_sumbit_at_bottom, bg="floral white")
    department_date_2 = Label(department_sumbit_at_bottom, bg="floral white")
    department_date_3 = Label(department_sumbit_at_bottom, bg="floral white")
    department_date_space1 = Label(department_sumbit_at_bottom, text="/",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    department_date_space2 = Label(department_sumbit_at_bottom, text="/",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
  
    
    datetime_initialise()#kalesma synarthshs gia hmeromhnia

    date_val = StringVar(department_date_l)
    date_val.set(date_options[0])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    date_choice = OptionMenu(department_date_l, date_val, *date_options)
    date_choice.config(bg="snow")

    month_val = StringVar(department_date_2)
    month_val.set(month_options[0])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    month_choice = OptionMenu(department_date_2, month_val, *month_options)
    month_choice.config(bg="snow")


    year_val = StringVar(department_date_3)
    year_val.set(year_options[0])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    year_choice = OptionMenu(department_date_3, year_val, *year_options)
    year_choice.config(bg="snow")

    department_sumbit.pack(side=TOP,expand=1,fill=BOTH)
    department_sumbit_a_top.pack(side=TOP,fill=BOTH, expand=1)
    department_sumbit_at_top.pack(side=TOP)
    department_sumbit_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    
    #department_date.pack(side=LEFT)
    department_date_l.pack(side=LEFT)
    department_date_space1.pack(side=LEFT)
    department_date_2.pack(side=LEFT)
    department_date_space2.pack(side=LEFT)
    department_date_3.pack(side=LEFT)
    date_choice.pack(side=LEFT)
    month_choice.pack(side=LEFT)
    year_choice.pack(side=LEFT)



    # -------------------------------ΗΜΕΡΟΜΗΝΙΑ END, Start of ΠΑΝΕΛΛΗΝΙΕΣ-------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    panexams_all=Label(Panhellenic_Frame,bg="floral white")

    panexams_all_top = Label(panexams_all, bg="floral white")
    panexams_at_top = Label(panexams_all_top, text="Πανελλήνιες Εξετάσεις:",  bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    panexams_all_mid =  Label(panexams_all, bg="floral white")
    panexams_am_top = Label(panexams_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="black")
    panexams_am_bot = Label(panexams_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    panexams_all_mid_top= Label(panexams_all, bg="floral white")

    btn_exams_program = Button(panexams_am_bot, text="Πρόγραμμα Πανελληνίων Εξετάσεων", command=lambda: raiseNdrop_frame(panexams_program_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_grade_center = Button(panexams_am_bot, text="Υποβολή Βαθμολογικών Κέντρων", command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_grader = Button(panexams_am_bot, text="Υποβολή Βαθμολογητών", command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    panexams_all.pack(side=TOP,expand=1,fill=BOTH)

    panexams_all.pack(side = TOP, fill=BOTH, expand=1)
    panexams_all_top.pack(side = TOP, fill=X, ipady=50)
    panexams_at_top.pack(side = TOP)
    panexams_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    panexams_am_top.pack(side = TOP)
    panexams_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    btn_exams_program.pack(side = TOP,pady=80)
    btn_grade_center.pack(side = TOP,pady=100)
    btn_grader.pack(side = TOP)

    # -------------------------------ΠΑΝΕΛΛΗΝΙΕΣ END, Start of ΠΡΟΓΡΑΜΜΑ ΠΑΝΕΛΛΗΝΙΩΝ------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    #school_exams_program_Frame
    label_panexams_all = Label(panexams_program_Frame, bg="floral white")
    label_panexams_a_top = Label(label_panexams_all, bg="floral white")
    label_panexams_at_top = Label(label_panexams_a_top, bg="floral white", text="Πρόγραμμα Πανελλήνιων Εξεταστικής ",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    label_panexams_at_bottom = Label(label_panexams_a_top, bg="floral white")
    label_panexams_a_bottom = Label(label_panexams_at_bottom, bg="floral white")

    btn2_return_program = Button(label_panexams_a_bottom, text="Επιστροφή", command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)


    #sos sos zisis input data στο calendar για ημερομηνια εξετασης ενδοσχολικων

    ############## CALENDAR################
    cal_panexams = Calendar(label_panexams_at_bottom, selectmode='none')
    date = cal_panexams.datetime.today() + cal_panexams.timedelta(days=2)
    cal_panexams.calevent_create(date, 'Hello World', 'message')
    cal_panexams.calevent_create(date, 'Reminder 2', 'reminder')
    cal_panexams.calevent_create(date + cal_panexams.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal_panexams.calevent_create(date + cal_panexams.timedelta(days=3), 'Message', 'message')

    cal_panexams.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')

    #pack()
    cal_panexams.pack(fill="both", expand=1)
    ttk.Label(label_panexams_at_bottom, text="Hover over the events.").pack()

    label_panexams_all.pack(side=TOP,fill=BOTH, expand=1)
    label_panexams_a_top.pack(side=TOP,fill=BOTH, expand=1)
    label_panexams_at_top.pack(side=TOP)
    label_panexams_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    label_panexams_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)
    btn2_return_program.pack(side=RIGHT)


##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()

main()

