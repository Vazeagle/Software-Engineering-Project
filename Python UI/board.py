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

load3 = Image.open('user_blank.png')
load3 = load3.resize((102, 72), Image.ANTIALIAS)
render3 = ImageTk.PhotoImage(load3)

####classes#####

#cur_Admin="Γεώργιος Δημητρόπουλος"

######################


###frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")
application_Frame=Frame(all_Frame, bg="floral white")
pending_applic_Frame=Frame(all_Frame, bg="floral white") #aitiseis
applic_verify_Frame=Frame(all_Frame, bg="floral white")#pendingaitiseis
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
    label_rddrl_up = Label(label_rddr_left, text="Γεώργιος Δημητρόπουλος", borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="floral white")  # katastash

    descriptionText = Text(label_rul_right, height=8, bg="floral white", fg="gray44", borderwidth=0, highlightthickness=2,font=("Times New Roman (Times)", 12), width=55)
    descriptionText.insert(INSERT,"Ο Παρμενίδης ήταν αρχαίος έλληνας φιλόσοφος. Γεννήθηκε στην \nΕλέα της Μεγάλης Ελλάδας στα τέλη του 6ου αιώνα π.Χ., σε ένα \nπεριβάλλον επηρεασμένο από τις απόψεις του Πυθαγόρα και του Ξενοφάνη. Ο Παρμενίδης υποστήριξε ότι η πολλαπότητα των \nυπάρχοντων πραγμάτων, οι μεταβαλλόμενες μορφές και η κίνηση τους δεν είναι παρά μια εμφάνιση μιας ενιαίας αιώνιας \nπραγματικότητα (<<Όν>>), οδηγώντας έτσι στην παρμενίδια αρχή \nότι <<όλα είναι ένα>>.")
    descriptionText.config(state=DISABLED)#to be un editable

    
    label_left = Label(menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames
    
    #label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    #label_ruu_up = Label(label_right, text="Καλώς ήρθατε!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Calibri", 24, "bold"))

    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1 = Button(label_l_down, text="Αιτήσεις", command=lambda: raiseNdrop_frame(application_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2 = Button(label_l_down, text="Θέσεις Τμημάτων", command=lambda: raiseNdrop_frame(department_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext3 = Button(label_l_down, text="Πανελλήνιες", command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext4 = Button(label_l_down, text="Προβλήματα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext5 = Button(label_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

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
    
    descriptionText.pack()
    
    butttonNext0.pack(side=TOP,pady=2,ipady=5)
    butttonNext1.pack(side=TOP,pady=2,ipady=5)
    butttonNext2.pack(side=TOP,pady=2,ipady=5)
    butttonNext3.pack(side=TOP,pady=2,ipady=5)
    butttonNext4.pack(side=TOP,pady=2,ipady=5)
    butttonNext5.pack(side=TOP,pady=2,ipady=5)

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

    btn_applic_1 = Button(pending_applic_at_bottom, text="Σταυρόπουλος Παναγιώτης", command=lambda: raiseNdrop_frame(applic_verify_Frame,previous_frame), bg="floral white",height = 2, width = 35,font=("Calibri", 14, "bold"), fg= "dodger blue")
    btn_applic_2 = Button(pending_applic_at_bottom, text="Βαζαίος Στυλιανός", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="floral white",height = 2, width = 35,font=("Calibri", 14, "bold"), fg= "dodger blue")
    btn_applic_3 = Button(pending_applic_at_bottom, text="Σβίγγου Αναστασία", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="floral white",height = 2, width = 35,font=("Calibri", 14, "bold"), fg= "dodger blue")
    btn_applic_4 = Button(pending_applic_at_bottom, text="Στεργιοπούλου Φωτεινή", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="floral white",height = 2, width = 35,font=("Calibri", 14, "bold"), fg= "dodger blue")
    btn_applic_5 = Button(pending_applic_at_bottom, text="Τράμπαρης Ζήσιμος-Στυλιανός", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="floral white",height = 2, width = 35,font=("Calibri", 14, "bold"), fg= "dodger blue")

    btn2_return_program = Button(pending_applic_a_bottom, text="Επιστροφή", command=lambda: raiseNdrop_frame(application_Frame,previous_frame), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)

    pending_applic_all.pack(side=TOP,fill=BOTH, expand=1)
    pending_applic_a_top.pack(side=TOP,fill=BOTH, expand=1)
    pending_applic_at_top.pack(side=TOP)
    pending_applic_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    pending_applic_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)
    
    btn_applic_1.pack(side=TOP)
    btn_applic_2.pack(side=TOP)
    btn_applic_3.pack(side=TOP)
    btn_applic_4.pack(side=TOP)
    btn_applic_5.pack(side=TOP)
    
    btn2_return_program.pack(side=RIGHT)

    # -------------------------------ΕΚΚΡΕΜΕΙΣ ΑΙΤΗΣΕΙΣ END, Start of ΣΕΛΙΔΑ ΑΙΤΗΣΕΙΣ-------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    applic_verify_all = Label(applic_verify_Frame, bg="floral white")
    applic_verify_a_top = Label(applic_verify_all, bg="floral white")
    applic_verify_at_top = Label(applic_verify_a_top, bg="floral white", text="Εκκρεμείς Αιτήσεις",font=("Times New Roman (Times)", 36, "bold"),fg="black")
    applic_verify_at_mid = Label(applic_verify_a_top, bg="floral white")
    applic_verify_a_bottom = Label(applic_verify_at_mid, bg="floral white")

    applic_verify_name = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_name1 = Label(applic_verify_name, text="Όνομα: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_name2 = Label(applic_verify_name, text="Παναγιώτης", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    applic_verify_surname = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_surname1 = Label(applic_verify_surname, text="Επώνυμο: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_surname2 = Label(applic_verify_surname, text="Σταυρόπουλος", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    applic_verify_birthdate = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_birthdate1 = Label(applic_verify_birthdate, text="Ημερομηνία Γέννησης: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_birthdate2 = Label(applic_verify_birthdate, text="15/06/1998", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    
    applic_verify_Fname = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_Fname1 = Label(applic_verify_Fname, text="Όνομα Πατρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_Fname2 = Label(applic_verify_Fname, text="Κωνστανίνος", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    applic_verify_Fsurname = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_Fsurname1 = Label(applic_verify_Fsurname, text="Επώνυμο Πατρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_Fsurname2 = Label(applic_verify_Fsurname, text="Σταυρόπουλος", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    
    applic_verify_Mname = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_Mname1 = Label(applic_verify_Mname, text="Όνομα Μητρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_Mname2 = Label(applic_verify_Mname, text="Αναστασία", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    applic_verify_Msurname = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_Msurname1 = Label(applic_verify_Msurname, text="Επώνυμο Πατρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_Msurname2 = Label(applic_verify_Msurname, text="Παλαιοθοδώρου", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))  

    applic_verify_Apply = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_Apply1 = Label(applic_verify_Apply, text="Αίτηση Συμμετοχής: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_Apply2 = Label(applic_verify_Apply, text="dilosi.pdf", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    applic_verify_ID = Label(applic_verify_at_mid, bg="floral white")
    applic_verify_ID1 = Label(applic_verify_ID, text="Αστυνομική Ταυτότητα: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    applic_verify_ID2 = Label(applic_verify_ID, text="tautot.pdf", bg="WHITE", height=1, width=40, fg="dodger blue", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    buttton_accept = Button(applic_verify_a_bottom, text="Αποδοχή", command=lambda: accept(), bg="green",font=("Calibri", 14, "bold"),height=1 ,width=12)
    buttton_deny = Button(applic_verify_a_bottom, text="Απόρριψη", command=lambda: deny(), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)
    buttton_back_to_statement = Button(applic_verify_a_bottom, text="Επιστροφή", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="gray",font=("Calibri", 14, "bold"),height=1 ,width=12)
    
    #ΠΡΟΧΕΙΡΗ ΤΟΠΟΘΕΤΗΣΗ ΣΥΝΑΡΤΗΣΗΣ----------------------------------------------------------
    def accept():
        msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να κάνετε αποδεχτείτε αυτή τη δήλωση;',icon='warning')
        if msg_confirmation == 'yes':
            messagebox.showinfo('Oλοκλήρωση', 'Η δήλωση έγινε δεκτή με επιτυχία!')
            raiseNdrop_frame(pending_applic_Frame,previous_frame) ###ενδεχομενως να βαλουμε εδω να διαγραφεται η αιτηση και να πηγαινει στο ιστορικο
        else:
            raiseNdrop_frame(applic_verify_Frame,previous_frame)

    def deny():
        msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να κάνετε απορρίψετε αυτή τη δήλωση;',icon='warning')
        if msg_confirmation == 'yes':
            messagebox.showinfo('Oλοκλήρωση', 'Η δήλωση απορρίφθηκε με επιτυχία!')
            raiseNdrop_frame(pending_applic_Frame,previous_frame)
        else:
            raiseNdrop_frame(applic_verify_Frame,previous_frame)

    
    applic_verify_all.pack(side=TOP,fill=BOTH, expand=1)
    applic_verify_a_top.pack(side=TOP,fill=BOTH, expand=1)
    applic_verify_at_top.pack(side=TOP)
    applic_verify_at_mid.pack(side=TOP, fill=BOTH, expand=1, pady=100)
    applic_verify_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)

    applic_verify_name.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_name1.pack(side=LEFT,padx=10)
    applic_verify_name2.pack(side=LEFT)

    applic_verify_surname.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_surname1.pack(side=LEFT,padx=10)
    applic_verify_surname2.pack(side=LEFT)

    applic_verify_birthdate.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_birthdate1.pack(side=LEFT,padx=10)
    applic_verify_birthdate2.pack(side=LEFT)

    applic_verify_Fname.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_Fname1.pack(side=LEFT,padx=10)
    applic_verify_Fname2.pack(side=LEFT)

    applic_verify_Fsurname.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_Fsurname1.pack(side=LEFT,padx=10)
    applic_verify_Fsurname2.pack(side=LEFT)

    applic_verify_Mname.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_Mname1.pack(side=LEFT,padx=10)
    applic_verify_Mname2.pack(side=LEFT)

    applic_verify_Msurname.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_Msurname1.pack(side=LEFT,padx=10)
    applic_verify_Msurname2.pack(side=LEFT)

    applic_verify_Apply.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_Apply1.pack(side=LEFT,padx=10)
    applic_verify_Apply2.pack(side=LEFT)

    applic_verify_ID.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    applic_verify_ID1.pack(side=LEFT,padx=10)
    applic_verify_ID2.pack(side=LEFT)

    buttton_accept.pack(side=RIGHT,padx=25)
    buttton_deny.pack(side=RIGHT, padx=25)
    buttton_back_to_statement.pack(side=RIGHT)

    # -------------------------------ΣΕΛΙΔΑ ΑΙΤΗΣΕΙΣ END, Start of ΘΕΣΕΙΣ ΤΜΗΜΑΤΩΝ----------------------
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

    lbl_department_submit = Label(department_am_bot, text="Υποβολή Ημερομηνίας: 15/07/2020", bg="floral white",height = 2, width = 35,font=("Calibri", 25, "bold"))
    btn_department_editdate = Button(department_am_bot, text="Επεξεργασία Ημερομηνίας", command=lambda: date_edit(), bg="gray26",height = 2, width = 25,font=("Calibri", 14, "bold"))
    btn_department_history = Button(department_am_bot, text="Τελικές Θέσεις Τμημάτων", command=lambda: raiseNdrop_frame(department_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    def date_edit():
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

        department_date_l.pack(side=LEFT)
        department_date_space1.pack(side=LEFT)
        department_date_2.pack(side=LEFT)
        department_date_space2.pack(side=LEFT)
        department_date_3.pack(side=LEFT)
        date_choice.pack(side=LEFT)
        month_choice.pack(side=LEFT)
        year_choice.pack(side=LEFT)





    department_all.pack(side=TOP,expand=1,fill=BOTH)

    department_all.pack(side = TOP, fill=BOTH, expand=1)
    department_all_top.pack(side = TOP, fill=X, ipady=50)
    department_at_top.pack(side = TOP)
    department_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    department_am_top.pack(side = TOP)
    department_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    lbl_department_submit.pack(side = TOP)
    btn_department_editdate.pack(side = TOP,pady=80)
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

