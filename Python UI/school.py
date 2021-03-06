#extra need yagmail from pip import and import os and treectrl, validate_email, py3DNS

#region imports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry
import uuid
import yagmail
from TkTreectrl import *
import TkTreectrl as treectrl
import os
from validate_email import *
#endregion

#Initialisation
getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])
main_window = Tk()
main_window.geometry(resolution) ###########################################resolution
main_window.title("Parmenidis")
main_window.configure()
main_window.state("zoomed")
#main_window.attributes('-fullscreen', True)
none="none" # προσωρινο για μεταβαση σε frames
previous_frame="previous_frame"
frame_counter=0
init_pass=0
mydir=os.getcwd()
memory_dir=None
school_week_path = None
school_exams_path = None
std_list_path = None
login_path=None
selected_row=None  #αρχικοποίηση μεταβλητης για να παίρνω το row που έχει επιλεχθεί στα προγράμματα
std_counter=None
hour_1=[]#arxikopoihsh pinaka
hour_2=[]
hour_3=[]
hour_4=[]
hour_5=[]
hour_6=[]
hour_7=[]
exams_dates=[]
std_users=[]
login_list=[]


#region Frames For Main Window
frame_temp=Frame()#Frame to get as temp to successfull change between frames
school_Frame=Frame(main_window, bg="white")
school_menu_Frame=Frame(school_Frame, bg="gray26")
school_intro_Frame = Frame(school_Frame, bg="floral white")
school_Dates_Frame = Frame(school_Frame, bg="floral white")
school_exams_Frame = Frame(school_Frame, bg="floral white")
school_program_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_create_Frame = Frame(school_Frame, bg="floral white")
school_std_reg_fin_Frame = Frame(school_Frame, bg="floral white")
#endregion

