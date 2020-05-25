#extra need yagmail from pip import

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry
import uuid
#import yagmail




#Initialisation
getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])
main_window = Tk()
main_window.geometry(resolution) ###########################################resolution
main_window.title("Parmenidis")
main_window.configure()
main_window.state("zoomed")
none="none" # προσωρινο για μεταβαση σε frames
previous_frame="previous_frame"
frame_counter=0
init_pass=0
stoixeia=[]#sos sos delete ειναι σαν temp για εισαγωγή data για email για έναν χρήστη


#Frames For Main Window
frame_temp=Frame()#Frame to get as temp to successfull change between frames
school_Frame=Frame(main_window, bg="white")
school_menu_Frame=Frame(school_Frame, bg="gray26")
school_intro_Frame = Frame(school_Frame, bg="floral white")
school_Dates_Frame = Frame(school_Frame, bg="floral white")
school_exams_Frame = Frame(school_Frame, bg="floral white")
school_program_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_create_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_edit_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_fin_Frame = Frame(school_Frame, bg="floral white")

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
    

    if(frameUp==school_menu_Frame):
        frameUp.tkraise()
        frameUp.pack(side=LEFT, fill=Y)
        init_pass=1
    else:
        frameUp.tkraise()
        frameUp.pack(expand=1,fill=BOTH)

#LOAD PHOTO
load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)

load0 = Image.open('backround2.jpg')
load0 = load0.resize((getRes[0], getRes[1]), Image.ANTIALIAS)
render0 = ImageTk.PhotoImage(load0)

