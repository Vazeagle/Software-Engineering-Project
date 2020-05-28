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

load1 = Image.open('P1.png')
load1 = load1.resize((140, 160), Image.ANTIALIAS)
render1 = ImageTk.PhotoImage(load1)
    
load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)

load3 = Image.open('ceid.png')
#load3 = load3.resize((102, 72), Image.ANTIALIAS)
render3 = ImageTk.PhotoImage(load3)

####################################  DHLWSH
folder_path_list= StringVar()#label_graderslist
folder_path_list.set("")






####classes#####

#cur_Admin="Γεώργιος Δημητρόπουλος"

######################


###frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")
capacity_submit_Frame=Frame(all_Frame, bg="floral white") #theseis
dhmiourgia_Frame=Frame(all_Frame, bg="floral white")#dhmiourgia&epeksergasia
site_Frame=Frame(all_Frame, bg="floral white")#selidatmhmatos
problem_Frame=Frame(all_Frame, bg="floral white")#problems
exitt_frame=Frame(all_Frame, bg="floral white") #eksodos

folder_path_list = StringVar()#(ypovoli programmatos)
folder_path_list.set("")



def main():
    
    label_left = Label(menu_Frame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg="gray26",font=("Times New Roman (Times)", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, text="ΦΩΤΟΓΤΑΦΙΑ\n ΠΑΡΜΕΝΊΔΗΣ", borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    label_r_up = Label(label_right, borderwidth=1, highlightthickness=0, bg="floral white")  # panw meros me perilipsh kai hmerologio
    label_ru_up = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="floral white")  # kalos orisate+ to eniaio susthma klp
    label_ruu_up = Label(label_ru_up, text="Καλώς ήρθατε στον Παρμενίδη!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Times New Roman (Times)", 24, "bold"))
    label_ruu_down = Label(label_ru_up, text="Το ενιαίο σύστημα για τις Πανελλήνιες Εξετάσεις.\n", borderwidth=0,highlightthickness=0, bg="floral white", font=("Times New Roman (Times)", 18))

    # isws na 8elei up kai oxi left
    label_ru_left = Label(label_ru_up, borderwidth=1, highlightthickness=0,bg="floral white")  # foto parmenidi+ desription parmenidi
    label_rul_left = Label(label_ru_left, image=render1, borderwidth=1, highlightthickness=0,bg="floral white")  # foto parmenidi
    label_rul_right = Label(label_ru_left, borderwidth=1, highlightthickness=0,bg="floral white")  # Ο παρμενιδης ειναι bla bla

    label_ru_right = Label(label_ru_up, borderwidth=0, highlightthickness=1,bg="floral white")  # hmerologio gramma + hmerologio
    label_rur_up = Label(label_ru_right, text="Ημερολόγιο\n", borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18))  # hmerologio gramma
    label_rur_down = Label(label_ru_right, borderwidth=1, highlightthickness=0, bg="floral white")  # hmerologio

    label_r_down = Label(label_right, borderwidth=20, highlightthickness=0, relief="raised", bg="floral white")  # sunoptiko profil
    label_rd_up = Label(label_r_down, text=" Παρών χρήστης: ",relief="groove", borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))  # sunoptiko profil
    label_rd_down = Label(label_r_down, borderwidth=1, highlightthickness=0, bg="floral white")  # onoma xrhsth kai alla
    label_rdd_left = Label(label_rd_down,image=render3, borderwidth=0, highlightthickness=0, bg="floral white")  # eikona user
    label_rdd_right = Label(label_rd_down, borderwidth=1, highlightthickness=0,bg="floral white")  # onoma xrhsth status lukeio kai alla

    label_rddr_left = Label(label_rdd_right, borderwidth=1, highlightthickness=0,bg="floral white")  # onoma xrhsth kai status
    label_rddrl_up = Label(label_rddr_left, text="Τμήμα Μηχανικών Η/Υ και Πληροφορικής", borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="floral white")  # katastash
    label_rddrld_left = Label(label_rddrl_down, text="Ίδρυμα: ", borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 14))  # katastash text
    label_rddrld_right = Label(label_rddrl_down, text="Πανεπιστήμιο Πατρών", borderwidth=1, highlightthickness=1, relief="groove",bg="white",font=("Times New Roman (Times)", 14))  # input katastashs apo data base

    descriptionText = Text(label_rul_right, height=8, bg="floral white", fg="gray44", borderwidth=0, highlightthickness=2,font=("Times New Roman (Times)", 12), width=55)
    descriptionText.insert(INSERT,"Ο Παρμενίδης ήταν αρχαίος έλληνας φιλόσοφος. Γεννήθηκε στην \nΕλέα της Μεγάλης Ελλάδας στα τέλη του 6ου αιώνα π.Χ., σε ένα \nπεριβάλλον επηρεασμένο από τις απόψεις του Πυθαγόρα και του Ξενοφάνη. Ο Παρμενίδης υποστήριξε ότι η πολλαπότητα των \nυπάρχοντων πραγμάτων, οι μεταβαλλόμενες μορφές και η κίνηση τους δεν είναι παρά μια εμφάνιση μιας ενιαίας αιώνιας \nπραγματικότητα (<<Όν>>), οδηγώντας έτσι στην παρμενίδια αρχή \nότι <<όλα είναι ένα>>.")
    descriptionText.config(state=DISABLED)#to be un editable

    
    label_left = Label(menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames
    
    #label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    #label_ruu_up = Label(label_right, text="Καλώς ήρθατε!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Calibri", 24, "bold"))

    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1 = Button(label_l_down, text="Θέσεις Επιτυχόντων", command=lambda: raiseNdrop_frame(capacity_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2 = Button(label_l_down, text="Σελίδα Τμήματος", command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext3 = Button(label_l_down, text="Προβλήματα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext4 = Button(label_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    cal = Calendar(label_rur_down, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(label_rur_down, text="Hover over the events.").pack()
      

    label_left.pack(side=LEFT)
    label_l_up.pack(side=TOP)#PARMENIDIS LOGO
    label_l_down.pack(side=BOTTOM)#CONTAINS BUTTONS

    label_right.pack(side=TOP,fill=BOTH,expand=1)#SOS SOS SOS SOS SOS SOS SOS SOS SOS SOS salmon eswteriko dexi prepei na to anrikatastisw me init_label
    label_r_up.pack(side=TOP,fill=BOTH,expand=1)#kalos hr8ate+eniaio susthma+perilhpsh+calendar
    label_ru_up.pack(side=TOP)
    label_ruu_up.pack(side=TOP)
    label_ruu_down.pack(side=TOP)

    # isws na 8elei up kai oxi left
    label_ru_left.pack(side=LEFT)
    label_rul_left.pack(side=LEFT)#eikona pamenidi
    label_rul_right.pack(side=LEFT)#peilhpsh

    label_ru_right.pack(side=LEFT)
    label_rur_up.pack(side=TOP)#hmerologio gramma
    label_rur_down.pack(side=TOP,padx=50,ipady=40,ipadx=40)#,ipadx=40,ipady=30)#calendar

    label_r_down.pack(side=BOTTOM,fill=X,expand=1)##SYNOPTIKA
    label_rd_up.pack(side=TOP)#SYNOPTIKA
    label_rd_down.pack(side=TOP,pady=10)#FOTO KATASTASH KLP
    label_rdd_left.pack(side=LEFT)
    label_rdd_right.pack(side=RIGHT)

    label_rddr_left.pack(side=LEFT)
    label_rddrl_up.pack(side=TOP,)
    label_rddrl_down.pack(side=BOTTOM)
    label_rddrld_left.pack(side=LEFT)
    label_rddrld_right.pack(side=RIGHT)
    
    descriptionText.pack()
    
    butttonNext0.pack(side=TOP,pady=2,ipady=5)
    butttonNext1.pack(side=TOP,pady=2,ipady=5)
    butttonNext2.pack(side=TOP,pady=2,ipady=5)
    butttonNext3.pack(side=TOP,pady=2,ipady=5)
    butttonNext4.pack(side=TOP,pady=2,ipady=5)


    raiseNdrop_frame(all_Frame,none)
    raiseNdrop_frame(menu_Frame,none)
    raiseNdrop_frame(intro_Frame,none)




    ############################# SINARTISI############

    def browse_list():  #filedialog documentation  για λεπτομερειες 
    # Allow user to select a file and store it in global variable folder_path_form  και ασφάλεια από λάθος αρχείο
        global folder_path_list
        filename_form = filedialog.askopenfilename()
        file_type2=filename_form.split(".")
        if(file_type2[-1]=="xlsx" ): #αν το τελευταιο στοιχειο της λιστας είναι το string xls
            folder_path_list.set(filename_form)
            msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να υποβάλετε αυτό το αρχείο;',icon='warning')
            if msg_confirmation == 'yes':
                messagebox.showinfo('Oλοκλήρωση', 'Επιτυχής υποβολή αρχείου!')
                raiseNdrop_frame(Panhellenic_Frame,previous_frame) 
            else:
                browse_list()

        else:
            msg_error_form = messagebox.showerror('Πρόβλημα Αρχείου!', 'Παρακαλώ επιλέξτε ένα αρχείο τύπου xls που να περιέχει τα στοιχεία της λίστας σας', icon='warning')
            filename_ID=""



    # -------------------------------First Frame END, Start of ΘΕΣΕΙΣ ΕΠΙΤΥΧΟΝΤΩΝ-----------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------


    capacity_all=Label(capacity_Frame,bg="floral white")

    capacity_all_top = Label(capacity_all, bg="floral white")
    capacity_at_top = Label(capacity_all_top, text="Θέσεις Επιτυχόντων:",  bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    capacity_all_mid =  Label(capacity_all, bg="floral white")
    capacity_am_top = Label(capacity_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="black")
    capacity_am_bot = Label(capacity_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    
    btn_capacity_editdate = Button(capacity_am_bot, text="Υποβολή Θέσεων", command=lambda: raiseNdrop_frame(capacity_submit_Frame,previous_frame), bg="gray26",height = 2, width = 25,font=("Calibri", 14, "bold"))
    btn_capacity_history = Button(capacity_am_bot, text="Τελικά Αποτελέσματα", command=lambda: raiseNdrop_frame(capacity_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    capacity_all.pack(side=TOP,expand=1,fill=BOTH)

    capacity_all.pack(side = TOP, fill=BOTH, expand=1)
    capacity_all_top.pack(side = TOP, fill=X, ipady=50)
    capacity_at_top.pack(side = TOP)
    capacity_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    capacity_am_top.pack(side = TOP)
    capacity_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    btn_capacity_editdate.pack(side = TOP,pady=80)
    btn_capacity_history.pack(side = TOP,pady=100)



    # -------------------------------ΘΕΣΕΙΣ ΕΠΙΤΥΧΟΝΤΩΝ END, Start of ΥΠΟΒΟΛΗ---------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------


    capacity_submit_all= Label(capacity_submit_Frame, bg="floral white")
    capacity_submit_a_top = Label(capacity_submit_all, bg="floral white")
    capacity_submit_at_top = Label(capacity_submit_a_top, bg="floral white", text="Υποβολή Θέσεων",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    capacity_submit_all_mid =  Label(capacity_submit_all, bg="floral white")
    capacity_submit_am_top = Label(capacity_submit_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="black")
    capacity_submit_am_bot = Label(capacity_submit_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    

    capacity_date = Label(capacity_submit_all, text="Ημερομηνία Υποβολής: 15/07/2020",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    capacity_date_check = Label(capacity_submit_am_bot, text="Βάσει ημερομηνίας, η υποβολή είναι:",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    capacity_date_check1 = Label(capacity_submit_am_bot, text="ΕΦΙΚΤΗ", borderwidth=1, highlightthickness=1, relief="groove",bg="green3",font=("Times New Roman (Times)", 14))
    capacity_submit_check = Label(capacity_submit_am_bot, text="Στο σύστημα υπάρχει αίτηση;",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    capacity_submit_check1 = Label(capacity_submit_am_bot, text="ΟΧΙ", borderwidth=1, highlightthickness=1, relief="groove",bg="red",font=("Times New Roman (Times)", 14))
    btn_new_submission = Button(capacity_submit_am_bot, text="Νεα Αίτηση", command=lambda: raiseNdrop_frame(capacity_submit_Frame,previous_frame), bg="gray26",height = 2, width = 25,font=("Calibri", 14, "bold"))
  

    capacity_submit_all.pack(side=TOP,expand=1,fill=BOTH)
    capacity_submit_a_top.pack(side=TOP,fill=BOTH, expand=1)
    capacity_submit_at_top.pack(side=TOP)
    capacity_submit_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=25)
    capacity_submit_am_top.pack(side = TOP)
    capacity_submit_am_bot.pack(side = LEFT, fill=BOTH, expand=1)
    
    capacity_date.pack(side=TOP)
    capacity_date_check.pack(side=TOP)
    capacity_date_check1.pack(side=TOP)
    capacity_submit_check.pack(side=TOP)
    capacity_submit_check1.pack(side=TOP)
    
    btn_new_submission.pack(side=TOP)



    # -------------------------------ΥΠΟΒΟΛΗ END, Start of ΝΕΑ ΑΙΤΗΣΗ-----------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    





    # -------------------------------ΝΕΑ ΑΙΤΗΣΗ END, Start of _______-----------------------------------
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
    btn_grader = Button(panexams_am_bot, text="Υποβολή Βαθμολογητών", command=lambda: browse_list(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

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


    #graderslist_frame
    label_graderslist_all= Label(panexams_program_Frame,bg="floral white")
    label_graderslist_a_top = Label(label_graderslist_all, bg="floral white")
    label_graderslist_at_top = Label(label_graderslist_a_top, bg="floral white", text=" Υποβολή Λίστας Βαθμολογητών ",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    label_graderslist_at_bottom = Label(label_graderslist_a_top, bg="floral white")
    label_graderslist_a_bottom = Label(label_graderslist_at_bottom, bg="floral white")

    btn3_return_list = Button(label_graderslist_a_bottom, text="Επιστροφή", command=lambda: browse_list(), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)







    #pack()
    cal_panexams.pack(fill="both", expand=1)
    ttk.Label(label_panexams_at_bottom, text="Hover over the events.").pack()

    label_panexams_all.pack(side=TOP,fill=BOTH, expand=1)
    label_panexams_a_top.pack(side=TOP,fill=BOTH, expand=1)
    label_panexams_at_top.pack(side=TOP)
    label_panexams_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    label_panexams_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)
    label_graderslist_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    label_graderslist_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)
    btn2_return_program.pack(side=RIGHT)
    btn3_return_list.pack(side=RIGHT)

##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()

main()