def memory():    #function to create a folder that contains txts with memory
    global hour_1#arxikopoihsh pinaka
    global hour_2
    global hour_3
    global hour_4
    global hour_5
    global hour_6
    global hour_7

    global memory_dir
    global school_week_path
    global school_exams_path
    global std_list_path
    global login_path

    global exams_dates
    global std_counter
    global std_users
    global login_List
    try:
        if not os.path.exists('Memory'):
            os.makedirs('Memory')
            messagebox.showinfo('Προσοχή',"Ο φάκελος Memory μόλις δημιουργήθηκε\n")
            memory_dir = mydir+"\Memory"
            #αρχικοποίηση στοιχείων-data
            hour_1=['08:15-09:00','','','','','']#arxikopoihsh pinaka
            hour_2=['09:10-09:50','','','','','']
            hour_3=['10:00-10:40','','','','','']
            hour_4=['10:50-11:30','','','','','']
            hour_5=['11:35-12:15','','','','','']
            hour_6=['12:20-13:00','','','','','']
            hour_7=['13:05-13:40','','','','','']
        else:
            #messagebox.showinfo('Προσοχή'," Folder Memory already exists\n")
            memory_dir = mydir+"\Memory"

            #path arxeiwn
            school_week_path = memory_dir + "\school_week.txt"
            school_exams_path = memory_dir + "\school_exams.txt"
            std_list_path = memory_dir +  "\std_list.txt"
            login_path = memory_dir +  "\login.txt"

            #check if all needed files exist!
            #region login
            if os.path.isfile(login_path):
                print ("File login exist")
                login_file = open(login_path, "r")
                login_line_list = login_file.readlines()#this list contains rows with \n
                for login_info in login_line_list:
                    cur_login = login_info.strip()#removes\n from each line of the text returns string
                    cur_login_list = cur_login.split(",")#returns list with splitted elements of notification
                    login_list.append(cur_login_list)
                print("\nlogin_list=",login_list)
            else:
                print ("File login created")#created
            #endregion

            #region school_week
            if os.path.isfile(school_week_path):
                print ("File school_week exist")#read
                school_week = open(school_week_path, "r")
                print(school_week)
                week_program = school_week.readlines()
                line_count=0
                for hour_program in week_program:
                    line_count+=1
                    cur_hour = hour_program.strip()#removes\n from each line of the text
                    if(line_count==1):
                       hour_1 = cur_hour.split(",")
                    elif(line_count==2):
                        hour_2 = cur_hour.split(",")
                    elif(line_count==3):
                        hour_3 = cur_hour.split(",")
                    elif(line_count==4):
                        hour_4 = cur_hour.split(",")
                    elif(line_count==5):
                        hour_5 = cur_hour.split(",")
                    elif(line_count==6):
                        hour_6 = cur_hour.split(",")
                    elif(line_count==7):
                        hour_7 = cur_hour.split(",")
                school_week.close()#close file

            else:
                print ("File school_week created")#created
                school_week = open(school_week_path, "w")
                school_week.close()
            #endregion

            #region school_exams
            if os.path.isfile(school_exams_path):
                print ("File school_exams exist")#read
                school_exams = open(school_exams_path, "r")
                print(school_exams)
                exams_program = school_exams.readlines()
                for notification in exams_program:
                    exams_count=1
                    cur_notification = notification.strip()#removes\n from each line of the text returns string
                    cur_notif_list = cur_notification.split(",")#returns list with splitted elements of notification
                    exams_dates.append(cur_notif_list)
                print(exams_dates)
                school_exams.close()
            else:
                print ("File school_exams created")#created
                school_exams = open(school_exams_path, "w")
                school_exams.close()
            #endregion

            #region school_insert_user
            if os.path.isfile(std_list_path):
                print ("File std_list exist")#read
                std_list = open(std_list_path, "r")
                student_list = std_list.readlines()
                print('\nstdlist=',student_list)
                temp_id_counter=None
                temp_id_str=None
                temp_idx=0
                std_counter=0
                for std in student_list:
                    exams_count=1
                    cur_student = std.strip()#removes\n from each line of the text returns string
                    cur_student_list = cur_student.split(",")#returns list with splitted elements of notification
                    std_users.append(cur_student_list)
                    #get max id num to know next id counter
                    temp_id_str=std_users[temp_idx][0]
                    usrn_list=list(temp_id_str)
                    usrn_list.pop(0)#remove s
                    usrn_list.pop(0)#remove t
                    usrn_list.pop(0)#remove d
                    temp_id_counter="".join(usrn_list)
                    temp_id_compare = int(temp_id_counter)
                    if(temp_id_compare > std_counter):#find max id number
                        std_counter=temp_id_compare
                    temp_idx+=1#increase to get new idx
                    #----------
                print("\nstd_users=",std_users)
                std_list.close()
                print("\nstdcounter",std_counter)
            else:
                print ("File std_list created")#created
                std_list = open(std_list_path, "w")
                std_counter=0
                std_list.close()
            #endregion
    except OSError:
        messagebox.showinfo('Προσοχή',"Error creating directory "+(mydir)+"\Memory")


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
    global exams_dates#list containing data from memory exams school

    school_menu = Label(school_menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    smenu_l_up = Label(school_menu, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    smenu_l_down = Label(school_menu, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    initialSchool_all = Label(school_intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexia arxikh selida
    initialSchool_all_top = Label(initialSchool_all, text='Καλώς ορίσατε στον Παρμενίδη!',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 36, "bold"))
    initialSchool_all_bot = Label(initialSchool_all, borderwidth=1, highlightthickness=0, bg="floral white")
    initialSchool_ab_top = Label(initialSchool_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include user name and calendar
    initialSchool_abt_left = Label(initialSchool_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#user school name left side
    initialSchool_abtl_top = Label(initialSchool_abt_left, borderwidth=1, highlightthickness=0, bg="floral white")#user school name top left previous side
    initialSchool_abtlt_left = Label(initialSchool_abtl_top, borderwidth=1, highlightthickness=0, bg="floral white")#user school name top of left side
    initialSchool_abtltl_left = Label(initialSchool_abtlt_left, text='Είστε συνδεδεμένοι ως: ',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    initialSchool_abtltl_right = Label(initialSchool_abtlt_left, text='1o Γενικό Λύκειο Κλειτορίας',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    initialSchool_abt_right = Label(initialSchool_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#calenar and text include
    initialSchool_abtr_top = Label(initialSchool_abt_right, text='Ημερολόγιο', borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#calendar text
    initialSchool_abtr_bot = Label(initialSchool_abt_right, borderwidth=1, highlightthickness=0, bg="floral white")#calendar
    initialSchool_ab_bot = Label(initialSchool_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include announcements
    initialSchool_abb_top = Label(initialSchool_ab_bot, borderwidth=1, highlightthickness=0, bg="floral white")
    initialSchool_abbt_left = Label(initialSchool_abb_top, text='Ανακοινώσεις',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#announcement title
    initialSchool_abb_bot = Frame(initialSchool_ab_bot, bg="floral white")#announcement box

    #orismos listbox anakoinwsewn
    ministry_news_list  = Listbox (initialSchool_abb_bot, bg="floral white", borderwidth=2, highlightthickness=0)#width=getRes[0]-50, height=getRes[1]-70
    
    scrollh = Scrollbar(initialSchool_abb_bot, orient="horizontal", command=ministry_news_list.xview)
    scrollv= Scrollbar(initialSchool_abb_bot, orient="vertical", command=ministry_news_list.yview)
    initialSchool_abb_bot.bind("<Configure>",lambda e: ministry_news_list.configure(scrollregion=ministry_news_list.bbox("all")))
    ministry_news_list.configure(yscrollcommand=scrollv.set, xscrollcommand=scrollh.set, font=("Calibri", 18))
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
    btn_school_program = Button(dates_am_bot, text="Εβδομαδιαίο Πρόγραμμα", command=lambda: raiseNdrop_frame(school_program_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_school_exams = Button(dates_am_bot, text="Πρόγραμμα Εξεταστικής", command=lambda: raiseNdrop_frame(school_exams_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    #pack-εμφάνιση στοιχείων
    dates_all.pack(side = TOP, fill=BOTH, expand=1)
    dates_all_top.pack(side = TOP, fill=X, ipady=50)
    dates_at_top.pack(side = TOP)
    dates_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    dates_am_top.pack(side = TOP)
    dates_am_bot.pack(side = TOP, fill=BOTH, expand=1)
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
    school_exams_am_mid = Label(school_exams_a_mid, bg="floral white",relief="groove")#add/edit/delete calendar
    school_exams_amm_top = Label(school_exams_am_mid, text="Επεξεργασία Προγράμματος", bg="SkyBlue1", font=("Times New Roman (Times)", 20, "bold"))#edit title
    school_exams_amm_mid = Label(school_exams_am_mid, bg="floral white")#text - input from user
    school_exams_amm_bot = Label(school_exams_am_mid, bg="floral white")#buttons add/delete

    school_exams_ammm_top = Label(school_exams_amm_mid, bg="floral white")#message
    school_exams_ammmt_left = Label(school_exams_ammm_top, text="Μήνυμα:\t\t", bg="floral white", font=("Times New Roman (Times)", 18, "bold"))
    school_exams_ammmt_right = Text(school_exams_ammm_top, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    

    school_exams_ammm_mid = Label(school_exams_amm_mid, bg="floral white")#reminder
    school_exams_ammmm_left = Label(school_exams_ammm_mid, text="Υπενθύμιση:\t", bg="floral white" ,font=("Times New Roman (Times)", 18, "bold"))
    school_exams_ammmm_right = Text(school_exams_ammm_mid, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    school_exams_ammm_bot = Label(school_exams_amm_mid, bg="floral white")#date
    school_exams_ammmb_left = Label(school_exams_ammm_bot, text="Ημερομηνία:\t", bg="floral white" ,font=("Times New Roman (Times)", 18, "bold"))
    school_exams_ammmb_right = Text(school_exams_ammm_bot, state=NORMAL, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    #ανάκτηση ημερομηνίας μεταβλητη
    cur_exam_date = StringVar()
    cur_exam_date.set("")

    def conf_school_exams():
        global school_exams_path
        event_ids = cal_exams.get_calevents()
        print("events:",event_ids)
        print("school exams confirmed")
        write_exams_program = open(school_exams_path,"w").close()#διαγραφή περιεχομένου  αρχείου εβδομαδιαίου προγράμματος
        for id in event_ids:
            #date = cal_exams.calevent_cget(id,'date')
            date = datetime.strptime(str(cal_exams.calevent_cget(id,'date')), '%Y-%m-%d').strftime('%d/%m/%Y')#μετατροπη date απο y-m-d σε d/m/y
            print("date:",date)
            text = cal_exams.calevent_cget(id,'text')
            print("text:",text)
            tag_list = cal_exams.calevent_cget(id,'tags')
            tag=tag_list[0]#γιατι θέλουμε το message ή reminder σαν string
            print("tag:",tag)
            exam_row = str(date) + "," + str(text) + "," + str(tag) + "\n"
            write_exam_program = open(school_exams_path,"a")#εισαγωγή δεδομένων σε αρχείο εβδομαδιαίου προγράμματος
            write_exam_program.write(exam_row)
        write_exam_program.close()
        #options= "text", "tags" and "date".

    def add_school_exams():
        message = school_exams_ammmt_right.get("1.0",'end-1c')
        reminder = school_exams_ammmm_right.get("1.0",'end-1c')
        date = school_exams_ammmb_right.get("1.0",'end-1c')
        flag=0
        if (date!=""):
            date_time_obj = datetime.strptime(date, '%d/%m/%Y')
        if(date==""):
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε μια ημερομηνία για το μήνυμα ή την υπενθύμιση που θέλετε να προσθέσετε!',icon='warning')
        else:
            if(message!=""):
                cal_exams.calevent_create(date_time_obj, message, 'message')
            if(reminder!=""):
                cal_exams.calevent_create(date_time_obj, reminder, 'reminder')
            if(message=="" and reminder==""):
                flag=1
                messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε ένα μήνυμα ή υπενθύμιση για την τρέχουσα ημερομηνία και δοκιμάστε να ξανακάνετε προσθήκη!',icon='warning')
        school_exams_ammmt_right.delete('1.0', END)
        school_exams_ammmm_right.delete('1.0', END)
        if(flag==0):
            school_exams_ammmb_right.delete('1.0', END)
        print("school exams added")

    def delete_school_exams():
        #cal_exams.selection_clear(cur_exam_date.get())
        date_rem = datetime.strptime(cur_exam_date.get(), '%d/%m/%Y')
        cal_exams.calevent_remove(date=date_rem)
        #print("deleted:",cur_exam_date.get())
        print("school exams selected event deleted")
        cal_exams.selection_clear()

    def delete_school_exams_calendar():
        cal_exams.calevent_remove('all')
        print("all school exams calendar events are deleted")

    #add 4 buttons
    btn_add_cal = Button(school_exams_amm_bot, text="Προσθήκη", state=NORMAL, command=lambda: add_school_exams(),bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_delete_cal = Button(school_exams_amm_bot, text="Διαγραφή", state=NORMAL, command=lambda: delete_school_exams(),bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_confirm_cal = Button(school_exams_a_bot, text="Επιβεβαίωση", state=NORMAL, command=lambda: conf_school_exams(), bg="green4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_return_cal = Button(school_exams_a_bot, text="Επιστροφή", state=NORMAL, command=lambda: raiseNdrop_frame(school_Dates_Frame,previous_frame),bg="red4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_delete_cal_all = Button(school_exams_a_bot, text="Διαγραφή Ημερολογίου ", state=NORMAL, command=lambda: delete_school_exams_calendar(), bg="floral white",font=("Times New Roman (Times)", 13, "bold"),height=1 ,width=20)
    

    #ορισμος ημερολογιου και αρχικοποίηση τιμών μέσω memory
    cal_exams = Calendar(school_exams_am_top, selectmode='day',textvariable=cur_exam_date, date_pattern='dd/mm/y')
    cal_exams.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')

    def check_exam_dates(date_list):#ADDS EVENTS FROM MEMORY
        for elem in date_list:
            # date message reminder με αυτη την σειρα έιναι τα data
            datetime_obj = datetime.strptime(elem[0], '%d/%m/%Y')
            if(elem[2]=="message"):#Ωστε να μην κανει insert το κενό
                cal_exams.calevent_create(datetime_obj, elem[1], 'message')
            elif(elem[2]=="reminder"):
                cal_exams.calevent_create(datetime_obj, elem[1], 'reminder')
            
            print("inserted exams dates from memory")
    check_exam_dates(exams_dates)


    #Εμφάμιση στοιχείων packs
    school_exams_all.pack(side=TOP, expand=1, fill=BOTH)#contains all labels
    school_exams_a_top.pack(side=TOP, fill=X)#title label
    school_exams_a_mid.pack(side=TOP, expand=1, fill=BOTH, pady=50)#middle labels edit etc
    school_exams_a_bot.pack(side=TOP, fill=X)#buttons down label
    school_exams_am_top.pack(side=TOP, expand=1, fill=BOTH, ipady=20)#calendar
    cal_exams.pack(side=TOP, expand=1, fill=BOTH)
    school_exams_am_mid.pack(side=TOP, expand=1, fill=BOTH)#edits
    school_exams_amm_top.pack(side=TOP, fill=X, ipady=5)#edit Title
    school_exams_amm_mid.pack(side=TOP, expand=1, fill=BOTH)
    school_exams_amm_bot.pack(side=TOP, fill=X)

    #Στοιχεία προς επεξεργασία
    #μηνυμα
    school_exams_ammm_top.pack(side=TOP, fill=X)
    school_exams_ammmt_left.pack(side=LEFT,padx=50)
    school_exams_ammmt_right.pack(side=LEFT)
    #υπενθυμιση
    school_exams_ammm_mid.pack(side=TOP, fill=X)
    school_exams_ammmm_left.pack(side=LEFT,padx=50)
    school_exams_ammmm_right.pack(side=LEFT)
    #ημερομηνία
    school_exams_ammm_bot.pack(side=TOP, fill=X)
    school_exams_ammmb_left.pack(side=LEFT,padx=50)
    school_exams_ammmb_right.pack(side=LEFT)

    #εμφάνιση κουμπιών 
    #κουμπια επεξεργασίας
    btn_add_cal.pack(side=RIGHT, padx=100)
    btn_delete_cal.pack(side=RIGHT)
    #κουμπιά μενού
    btn_confirm_cal.pack(side=RIGHT, padx=100)
    btn_return_cal.pack(side=RIGHT)
    btn_delete_cal_all.pack(side=LEFT, padx=100)


    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_program_Frame


    school_program_all = Label(school_program_Frame, bg="floral white")
    school_program_a_top = Label(school_program_all, text="Εβδομαδιαίο Πρόγραμμα", bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    school_program_a_mid = Label(school_program_all, bg="floral white")
    school_program_a_bot = Label(school_program_all, bg="floral white")
    school_program_am_top = Label(school_program_a_mid, bg="floral white")#calendar
    school_program_am_mid = Label(school_program_a_mid, bg="floral white",relief="groove")#add/edit/delete calendar
    school_program_amm_top = Label(school_program_am_mid, text="Επεξεργασία Προγράμματος", bg="SkyBlue1", font=("Times New Roman (Times)", 20, "bold"))#edit title
    school_program_amm_mid = Label(school_program_am_mid, bg="floral white")#text - input from user
    school_program_amm_bot = Label(school_program_am_mid, bg="floral white")#buttons add/delete

    school_program_ammm_top0 = Label(school_program_amm_mid, bg="floral white")#Ώρα
    school_program_ammmt0_left = Label(school_program_ammm_top0, text="Ώρα:\t\t", bg="floral white", font=("Times New Roman (Times)", 14, "bold"))
    school_program_ammmt0_right = Text(school_program_ammm_top0, bg="WHITE", fg="black", height=1, width=40, borderwidth=1, highlightthickness=2,font=("Calibri", 14))

    school_program_ammm_top = Label(school_program_amm_mid, bg="floral white")#Δευτέρα
    school_program_ammmt_left = Label(school_program_ammm_top, text="Δευτέρα:\t\t", bg="floral white", font=("Times New Roman (Times)", 14, "bold"))
    school_program_ammmt_right = Text(school_program_ammm_top, bg="WHITE", fg="black", height=1, width=40, borderwidth=1, highlightthickness=2,font=("Calibri", 14))
    
    school_program_ammm_mid = Label(school_program_amm_mid, bg="floral white")#Τρίτη
    school_program_ammmm_left = Label(school_program_ammm_mid, text="Τρίτη:\t\t", bg="floral white" ,font=("Times New Roman (Times)", 14, "bold"))
    school_program_ammmm_right = Text(school_program_ammm_mid, bg="WHITE", fg="black", height=1, width=40, borderwidth=1, highlightthickness=2,font=("Calibri", 14))

    school_program_ammm_bot = Label(school_program_amm_mid, bg="floral white")#Τετάρτη
    school_program_ammmb_left = Label(school_program_ammm_bot, text="Τετάρτη:\t\t", bg="floral white" ,font=("Times New Roman (Times)", 14, "bold"))
    school_program_ammmb_right = Text(school_program_ammm_bot, bg="WHITE", fg="black", height=1, width=40, borderwidth=1, highlightthickness=2,font=("Calibri", 14))

    school_program_ammm_bot2 = Label(school_program_amm_mid, bg="floral white")#Πέμπτη
    school_program_ammmb2_left = Label(school_program_ammm_bot2, text="Πέμπτη:\t\t", bg="floral white" ,font=("Times New Roman (Times)", 14, "bold"))
    school_program_ammmb2_right = Text(school_program_ammm_bot2, bg="WHITE", fg="black", height=1, width=40, borderwidth=1, highlightthickness=2,font=("Calibri", 14))

    school_program_ammm_bot3 = Label(school_program_amm_mid, bg="floral white")#Παρασκευή
    school_program_ammmb3_left = Label(school_program_ammm_bot3, text="Παρασκευή:\t", bg="floral white" ,font=("Times New Roman (Times)", 14, "bold"))
    school_program_ammmb3_right = Text(school_program_ammm_bot3, bg="WHITE", fg="black", height=1, width=40, borderwidth=1, highlightthickness=2,font=("Calibri", 14))
    #MAKE TEXT UNEDITABLE
    school_program_ammmt0_right.config(state=DISABLED)
    school_program_ammmt_right.config(state=DISABLED)
    school_program_ammmm_right.config(state=DISABLED)
    school_program_ammmb_right.config(state=DISABLED)
    school_program_ammmb2_right.config(state=DISABLED)
    school_program_ammmb3_right.config(state=DISABLED)

    #ορισμος εβδομαδιαίου ημερολογίου με treectrl
    cal_program = treectrl.MultiListbox(school_program_am_top)
    titles=['Ωράριο', 'Δευτέρα','Τρίτη','Τετάρτη','Πέμπτη','Παρασκευή']
   

    def conf_school_program():
        global school_week_path
        global hour_1
        global hour_2
        global hour_3
        global hour_4
        global hour_5
        global hour_6
        global hour_7
        temp_1=",".join(hour_1)
        temp_2=",".join(hour_2)
        temp_3=",".join(hour_3)
        temp_4=",".join(hour_4)
        temp_5=",".join(hour_5)
        temp_6=",".join(hour_6)
        temp_7=",".join(hour_7)
        #fix data with \n to be readable by memory function
        h1=temp_1 +"\n"
        h2=temp_2 +"\n"
        h3=temp_3 +"\n"
        h4=temp_4 +"\n"
        h5=temp_5 +"\n"
        h6=temp_6 +"\n"
        h7=temp_7 +"\n"
        write_week_program = open(school_week_path,"w").close()#διαγραφή περιεχομένου  αρχείου εβδομαδιαίου προγράμματος
        write_week_program = open(school_week_path,"a")#εισαγωγή δεδομένων σε αρχείο εβδομαδιαίου προγράμματος
        write_week_program.write(h1)
        write_week_program.write(h2)
        write_week_program.write(h3)
        write_week_program.write(h4)
        write_week_program.write(h5)
        write_week_program.write(h6)
        write_week_program.write(h7)
        write_week_program.close()
        print("Αποθήκευση νέου εβδομαδιαίου προγράμματος με επιτυχία!")

    def select_cmd(selected):
        print ('Selected items:',selected)#shows tuple row selected
        global selected_row
        selected_row = int(selected[0])#shows row selected
        print(selected_row)
        #MAKE TEXT EDITABLE
        school_program_ammmt0_right.config(state=NORMAL)
        school_program_ammmt_right.config(state=NORMAL)
        school_program_ammmm_right.config(state=NORMAL)
        school_program_ammmb_right.config(state=NORMAL)
        school_program_ammmb2_right.config(state=NORMAL)
        school_program_ammmb3_right.config(state=NORMAL)
        #DELETE OLD TEXT INPUTS
        school_program_ammmt0_right.delete('1.0', END)
        school_program_ammmt_right.delete('1.0', END)
        school_program_ammmm_right.delete('1.0', END)
        school_program_ammmb_right.delete('1.0', END)
        school_program_ammmb2_right.delete('1.0', END)
        school_program_ammmb3_right.delete('1.0', END)
        #BASE ON ROW SELECTED GET INFO to show on text
        if(selected_row==0):
            school_program_ammmt0_right.insert(INSERT,hour_1[0])
            school_program_ammmt_right.insert(INSERT,hour_1[1])
            school_program_ammmm_right.insert(INSERT,hour_1[2])
            school_program_ammmb_right.insert(INSERT,hour_1[3])
            school_program_ammmb2_right.insert(INSERT,hour_1[4])
            school_program_ammmb3_right.insert(INSERT,hour_1[5])
            print(hour_1)
        elif(selected_row==1):
            school_program_ammmt0_right.insert(INSERT,hour_2[0])
            school_program_ammmt_right.insert(INSERT,hour_2[1])
            school_program_ammmm_right.insert(INSERT,hour_2[2])
            school_program_ammmb_right.insert(INSERT,hour_2[3])
            school_program_ammmb2_right.insert(INSERT,hour_2[4])
            school_program_ammmb3_right.insert(INSERT,hour_2[5])
            print(hour_2)
        elif(selected_row==2):
            school_program_ammmt0_right.insert(INSERT,hour_3[0])
            school_program_ammmt_right.insert(INSERT,hour_3[1])
            school_program_ammmm_right.insert(INSERT,hour_3[2])
            school_program_ammmb_right.insert(INSERT,hour_3[3])
            school_program_ammmb2_right.insert(INSERT,hour_3[4])
            school_program_ammmb3_right.insert(INSERT,hour_3[5])
            print(hour_3)
        elif(selected_row==3):
            school_program_ammmt0_right.insert(INSERT,hour_4[0])
            school_program_ammmt_right.insert(INSERT,hour_4[1])
            school_program_ammmm_right.insert(INSERT,hour_4[2])
            school_program_ammmb_right.insert(INSERT,hour_4[3])
            school_program_ammmb2_right.insert(INSERT,hour_4[4])
            school_program_ammmb3_right.insert(INSERT,hour_4[5])
            print(hour_4)
        elif(selected_row==4):
            school_program_ammmt0_right.insert(INSERT,hour_5[0])
            school_program_ammmt_right.insert(INSERT,hour_5[1])
            school_program_ammmm_right.insert(INSERT,hour_5[2])
            school_program_ammmb_right.insert(INSERT,hour_5[3])
            school_program_ammmb2_right.insert(INSERT,hour_5[4])
            school_program_ammmb3_right.insert(INSERT,hour_5[5])
            print(hour_5)
        elif(selected_row==5):
            school_program_ammmt0_right.insert(INSERT,hour_6[0])
            school_program_ammmt_right.insert(INSERT,hour_6[1])
            school_program_ammmm_right.insert(INSERT,hour_6[2])
            school_program_ammmb_right.insert(INSERT,hour_6[3])
            school_program_ammmb2_right.insert(INSERT,hour_6[4])
            school_program_ammmb3_right.insert(INSERT,hour_6[5])
            print(hour_6)
        elif(selected_row==6):
            school_program_ammmt0_right.insert(INSERT,hour_7[0])
            school_program_ammmt_right.insert(INSERT,hour_7[1])
            school_program_ammmm_right.insert(INSERT,hour_7[2])
            school_program_ammmb_right.insert(INSERT,hour_7[3])
            school_program_ammmb2_right.insert(INSERT,hour_7[4])
            school_program_ammmb3_right.insert(INSERT,hour_7[5])
            print(hour_7)
        school_program_ammmt0_right.config(state=DISABLED)#SO HOURS WONT BE ABLE TO BE CHANGED
        

    def add_school_program():
        global selected_row
        global hour_1
        global hour_2
        global hour_3
        global hour_4
        global hour_5
        global hour_6
        global hour_7

        if(selected_row!=None):
            #delete row
            cal_program.delete(selected_row)
            #GET TEXT INPUTS FROM TEXT LABEL
            hour_add = school_program_ammmt0_right.get("1.0",'end-1c')
            monday_add = school_program_ammmt_right.get("1.0",'end-1c')
            tuesday_add = school_program_ammmm_right.get("1.0",'end-1c')
            wednesday_add = school_program_ammmb_right.get("1.0",'end-1c')
            thursday_add = school_program_ammmb2_right.get("1.0",'end-1c')
            friday_add = school_program_ammmb3_right.get("1.0",'end-1c')
            #replace row
            if(selected_row==0):
                hour_1=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(0,*hour_1)
            elif(selected_row==1):
                hour_2=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(1,*hour_2)
            elif(selected_row==2):
                hour_3=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(2,*hour_3)
            elif(selected_row==3):
                hour_4=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(3,*hour_4)
            elif(selected_row==4):
                hour_5=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(4,*hour_5)
            elif(selected_row==5):
                hour_6=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(5,*hour_6)
            elif(selected_row==6):
                hour_7=[hour_add,monday_add,tuesday_add,wednesday_add,thursday_add,friday_add]
                cal_program.insert(6,*hour_7)
            print("school program added")
            cal_program.selection_clear()
            #DELETE OLD TEXT INPUTS
            school_program_ammmt0_right.delete('1.0', END)
            school_program_ammmt_right.delete('1.0', END)
            school_program_ammmm_right.delete('1.0', END)
            school_program_ammmb_right.delete('1.0', END)
            school_program_ammmb2_right.delete('1.0', END)
            school_program_ammmb3_right.delete('1.0', END)
            selected_row=None#αρχικοποίηση για να μπορουν να δουλέψουν τα pop ups
        else:
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ επιλέξτε μία σχολική ώρα για προσθήκη',icon='warning')

    def delete_school_program():
        global selected_row
        global hour_1
        global hour_2
        global hour_3
        global hour_4
        global hour_5
        global hour_6
        global hour_7

        if(selected_row!=None):
            #delete row
            cal_program.delete(selected_row)
            #replace row
            if(selected_row==0):
                hour_1=['08:15-09:00','','','','','']
                print("test")
                cal_program.insert(0,*hour_1)
            elif(selected_row==1):
                hour_2=['09:10-09:50','','','','','']
                cal_program.insert(1,*hour_2)
            elif(selected_row==2):
                hour_3=['10:00-10:40','','','','','']
                cal_program.insert(2,*hour_3)
            elif(selected_row==3):
                hour_4=['10:50-11:30','','','','','']
                cal_program.insert(3,*hour_4)
            elif(selected_row==4):
                hour_5=['11:35-12:15','','','','','']
                cal_program.insert(4,*hour_5)
            elif(selected_row==5):
                hour_6=['12:20-13:00','','','','','']
                cal_program.insert(5,*hour_6)
            elif(selected_row==6):
                hour_7=['13:05-13:40','','','','','']
                cal_program.insert(6,*hour_7)

            #DESELECT CURRENT ROW
            cal_program.selection_clear()
            #Editeble HOUR AT TEXT
            school_program_ammmt0_right.config(state=NORMAL)
            #DELETE OLD TEXT INPUTS
            school_program_ammmt0_right.delete('1.0', END)
            school_program_ammmt_right.delete('1.0', END)
            school_program_ammmm_right.delete('1.0', END)
            school_program_ammmb_right.delete('1.0', END)
            school_program_ammmb2_right.delete('1.0', END)
            school_program_ammmb3_right.delete('1.0', END)
            #MAKE UN EDITABLE AGAIN 
            school_program_ammmt0_right.config(state=DISABLED)
            school_program_ammmt_right.config(state=DISABLED)
            school_program_ammmm_right.config(state=DISABLED)
            school_program_ammmb_right.config(state=DISABLED)
            school_program_ammmb2_right.config(state=DISABLED)
            school_program_ammmb3_right.config(state=DISABLED)     
            selected_row=None#αρχικοποίηση για να μπορουν να δουλέψουν τα pop ups
        else:
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ επιλέξτε μία σχολική ώρα προς διαγραφή!',icon='warning')
        #only delete lessons not hours
        print("school program deleted")

    #add 4 buttons
    btn_add_cal = Button(school_program_amm_bot, text="Προσθήκη", state=NORMAL, command=lambda: add_school_program(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_delete_cal = Button(school_program_amm_bot, text="Διαγραφή", state=NORMAL, command=lambda: delete_school_program(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_confirm_cal = Button(school_program_a_bot, text="Επιβεβαίωση", state=NORMAL, command=lambda: conf_school_program(), bg="green4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_return_cal = Button(school_program_a_bot, text="Επιστροφή", state=NORMAL, command=lambda: raiseNdrop_frame(school_Dates_Frame,previous_frame), bg="red4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    

    #configurations για εβδομαδιαιο προγραμμα
    cal_program.config(columns=titles,headerfont=("Times New Roman (Times)", 20, "bold"),selectmode='single',font=("Times New Roman (Times)", 16, "bold"))
    cal_program.configure(selectcmd=select_cmd)
    cal_program.insert(0,*hour_1)
    cal_program.insert(1,*hour_2)
    cal_program.insert(2,*hour_3)
    cal_program.insert(3,*hour_4)
    cal_program.insert(4,*hour_5)
    cal_program.insert(5,*hour_6)
    cal_program.insert(6,*hour_7)

    
     
    #Εμφάμιση στοιχείων packs
    school_program_all.pack(side=TOP, expand=1, fill=BOTH)#contains all labels
    school_program_a_top.pack(side=TOP, fill=X)#title label
    school_program_a_mid.pack(side=TOP, expand=1, fill=BOTH, pady=20)#middle labels edit etc
    school_program_a_bot.pack(side=TOP, fill=X)#buttons down label
    school_program_am_top.pack(side=TOP, expand=1, fill=BOTH, ipady=20)#calendar
    cal_program.pack(side=TOP, expand=1, fill=BOTH)
    school_program_am_mid.pack(side=TOP, expand=1, fill=BOTH)#edits
    school_program_amm_top.pack(side=TOP, fill=X,  ipady=5)#edit Title
    school_program_amm_mid.pack(side=TOP, expand=1, fill=BOTH)
    school_program_amm_bot.pack(side=TOP, fill=X)

    #Στοιχεία προς επεξεργασία
    #ωρα
    school_program_ammm_top0.pack(side=TOP, fill=X)
    school_program_ammmt0_left.pack(side=LEFT,padx=50)
    school_program_ammmt0_right.pack(side=LEFT)
    #δευτερα
    school_program_ammm_top.pack(side=TOP, fill=X)
    school_program_ammmt_left.pack(side=LEFT,padx=50)
    school_program_ammmt_right.pack(side=LEFT)
    #τριτη
    school_program_ammm_mid.pack(side=TOP, fill=X)
    school_program_ammmm_left.pack(side=LEFT,padx=50)
    school_program_ammmm_right.pack(side=LEFT)
    #τεταρτη
    school_program_ammm_bot.pack(side=TOP, fill=X)
    school_program_ammmb_left.pack(side=LEFT,padx=50)
    school_program_ammmb_right.pack(side=LEFT)

    #πεμπτη
    school_program_ammm_bot2.pack(side=TOP, fill=X)
    school_program_ammmb2_left.pack(side=LEFT,padx=50)
    school_program_ammmb2_right.pack(side=LEFT)

    #παρασκευη
    school_program_ammm_bot3.pack(side=TOP, fill=X)
    school_program_ammmb3_left.pack(side=LEFT,padx=50)
    school_program_ammmb3_right.pack(side=LEFT)

    #εμφάνιση κουμπιών 
    #κουμπια επεξεργασίας
    btn_add_cal.pack(side=RIGHT, padx=100)
    btn_delete_cal.pack(side=RIGHT)
    #κουμπιά μενού
    btn_confirm_cal.pack(side=RIGHT, padx=100)
    btn_return_cal.pack(side=RIGHT)



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
    btn_reg_create = Button(student_reg_am_bot, text="Δημιουργία/Επεξεργασία Εγγραφής", command=lambda: raiseNdrop_frame(school_std_reg_create_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_reg_spectate = Button(student_reg_am_bot, text="Ολοκληρωμένες Εγγραφές", command=lambda: raiseNdrop_frame(school_std_reg_fin_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    #pack-εμφάνιση στοιχείων
    student_reg_all.pack(side = TOP, fill=BOTH, expand=1)
    student_reg_all_top.pack(side = TOP, fill=X, ipady=30)
    student_reg_at_top.pack(side = TOP)
    student_reg_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    student_reg_am_top.pack(side = TOP)
    student_reg_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    #Buttons pack
    btn_reg_create.pack(side = TOP,pady=50)
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
    std_reg_create_all_bot = Label(std_reg_create_all, borderwidth=1, highlightthickness=0, bg="floral white")
    std_reg_create_ab_top = Label(std_reg_create_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include user name

    #ΣΤΟΙΧΕΙΑ ΜΑΘΗΤΗ
    std_reg_create_abt_top1 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student  name 
    std_reg_create_abt_top2 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student  lastname 
    std_reg_create_abt_top3 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student email 
    std_reg_create_abt_top4 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student phone 
    std_reg_create_abt_top5 = Label(std_reg_create_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#info

    std_reg_create_abtltl_l1 = Label(std_reg_create_abt_top1, text='Όνομα*:\t\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l2 = Label(std_reg_create_abt_top2, text='Επώνυμο*:\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l3 = Label(std_reg_create_abt_top3, text='E-mail*:\t\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l4 = Label(std_reg_create_abt_top4, text='Τηλέφωνο:\t',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l5 = Label(std_reg_create_abt_top5, text='(*Υποχρεωτικά πεδία)',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 12, "bold"))
    
    #TEXTS AS INPUTS!!!!!!!!!!!
    std_reg_create_abtltl_r1 = Text(std_reg_create_abt_top1, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    std_reg_create_abtltl_r2 = Text(std_reg_create_abt_top2, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    std_reg_create_abtltl_r3 = Text(std_reg_create_abt_top3, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    std_reg_create_abtltl_r4 = Text(std_reg_create_abt_top4, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))



    std_reg_create_ab_mid = Label(std_reg_create_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include announcements
    std_reg_create_abm_top = Label(std_reg_create_ab_mid, borderwidth=1, highlightthickness=0, bg="floral white")
    std_reg_create_abmt_left = Label(std_reg_create_abm_top, text='Λίστα Εγγραφών: ',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 16, "bold"))#announcement title
    std_reg_create_abmt_right = Text(std_reg_create_abm_top, borderwidth=1, highlightthickness=0, height=1, width=40, bg="floral white",font=("Times New Roman (Times)", 16, "bold"))#announcement title
    std_reg_create_abmt_right.config(state=DISABLED)
    std_reg_create_abm_bot = Label(std_reg_create_ab_mid, bg="floral white")#Listbox
    std_reg_create_ab_bot = Label(std_reg_create_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#ΚΑΤΩ ΠΛΕΥΡΑ ΜΕ ΚΟΥΜΠΙΑ NEXT KAI RETURN
    
    



    def confirm_list_name():
        list_name = std_reg_create_abtltl_r.get('1.0', 'end-1c')
        if (list_name!=""):#Αν δεν ειναι κενο το input
            std_reg_create_abtltl_r.config(state=DISABLED)
            std_reg_create_abmt_right.config(state=NORMAL)
            std_reg_create_abmt_right.insert('1.0',list_name)
            std_reg_create_abmt_right.config(state=DISABLED)#onoma listas
            #koumpia xrhsth
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


    

    def add_user():
        global std_users
        duplicate=0
        std_name = std_reg_create_abtltl_r1.get('1.0', 'end-1c')    #αντι end-1c αν βαλεις σκετο end βαζει στο τέλος newline 
        std_lastname = std_reg_create_abtltl_r2.get('1.0', 'end-1c')
        std_email = std_reg_create_abtltl_r3.get('1.0', 'end-1c')
        std_phone = std_reg_create_abtltl_r4.get('1.0', 'end-1c')
        is_valid = validate_email(std_email,verify=True)#if email exists
        if(is_valid):#αν υπάρχει το email
            #check if email already exists
            for elem in std_users:
                if (elem[3]==std_email):
                    duplicate=1#σαν flag
            if(duplicate==0):
                if (std_name!="" and std_lastname!="" and std_email!=""):
                    #delete inputs
                    std_reg_create_abtltl_r1.delete('1.0', 'end')
                    std_reg_create_abtltl_r2.delete('1.0', 'end')
                    std_reg_create_abtltl_r3.delete('1.0', 'end')
                    std_reg_create_abtltl_r4.delete('1.0', 'end')
                    #αποθηκευση τελικών στοιχείων
                    std_name_ok=std_name
                    std_lastname_ok=std_lastname
                    std_email_ok=std_email
                    #Αν δεν έχει input
                    if(std_phone==""):
                        std_phone_ok="-"
                    else:
                        std_phone_ok=std_phone    
                    info_to_add=[]
                    info_to_add.append("Όνομα: " + std_name_ok)
                    info_to_add.append("Επώνυμο: " + std_lastname_ok)
                    info_to_add.append("E-mail: " + std_email_ok)
                    info_to_add.append("Τηλέφωνο: " + std_phone_ok)
                    student_info = ('  |  '.join(info_to_add))
                    print(student_info)
                    #προσθήκη στοιχείων μαθητη listbox:
                    user_list.insert('end', student_info)#end στην τελευταια open θέση δλδ 0,1,2,3,...   
                else:
                    messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε ορθά τα στοιχεία του μαθητή',icon='warning')
            else:
                messagebox.showinfo('Σφάλμα', 'Υπάρχει ήδη λογαριασμός μαθητή με αυτό το email!\nΠαρακαλώ ελέξυε τα στοιχεία σας και ξαναπροσπαθήστε!',icon='warning')
        else:
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε ένα email που να υπάρχει!',icon='warning')
        

        
        
    def delete_user():
        global login_path
        global login_list
        global std_list_path 
        global std_users
        pending_user_data=[]
        spacer = "  |  "
        std_new = []
        login_new = []
        student_to_remove = [user_list.get(idx) for idx in user_list.curselection()]
        w=1
        while (w<=len(student_to_remove)):
            idx_count=0
            remove_temp=student_to_remove[w-1]
            while idx_count<=user_list.size():
                if(remove_temp==user_list.get(idx_count)):
                    print(idx_count,"idxc")
                    user_list.delete(idx_count)
                idx_count+=1
                    
            w=w+1

        for cur_std_remove in student_to_remove:
            std_data = cur_std_remove.split(spacer)#καθε index σε αυτο το list περιέχει ονομα επώνυμο κλπ στοιχεία με trash strings
            print("stoixeia xrhsth= ",cur_std_remove)
            for sub_data in std_data:
                print("sub_stoixeio=",sub_data)
                splitted_std = sub_data.split(" ")
                pending_user_data.append(splitted_std[1])
                splitted_std.clear()

            email_key = pending_user_data[2]
            pending_user_data.clear()

            for elem in std_users:
                print("\nelem3",elem[3])
                print("\nkey",email_key)
                if elem[3]==email_key:
                    print("email key ",email_key ," found!")
                    std_remove_id=elem[0]
                    print("id of user to remove=",std_remove_id)
                else:
                    std_new.append(elem)#φτιαχνω λίστα που περιέχει όλα τα στοιχεία εκτός από αυτό με το συγκεκριμένο email

            ######std remove and insert modified data
            std_users.clear()
            std_users = std_new.copy()#ωστε το παλιο std να έχει τα data που θέλουμε
            std_new.clear()
            #διαγραφή περιεχομένου  std_list
            del_std_list = open(std_list_path,"w").close()
            write_std = open(std_list_path,"a")
            #insert to std_list.txt
            for new_std_user in std_users:
                new_std_str = ",".join(new_std_user)#ενωση στοιχείων σαν string με κομμα aka username,password,id
                new_std_row = new_std_str + "\n"
                write_std.write(new_std_row)
            write_std.close()

            ##### delete from login specific student user
            for data in login_list:
                login_username = data[0]# retturns current student username πχ std1
                print("\nlogin_username=",login_username)
                if (login_username==std_remove_id):
                    print("\nstd_removed=",login_username)
                else:   #αν δεν είναι το std που ψάχνουμε
                    login_new.append(data)
            
            print("\n\n new lsit =",login_new)
            login_list.clear()
            login_list = login_new.copy()#ωστε το login να μην έχει std
            login_new.clear()
            print("\n\n\nlogin lsit new = ",login_list)
            #διαγραφή περιεχομένου  login
            del_login = open(login_path,"w").close()
            #άνοιγμα εισαγωγής δεδομένων σε αρχείο login
            write_login = open(login_path,"a")
            #insert to login.txt
            for new_login_user in login_list:
                new_login_str = ",".join(new_login_user)#ενωση στοιχείων σαν string με κο��μα aka username,password,id
                new_login_row = new_login_str + "\n"
                write_login.write(new_login_row)
            write_login.close()
        print("\n",student_to_remove)

        #να σπασω από αυτα που επιλέγονται και να πάρω το email σαν Key
        #αν αυτά τα στοιχεία υπάρχουν στην std_list με βάση email kane flag=1 και αφαιρεσε
        #αλλιως print it was'nt saved simple delete from listbox
        #με βάση το email να δώ την std_list να διαγράψω αυτά τα στοιχεία να πάρω το username τους να το αποθηκεύσω σε list και μετά κάνω delete το std_list
        # και μετα να το ανεβάσω πάλι με τα  στοιχεία που αφαιρέσαμε στο std_txt
        #μετα με την λίστα που εχουμε με τα username κανω προσπέλαση το login_list διαγραφω αυτά και μετά προχωράω σε delete txt και ξαναπέρασμα
        #να παρω το email
        #συγκρινε τις δυο λίστες αφάιρεσαι το std ου λείπει και κάνε πάλι insert
        print("deleted a user") 

        

    def confirm_registry():
        global std_counter
        global std_users
        global std_list_path
        global login_path
        global login_list
        spacer='  |  '
        final_user_data=[]
        std_id="5"
        #send email to all students
        #εδω θελουμε μια λίστα που να έχει αποθηκεύσει τα στοιχεία των μαθητών να την τρέχει και να στέλνει email.
        sender_email = "parmenidis.gr@gmail.com"
        sender_password = "tl2020Parme"
        try:
            yag = yagmail.SMTP(user=sender_email, password=sender_password)
            if (user_list.size()>=1):
                    msg_conf_student_user = messagebox.askquestion('Προσοχή!', 'Είστε σίγουροι ότι θέλετε να κάνετε υποβολή δήλωσης με αυτά τα στοιχεία;', icon='warning')
                    if msg_conf_student_user == 'yes':
                        messagebox.showinfo('Oλοκλήρωση', 'Η δήλωση καταχωρήθηκε με επιτυχία!')
                        user_list.select_set(0, 'end')
                        conf_user_list=[user_list.get(idx) for idx in user_list.curselection()]
                        user_list.select_clear(0,'end')
                        #spilt τα στοιχεία για να παίρνουμε μεμονομένα το ονομα επωνυμο κλπ
                        for stoixeio in conf_user_list:
                            existing_std_flag=0#flag για να δω αν υπάρχει ο χρηστης αυτός ήδη
                            user_data = stoixeio.split(spacer) #καθε index σε αυτο το list περιέχει ονομα επώνυμο κλπ στοιχεία με trash strings
                            print("stoixeia xrhsth",user_data)
                            for sub_stoixeio in user_data:
                                print("sub_stoixeio=",sub_stoixeio)
                                splitted_usr = sub_stoixeio.split(" ")
                                final_user_data.append(splitted_usr[1])
                                splitted_usr.clear()

                            #για να μην κάνει insert παλι και αλλάξει password σε υπάρχων χρήστη με βάση το email που είναι μοναδικό
                            print('\n\n\nfinal_user_data=',final_user_data)
                            email_ok = final_user_data[2]
                            for existing_std in std_users:
                                if (existing_std[3]==email_ok):
                                    print("existingtest=",existing_std)
                                    print("emailcmp",email_ok)
                                    existing_std_flag=1
                                    print("skip this user")
                                    print("Δήλωση Μαθητών:",final_user_data)
                                    final_user_data.clear()
                            if(existing_std_flag==0): #αν είναι νεος χρήστης κάνε εισαγωγή
                                name_ok = final_user_data[0]
                                lastname_ok = final_user_data[1]
                                phone_ok = final_user_data[3]
                                password = uuid.uuid4().hex[:10]#random unique 10 digit password will be send via email or phone number
                                username = "std" +str(std_counter+1)# to std_counter περιέχει το max num tou id opote 9eloume +1
                                std_add= username + "," + name_ok + "," + lastname_ok + "," + email_ok + "," + phone_ok
                                std_add_list=std_add.split(",")#για να εινια η μορφη που θέμε που χωρίζεται με κομμα
                                print('\nsossososos\n\n',std_add_list)
                                #add the new students into the array
                                std_users.append(std_add_list)
                                print("\nstd_user_new",std_users)
                                std_counter+=1#αυξηση counter για username

                                #προσθηκη σε login
                                std_login = username + "," + password + "," + std_id
                                std_login_insert = std_login + "\n"
                                write_std_login = open(login_path,"a")#εισαγωγή δεδομένων σε αρχείο login
                                write_std_login.write(std_login_insert)
                                write_std_login.close()
                                #εισαγωγή δεδομένων στην δυναμική λιστα στοιχείων login ,login_list
                                cur_std_login_list = std_login.split(",")
                                print("\cur_std_login_list=",cur_std_login_list)
                                login_list.append(cur_std_login_list)
                                print("\nnew_login_list=",login_list)

                                print("Δήλωση Μαθητών:",final_user_data)
                                final_user_data.clear()#clear list για αρχικοποίηση

                                #send verification email
                                subject='Στοιχεία Χρήστη Για Το Σύστημα Παρμενίδης'
                                e1="Όνομα: " + name_ok
                                e2="Επώνυμο: " + lastname_ok
                                e3="Όνομα χρήστη: " + username
                                e4="Κωδικός Πρόσβασης: " + password
                                e5="E-mail: " + email_ok
                                e6="Αριθμός Επικοινωνίας: " + phone_ok
                                contents = ["Καλώς ορίσατε στο ενιαίο Σύστημα Πανελληνίων Παρμενίδης!","Τα στοιχεία σας είναι τα εξής",e1,e2,e3,e4,e5,e6]
                                reciever=email_ok
                                yag.send(reciever, subject, contents)
                        del_std_users = open(std_list_path,"w").close()#διαγραφή περιεχομένου  λίστας μαθητών
                        write_std = open(std_list_path,"a")#εισαγωγή δεδομένων σε αρχείο λίστας μαθητών
                        #προσπέλαση λίστας και εισαγωγή data στην fake ΒΔ
                        for row in std_users:
                            new_std_list=",".join(row)
                            print("\n\nnewlist",new_std_list)
                            new_std_list = new_std_list + "\n"
                            write_std.write(new_std_list)
                        write_std.close()
               
                    else:
                        messagebox.showinfo('Επιστροφή', 'Παρακαλώ συνεχίστε στην επεξεργασία της λίστας σας!')
                        print("Ακύρωση από χρήστη της δήλωσης λίστας")
            else:
                messagebox.showinfo('Σφάλμα', 'Πρέπει να επιλέξετε προσθέσει τουλάχιστον ένα μαθητή  για την υποβολή της λίστας σας!')
            
        except:
            messagebox.showinfo('Σφάλμα', 'Αδυναμία αποστολής E-mail!')
            print("Error, email was not sent")
        print("registry confirmed")

    def delete_list():
        global login_path
        global login_list
        global std_list_path
        del_msg = messagebox.askquestion('Προσοχή!', 'Είστε σίγουροι ότι θέλετε να διαγράψετε την τρέχουσα λίστα;\n Τα τρέχουσα στοιχεία της λίστας θα διαγραφτούν μόνιμα αν δεν τα έχετε υποβάλει!', icon='warning')
        if del_msg == 'yes':
            user_list.delete(0,'end')
            new_login_list=[]
            for data in login_list:
                login_username = list(data[0])# retturns list with splited each letter id πχ['s','t','d','1']
                print("\nlogin_username=",login_username)
                if (login_username[0]=="s" and login_username[1]=="t" and login_username[2]=="d"):
                    print("\nstd_removed=",data)
                else:   #αν δεν είναι std
                    new_login_list.append(data)

            print("\n\n new lsit =",new_login_list)
            login_list.clear()
            login_list = new_login_list.copy()#ωστε το login να μην έχει std
            new_login_list.clear()
            print("\n\n\nlogin lsit new = ",login_list)
            #διαγραφή περιεχομένου  std_list
            del_std_list = open(std_list_path,"w").close()
            #διαγραφή περιεχομένου  login
            del_login = open(login_path,"w").close()
            #άνοιγμα εισαγωγής δεδομένων σε αρχείο login
            write_login = open(login_path,"a")
            #insert to login.txt
            for new_login_user in login_list:
                new_login_str = ",".join(new_login_user)#ενωση στοιχείων σαν string με κομμα aka username,password,id
                new_login_row = new_login_str + "\n"
                write_login.write(new_login_row)
            write_login.close()

            #αδειασμα text inputs
            std_reg_create_abtltl_r1.delete('1.0', END)
            std_reg_create_abtltl_r2.delete('1.0', END)
            std_reg_create_abtltl_r3.delete('1.0', END)
            std_reg_create_abtltl_r4.delete('1.0', END)
            print("deleted list")
        else:
           messagebox.showinfo('Επιστροφή', 'Παρακαλώ συνέχίστε με την συμπλήρωση της λίστας!',icon='warning') 
    
    #ORISMOS BTNS
    btn_reg_create_return = Button(std_reg_create_ab_bot, text="Επιστροφή", command=lambda: raiseNdrop_frame(school_std_reg_Frame,previous_frame), bg="red4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_reg_create_confirm = Button(std_reg_create_ab_bot, text="Επιβεβαίωση", state=NORMAL, command=lambda: confirm_registry(),bg="green4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_reg_delete_list = Button(std_reg_create_ab_bot, text="Διαγραφή Λίστας", state=NORMAL, command=lambda: delete_list(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)
    btn_reg_add = Button(std_reg_create_ab_top, text="Προσθήκη Εγγραφής", state=NORMAL, command=lambda: add_user(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=17)
    btn_reg_delete = Button(std_reg_create_ab_top, text="Διαγραφή Εγγραφής", state=NORMAL, command=lambda: delete_user(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=17)

    #orismos listbox sos sos edw 8elei tkinterctrl
    user_list  = Listbox (std_reg_create_abm_bot, bg="floral white", borderwidth=2, highlightthickness=0, selectmode='multiple', export=FALSE, activestyle=none)
    
    scrollh_usr = Scrollbar(std_reg_create_abm_bot, orient="horizontal", command=user_list.xview)
    scrollv_usr= Scrollbar(std_reg_create_abm_bot, orient="vertical", command=user_list.yview)
    std_reg_create_abm_bot.bind("<Configure>",lambda e: user_list.configure(scrollregion=user_list.bbox("all")))
    user_list.configure(yscrollcommand=scrollv_usr.set, xscrollcommand=scrollh_usr.set, font=("Times New Roman (Times)", 16,"bold"))
    std_reg_create_abm_bot.bind("<MouseWheel>", scrollv_usr)#ΚΑΘΕΤΟ SCROLL ΜΕ ΡΟΔΑ ΠΟΝΤΙΚΙΟΥ 

    #συναρτηση για check λίστας και εμφάνιση-γέμισαμ στοιχείων από μνήμη
    def check_std_list(alist):
        spacer="  |  "
        for std in alist:
            std_info = "Όνομα: " + std[1]+ spacer + "Επώνυμο: " + std[2] + spacer + "E-mail: " + std[3] + spacer + "Τηλέφωνο: " +std[4]
            user_list.insert('end', std_info)#end στην τελευταια open θέση δλδ 0,1,2,3,..

    check_std_list(std_users)

    #packs εμφάνιση στοιχείων
    std_reg_create_all.pack(side=TOP,fill=BOTH,expand=1)#δεξιο μενου-αρχικη σελίδα
    std_reg_create_all_top.pack(side=TOP,fill=X)

    std_reg_create_all_bot.pack(side=TOP, expand=1, fill=BOTH,pady=30)
    std_reg_create_ab_top.pack(side=TOP, fill=X)#expand=1
    
    #αριστερη πλευρα με  στοιχεια εγγραφης
    std_reg_create_abt_top1.pack(side=TOP, fill=X)
    std_reg_create_abt_top2.pack(side=TOP, fill=X)
    std_reg_create_abt_top3.pack(side=TOP, fill=X)
    std_reg_create_abt_top4.pack(side=TOP, fill=X)
    std_reg_create_abt_top5.pack(side=TOP, fill=X)

    std_reg_create_abtltl_l1.pack(side=LEFT, padx=50)#ονομα
    std_reg_create_abtltl_l2.pack(side=LEFT, padx=50)#επωνυμο
    std_reg_create_abtltl_l3.pack(side=LEFT, padx=50)#e-mail
    std_reg_create_abtltl_l4.pack(side=LEFT, padx=50)#τηλ επικ
    std_reg_create_abtltl_l5.pack(side=LEFT, padx=50)#info

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

    #κατω πλευρα με buttons σελιδας
    std_reg_create_ab_bot.pack(side= TOP, fill=X)

    #buttons MENU
    btn_reg_create_confirm.pack(side=RIGHT, padx=50)
    btn_reg_create_return.pack(side=RIGHT)
    btn_reg_add.pack(side=RIGHT, padx=50)
    btn_reg_delete.pack(side=RIGHT) 
    btn_reg_delete_list.pack(side=LEFT, padx=50) 

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #school_std_reg_fin_Frame
    
    
    student_reg_fin_all = Label(school_std_reg_fin_Frame, bg="floral white")
    student_reg_fin_a_bot = Label(student_reg_fin_all, bg="floral white")
    
    btn_reg_spectate = Button(student_reg_fin_a_bot, text="Επιστροφή", command=lambda: raiseNdrop_frame(school_std_reg_Frame,previous_frame), bg="red4",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=15)

    #packs

    student_reg_fin_all.pack(side = TOP, expand=1, fill=BOTH)
    student_reg_fin_a_bot.pack(side=BOTTOM, fill=X)
    btn_reg_spectate.pack(side=RIGHT, padx=100)

    main_window.mainloop()  # ------------------------------Put always to end of frames

memory()
main()