def main():

    school_menu = Label(school_menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    smenu_l_up = Label(school_menu, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    smenu_l_down = Label(school_menu, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    initialSchool_all = Label(school_intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexia arxikh selida
    initialSchool_all_top = Label(initialSchool_all, text='Καλώς ορίσατε στον Παρμενίδη!',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 36, "bold"))
    initialSchool_all_bot = Label(initialSchool_all, borderwidth=1, highlightthickness=0, bg="red")
    initialSchool_ab_top = Label(initialSchool_all_bot, borderwidth=1, highlightthickness=0, bg="green")#include user name and calendar
    initialSchool_abt_left = Label(initialSchool_ab_top, borderwidth=1, highlightthickness=0, bg="black")#user school name left side
    initialSchool_abtl_top = Label(initialSchool_abt_left, borderwidth=1, highlightthickness=0, bg="yellow")#user school name top left previous side
    initialSchool_abtlt_left = Label(initialSchool_abtl_top, borderwidth=1, highlightthickness=0, bg="yellow")#user school name top of left side
    initialSchool_abtltl_left = Label(initialSchool_abtlt_left, text='Είστε συνδεδεμένοι ως: ',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    initialSchool_abtltl_right = Label(initialSchool_abtlt_left, text='1o Γενικό Λύκειο Κλειτορίας',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    initialSchool_abt_right = Label(initialSchool_ab_top, borderwidth=1, highlightthickness=0, bg="purple")#calenar and text include
    initialSchool_abtr_top = Label(initialSchool_abt_right, text='Ημερολόγιο', borderwidth=1, highlightthickness=0, bg="purple",font=("Times New Roman (Times)", 18, "bold"))#calendar text
    initialSchool_abtr_bot = Label(initialSchool_abt_right, borderwidth=1, highlightthickness=0, bg="red3")#calendar
    initialSchool_ab_bot = Label(initialSchool_all_bot, borderwidth=1, highlightthickness=0, bg="blue")#include announcements
    initialSchool_abb_top = Label(initialSchool_ab_bot, borderwidth=1, highlightthickness=0, bg="blue")
    initialSchool_abbt_left = Label(initialSchool_abb_top, text='Ανακοινώσεις',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#announcement title
    initialSchool_abb_bot = Frame(initialSchool_ab_bot, bg="cyan2")#announcement box

    #orismos listbox anakoinwsewn
    ministry_news_list  = Listbox (initialSchool_abb_bot, bg="floral white", borderwidth=2, highlightthickness=0)#width=getRes[0]-50, height=getRes[1]-70
    
    scrollh = Scrollbar(initialSchool_abb_bot, orient="horizontal", command=ministry_news_list.xview)
    scrollv= Scrollbar(initialSchool_abb_bot, orient="vertical", command=ministry_news_list.yview)
    initialSchool_abb_bot.bind("<Configure>",lambda e: ministry_news_list.configure(scrollregion=ministry_news_list.bbox("all")))
    ministry_news_list.configure(yscrollcommand=scrollv.set, xscrollcommand=scrollh.set, font=("Calibri", 36))
    initialSchool_abb_bot.bind("<MouseWheel>", scrollv)#ΚΑΘΕΤΟ SCROLL ΜΕ ΡΟΔΑ ΠΟΝΤΙΚΙΟΥ
    
    #ορισμος ημερολογιου
    cal_intro = Calendar(initialSchool_abtr_bot, selectmode='none')
    date = cal_intro.datetime.today() + cal_intro.timedelta(days=2)
    cal_intro.calevent_create(date, 'Hello World', 'message')
    cal_intro.calevent_create(date, 'Reminder 2', 'reminder')
    cal_intro.calevent_create(date + cal_intro.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal_intro.calevent_create(date + cal_intro.timedelta(days=3), 'Message', 'message')
    cal_intro.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')




    #orismos buttons
    btn_next0 = Button(smenu_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(school_intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_next1 = Button(smenu_l_down, text="Πρόγραμματα", command=lambda: raiseNdrop_frame(school_Dates_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_next2 = Button(smenu_l_down, text="Εγγραφές", command=lambda: raiseNdrop_frame(school_std_reg_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold")) 
    btn_next3 = Button(smenu_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    

    #packs εμφάνιση στοιχείων
    school_menu.pack(side=LEFT,expand=1,fill=Y)
    smenu_l_up.pack(side=TOP,pady=50)#PARMENIDIS LOGO
    smenu_l_down.pack(side=TOP)#CONTAINS BUTTONS
    initialSchool_all.pack(side=TOP,fill=BOTH,expand=1)#δεξιο μενου-αρχικη σελίδα
    initialSchool_all_top.pack(side=TOP,fill=X,pady=50)
    initialSchool_all_bot.pack(side=LEFT, expand=1, fill=BOTH)
    initialSchool_ab_top.pack(side=TOP, expand=1, fill=BOTH, ipady=100)
    #αριστερη πλευρα με ονομα σχολειου-χρηστη
    initialSchool_abt_left.pack(side=LEFT, fill=Y, padx=50)
    initialSchool_abtl_top.pack(side=TOP, fill=X)
    initialSchool_abtlt_left.pack(side=LEFT)
    initialSchool_abtltl_left.pack(side=TOP, pady=20)
    initialSchool_abtltl_right.pack(side=TOP)
    #δεξια πλευρα με ημερολογιο
    initialSchool_abt_right.pack(side=RIGHT, expand=1, fill=BOTH, padx=40)
    initialSchool_abtr_top.pack(side=TOP, fill=X) 
    initialSchool_abtr_bot.pack(side=TOP, fill=BOTH, expand=1)#hmerologio
    cal_intro.pack(fill=BOTH, expand=1)
    ttk.Label(initialSchool_abtr_bot, text="Hover over the events.").pack()
    #κατω πλευρα με ανακοινωσεις
    initialSchool_ab_bot.pack(side=TOP, expand=1, fill=BOTH)
    initialSchool_abb_top.pack(side=TOP, fill=X)
    initialSchool_abbt_left.pack(side=LEFT)
    initialSchool_abb_bot.pack(side=TOP, expand=1, fill=BOTH)
    scrollv.pack(side=RIGHT, fill=Y)
    scrollh.pack(side=BOTTOM, fill=X)
    ministry_news_list.pack(side=BOTTOM, expand=1, fill=BOTH)
    initialSchool_abb_bot.pack(side=BOTTOM, expand=1, fill=BOTH)

    #buttons MENU
    btn_next0.pack(side=TOP,pady=2,ipady=5)
    btn_next1.pack(side=TOP,pady=2,ipady=5)
    btn_next2.pack(side=TOP,pady=2,ipady=5)
    btn_next3.pack(side=TOP,pady=2,ipady=5)    

    #add elements to announcements
    ministry_news_list.insert(1, "This is a test to see if the announcements works as it should be")
    ministry_news_list.insert(2, "Ανακοινωση Ημερομηνίας Δηλώσεων")
    ministry_news_list.insert(3, "Πρόγραμμα εξεταστικής έτους 2020-2021")
    ministry_news_list.insert(4, "#ΜΕΝΟΥΜΕ_ΣΠΙΤΙ")
    ministry_news_list.insert(5, "Έναρξη δηλώσεων μαθητών")
    ministry_news_list.insert(6, "ΠΑΡΜΕΝΙΔΗΣ ΜΕ TKINTER ΓΙΑ GUI")
    ministry_news_list.insert(7, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")

    #ΑΡΧΙΚΑ FRAMES ΕΜΦΑΝΙΣΗ
    raiseNdrop_frame(school_Frame,none)
    raiseNdrop_frame(school_menu_Frame,none)
    raiseNdrop_frame(school_intro_Frame,none)  


    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_Dates_Frame

    dates_all = Label(school_Dates_Frame, bg="floral white")
    dates_all_top = Label(dates_all, bg="floral white")
    dates_at_top = Label(dates_all_top, text="Πρόγραμμα", bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    dates_all_mid = Label(dates_all, bg="floral white")
    dates_am_top = Label(dates_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="dodger blue")
    dates_am_bot = Label(dates_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    #
    #dates_amb_top = Label(dates_am_bot, bg="red")
    #dates_ambt_left = Label(dates_amb_top, bg="floral white")
    #dates_ambtl_top = Label(dates_ambt_left, bg="floral white")
    #dates_ambtl_bot = Label(dates_ambt_left, bg="floral white")
    #
    btn_school_program = Button(dates_am_bot, text="Εβδομαδιαίο Πρόγραμμα", command=lambda: raiseNdrop_frame(school_program_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_school_exams = Button(dates_am_bot, text="Πρόγραμμα Εξεταστικής", command=lambda: raiseNdrop_frame(school_exams_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    #pack-εμφάνιση στοιχείων
    dates_all.pack(side = TOP, fill=BOTH, expand=1)
    dates_all_top.pack(side = TOP, fill=X, ipady=50)
    dates_at_top.pack(side = TOP)
    dates_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    dates_am_top.pack(side = TOP)
    dates_am_bot.pack(side = TOP, fill=BOTH, expand=1)
    #
    #dates_amb_top.pack(side = TOP, fill=X)
    #dates_ambt_left.pack(side = LEFT, padx=50)
    #dates_ambtl_top.pack(side = TOP, pady=50)#top btn
    #dates_ambtl_bot.pack(side = TOP)#bot btn
    #Buttons pack
    #
    btn_school_program.pack(side = TOP,pady=100)
    btn_school_exams.pack(side = TOP)


    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_exams_Frame
    school_exams_all = Label(school_exams_Frame, bg="floral white")
    school_exams_a_top = Label(school_exams_all, text="Πρόγραμμα Εξεταστικής", bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    school_exams_a_mid = Label(school_exams_all, bg="floral white")
    school_exams_a_bot = Label(school_exams_all, bg="floral white")
    school_exams_am_top = Label(school_exams_a_mid, bg="floral white")#calendar
    school_exams_am_mid = Label(school_exams_a_mid, bg="floral white")#add/edit calendar


    #25LABELS SUNOLIKA ME BASH TO DIAGRAMMA

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_program_Frame

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_std_reg_Frame

    student_reg_all = Label(school_std_reg_Frame, bg="floral white")
    student_reg_all_top = Label(student_reg_all, bg="floral white")
    student_reg_at_top = Label(student_reg_all_top, text="Πρόγραμμα", bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    student_reg_all_mid = Label(student_reg_all, bg="floral white")
    student_reg_am_top = Label(student_reg_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="dodger blue")
    student_reg_am_bot = Label(student_reg_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
    #student_reg_amb_top = Label(student_reg_am_bot, bg="red")
    #student_reg_ambt_left = Label(student_reg_amb_top, bg="floral white")
    #student_reg_ambtl_top = Label(student_reg_ambt_left, bg="floral white")
    #student_reg_ambtl_bot = Label(student_reg_ambt_left, bg="floral white")
    btn_reg_create = Button(student_reg_am_bot, text="Δημιουργία Εγγραφής", command=lambda: raiseNdrop_frame(school_std_reg_create_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_reg_edit = Button(student_reg_am_bot, text="Επεξεργασία Εγγραφών", command=lambda: raiseNdrop_frame(school_std_reg_edit_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_reg_spectate = Button(student_reg_am_bot, text="Ολοκληρωμένες Εγγραφές", command=lambda: raiseNdrop_frame(school_std_reg_fin_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    #pack-εμφάνιση στοιχείων
    student_reg_all.pack(side = TOP, fill=BOTH, expand=1)
    student_reg_all_top.pack(side = TOP, fill=X, ipady=30)
    student_reg_at_top.pack(side = TOP)
    student_reg_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    student_reg_am_top.pack(side = TOP)
    student_reg_am_bot.pack(side = TOP, fill=BOTH, expand=1)
    #student_reg_amb_top.pack(side = TOP, fill=X)
    #student_reg_ambt_left.pack(side = LEFT, padx=50)
    #student_reg_ambtl_top.pack(side = TOP, pady=50)
    #student_reg_ambtl_bot.pack(side = TOP)
    #Buttons pack
    btn_reg_create.pack(side = TOP,pady=50)
    btn_reg_edit.pack(side = TOP)
    btn_reg_spectate.pack(side = TOP,pady=50)

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_std_reg_create_Frame

    std_reg_create_all = Label(school_std_reg_create_Frame, borderwidth=0, highlightthickness=0, bg="floral white")  # dexia arxikh selida
    std_reg_create_all_top = Label(std_reg_create_all, text='Δημιουργία Λίστας Εγγραφών',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 36, "bold"))
    std_reg_create_all_bot = Label(std_reg_create_all, borderwidth=1, highlightthickness=0, bg="red")
    std_reg_create_ab_top = Label(std_reg_create_all_bot, borderwidth=1, highlightthickness=0, bg="green")#include user name

    #ONOMA LISTAS
    std_reg_create_abt_top = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="black")#LIST  name
    #ΣΤΟΙΧΕΙΑ ΜΑΘΗΤΗ
    std_reg_create_abt_top1 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="black")#student  name 
    std_reg_create_abt_top2 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="black")#student  lastname 
    std_reg_create_abt_top3 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="black")#student email 
    std_reg_create_abt_top4 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="black")#student phone 
    std_reg_create_abt_top5 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="black")#info

    std_reg_create_abtltl_l = Label(std_reg_create_abt_top, text='Όνομα Λίστας*:\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l1 = Label(std_reg_create_abt_top1, text='Όνομα*:\t\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l2 = Label(std_reg_create_abt_top2, text='Επώνυμο*:\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l3 = Label(std_reg_create_abt_top3, text='E-mail*:\t\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l4 = Label(std_reg_create_abt_top4, text='Τηλέφωνο:\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l5 = Label(std_reg_create_abt_top5, text='(*Υποχρεωτικά πεδία)',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 12, "bold"))
    
    #TEXTS AS INPUTS!!!!!!!!!!!
    std_reg_create_abtltl_r = Text(std_reg_create_abt_top, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r1 = Text(std_reg_create_abt_top1, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r2 = Text(std_reg_create_abt_top2, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r3 = Text(std_reg_create_abt_top3, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r4 = Text(std_reg_create_abt_top4, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r1.config(state=DISABLED)
    std_reg_create_abtltl_r2.config(state=DISABLED)
    std_reg_create_abtltl_r3.config(state=DISABLED)
    std_reg_create_abtltl_r4.config(state=DISABLED)

    #Δήλωση textvariables sos πριν το καλεσμα τους
    register_list = StringVar()#(label_Statement1_all_mt8l_left)
    register_list.set("")

    std_reg_create_ab_mid = Label(std_reg_create_all_bot, borderwidth=1, highlightthickness=0, bg="blue")#include announcements
    std_reg_create_abm_top = Label(std_reg_create_ab_mid, borderwidth=1, highlightthickness=0, bg="blue")
    std_reg_create_abmt_left = Label(std_reg_create_abm_top, text='Λίστα Εγγραφών: ',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#announcement title
    std_reg_create_abmt_right = Label(std_reg_create_abm_top,textvariable=register_list ,borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#announcement title
    std_reg_create_abm_bot = Label(std_reg_create_ab_mid, bg="cyan2")#announcement box

    std_reg_create_ab_bot = Label(std_reg_create_all_bot, borderwidth=1, highlightthickness=0, bg="red")#ΚΑΤΩ ΠΛΕΥΡΑ ΜΕ ΚΟΥΜΠΙΑ NEXT KAI RETURN
    
    


    def confirm_list_name():
        list_name = std_reg_create_abtltl_r.get('1.0', 'end-1c')
        if (list_name!=""):#Αν δεν ειναι κενο το input
            std_reg_create_abtltl_r.config(state=DISABLED)
            register_list.set(list_name)
            std_reg_create_abtltl_r1.config(state=NORMAL)
            std_reg_create_abtltl_r2.config(state=NORMAL)
            std_reg_create_abtltl_r3.config(state=NORMAL)
            std_reg_create_abtltl_r4.config(state=NORMAL)

            btn_reg_create_return.config(state=NORMAL)
            btn_reg_create_confirm.config(state=NORMAL)
            btn_reg_list_name.config(state=DISABLED)
            btn_reg_delete_list.config(state=NORMAL)
            btn_reg_add.config(state=NORMAL)
            btn_reg_delete.config(state=NORMAL)
        else:
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ δημιουργείστε μία λίστα για τα στοιχεία των μαθητών!',icon='warning')
        print(list_name)
        print("register_list=",register_list)

    def delete_list():
        print("deleted list")
    

    def add_user():
        global stoixeia
        std_name = std_reg_create_abtltl_r1.get('1.0', 'end-1c')    #αντι end-1c αν βαλεις σκετο end βαζει στο τέλος newline 
        std_lastname = std_reg_create_abtltl_r2.get('1.0', 'end-1c')
        std_email = std_reg_create_abtltl_r3.get('1.0', 'end-1c')
        std_phone = std_reg_create_abtltl_r4.get('1.0', 'end-1c')
        if (std_name!="" and std_lastname!="" and std_email!=""):
            std_name_ok=std_name
            std_lastname_ok=std_lastname
            std_email_ok=std_email
            std_phone_ok=std_phone
            #insert ola ta ok se ΒΔ τα ok σαν attributes
            password = uuid.uuid4().hex[:10]#random unique 10 digit password will be send via email or phone number

            ###################################to delete just test
            stoixeia.append(std_name_ok)
            stoixeia.append(std_lastname_ok)
            stoixeia.append(password)
            stoixeia.append(std_email_ok)
            stoixeia.append(std_phone_ok)
            print(stoixeia)
            #--------------------------------------------------
        else:
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε ορθά τα στοιχεία του μαθητή',icon='warning')

        print(std_name_ok)
        print(std_lastname_ok)
        print(std_email_ok)
        print(std_phone_ok)
        print("password",password) 
        #https://realpython.com/python-send-email/
        #sos sos zisis ολα αυτα τα στοιχεια θα δημιουργουνται για την κλαση λιστας και οταν γίνει επιβεβαίωση λιστας θα αποθηκεύεται
        #  και θα διαβαζει ολους τους μαθητες στην λίστα και θα στέλνει από εκει emails.
        

    def delete_user():
        print("deleted user")

    def confirm_registry():
        #send email to all students
        #εδω θελουμε μια λίστα που να έχει αποθηκεύσει τα στοιχεία των μαθητών να την τρέχει και να στέλνει email.
        #https://dev.to/davidmm1707/how-to-send-emails-with-just-a-few-lines-of-code-with-yagmail-in-python-25pm
        sender_email = "parmenidis.gr@gmail.com"
        sender_password = "tl2020Parme"
        try:
            yag = yagmail.SMTP(user=sender_email, password=sender_password)
            subject='Στοιχεία Χρήστη Για Το Σύστημα Παρμενίδης'
            e1="Όνομα: " + stoixeia[0]
            e2="Επώνυμο: " + stoixeia[1]
            e3="Κωδικός Πρόσβασης: " + stoixeia[2]
            e4="E-mail: " + stoixeia[3]
            e5="Αριθμός Επικοινωνίας: " + stoixeia[4]
            contents = ["Καλώς ορίσατε στο ενιαίο Σύστημα Πανελληνίων Παρμενίδης!","Τα στοιχεία σας είνια τα εξής",e1,e2,e3,e4,e5]
            reciever=stoixeia[3]
            yag.send(reciever, subject, contents)
        except:
            print("Error, email was not sent")
        print("registry confirmed")

    #ORISMOS BTNS
    btn_reg_create_return = Button(std_reg_create_ab_bot, text="Επιστροφή", command=lambda: raiseNdrop_frame(school_std_reg_Frame,previous_frame), bg="red3",height = 1, width = 12,font=("Calibri", 16, "bold"))
    btn_reg_create_confirm = Button(std_reg_create_ab_bot, text="Επιβεβαίωση", state=DISABLED, command=lambda: confirm_registry(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_list_name = Button(std_reg_create_abt_top, text="Δημιουργία Λίστας", command=lambda: confirm_list_name(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_delete_list = Button(std_reg_create_ab_bot, text="Διαγραφή Λίστας", state=DISABLED, command=lambda: delete_list(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_add = Button(std_reg_create_ab_top, text="Προσθήκη Εγγραφής", state=DISABLED, command=lambda: add_user(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_delete = Button(std_reg_create_ab_top, text="Διαγραφή Εγγραφής", state=DISABLED, command=lambda: delete_user(), bg="red3",font=("Calibri", 16, "bold"))

    #orismos listbox sos sos edw 8elei tkinterctrl
    user_list  = Listbox (std_reg_create_abm_bot, bg="floral white", borderwidth=2, highlightthickness=0, selectmode='single')
    
    scrollh_usr = Scrollbar(std_reg_create_abm_bot, orient="horizontal", command=user_list.xview)
    scrollv_usr= Scrollbar(std_reg_create_abm_bot, orient="vertical", command=user_list.yview)
    std_reg_create_abm_bot.bind("<Configure>",lambda e: user_list.configure(scrollregion=user_list.bbox("all")))
    user_list.configure(yscrollcommand=scrollv_usr.set, xscrollcommand=scrollh_usr.set, font=("Times New Roman (Times)", 16,"bold"))
    std_reg_create_abm_bot.bind("<MouseWheel>", scrollv_usr)#ΚΑΘΕΤΟ SCROLL ΜΕ ΡΟΔΑ ΠΟΝΤΙΚΙΟΥ
    
    #add elements to announcements
    user_list.insert(1, "This is a test to see if the announcements works as it should be")
    user_list.insert(2, "Ανακοινωση Ημερομηνίας Δηλώσεων")
    user_list.insert(3, "Πρόγραμμα εξεταστικής έτους 2020-2021")
    user_list.insert(4, "#ΜΕΝΟΥΜΕ_ΣΠΙΤΙ")
    user_list.insert(5, "Έναρξη δηλώσεων μαθητών")
    user_list.insert(6, "ΠΑΡΜΕΝΙΔΗΣ ΜΕ TKINTER ΓΙΑ GUI")
    user_list.insert(7, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")

    #packs εμφάνιση στοιχείων
    std_reg_create_all.pack(side=TOP,fill=BOTH,expand=1)#δεξιο μενου-αρχικη σελίδα
    std_reg_create_all_top.pack(side=TOP,fill=X)

    std_reg_create_all_bot.pack(side=TOP, expand=1, fill=BOTH,pady=30)
    std_reg_create_ab_top.pack(side=TOP, fill=X)#expand=1
    
    #αριστερη πλευρα με  στοιχεια εγγραφης
    std_reg_create_abt_top.pack(side=TOP, fill=X)
    std_reg_create_abt_top1.pack(side=TOP, fill=X)
    std_reg_create_abt_top2.pack(side=TOP, fill=X)
    std_reg_create_abt_top3.pack(side=TOP, fill=X)
    std_reg_create_abt_top4.pack(side=TOP, fill=X)
    std_reg_create_abt_top5.pack(side=TOP, fill=X)

    std_reg_create_abtltl_l.pack(side=LEFT, padx=50)#ονομα λίστας
    std_reg_create_abtltl_l1.pack(side=LEFT, padx=50)#ονομα
    std_reg_create_abtltl_l2.pack(side=LEFT, padx=50)#επωνυμο
    std_reg_create_abtltl_l3.pack(side=LEFT, padx=50)#e-mail
    std_reg_create_abtltl_l4.pack(side=LEFT, padx=50)#τηλ επικ
    std_reg_create_abtltl_l5.pack(side=LEFT, padx=50)#info

    std_reg_create_abtltl_r.pack(side=LEFT)#ονομα λίστας
    std_reg_create_abtltl_r1.pack(side=LEFT)#ονομα
    std_reg_create_abtltl_r2.pack(side=LEFT)#επωνυμο
    std_reg_create_abtltl_r3.pack(side=LEFT)#e-mail
    std_reg_create_abtltl_r4.pack(side=LEFT)#τηλ επικ

    #κατω πλευρα με Λίστα
    std_reg_create_ab_mid.pack(side=TOP, fill=BOTH,expand=1)#,ipady=100)#, expand=1, fill=X)#BOTH
    std_reg_create_abm_top.pack(side=TOP, fill=X)
    std_reg_create_abmt_left.pack(side=LEFT,padx=10)
    std_reg_create_abmt_right.pack(side=LEFT)
    std_reg_create_abm_bot.pack(side=TOP, expand=1, fill=BOTH)#BOTH
    scrollv_usr.pack(side=RIGHT, fill=Y)
    scrollh_usr.pack(side=BOTTOM, fill=X)
    user_list.pack(side=BOTTOM, expand=1, fill=BOTH)#BOTH
    #std_reg_create_abm_bot.pack(side=BOTTOM, expand=1, fill=BOTH)#BOTH

    #κατω πλευρα με buttons σελιδας
    std_reg_create_ab_bot.pack(side= TOP, fill=X)

    #buttons MENU
    btn_reg_create_confirm.pack(side=RIGHT, padx=50)
    btn_reg_create_return.pack(side=RIGHT)
    btn_reg_add.pack(side=RIGHT, padx=50)
    btn_reg_delete.pack(side=RIGHT) 
    btn_reg_list_name.pack(side=LEFT, padx=30) 
    btn_reg_delete_list.pack(side=LEFT, padx=50) 
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_std_reg_edit_Frame


    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_std_reg_fin_Frame
    
    
    student_reg_fin_all = Label(school_std_reg_fin_Frame, bg="floral white")
    student_reg_fin_a_bot = Label(student_reg_fin_all, bg="floral white")
    
    btn_reg_spectate = Button(student_reg_fin_a_bot, text="Επιστροφή", command=lambda: raiseNdrop_frame(school_std_reg_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    #packs

    student_reg_fin_all.pack(side = TOP, expand=1, fill=BOTH)
    student_reg_fin_a_bot.pack(side=BOTTOM, fill=X)
    btn_reg_spectate.pack(side=RIGHT, padx=100)

    main_window.mainloop()  # ------------------------------Put always to end of frames

main()
