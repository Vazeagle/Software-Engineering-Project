import os, sys
from Classes import *
from Classes import Lesson,Orientation,Direction,Department,Student,School,Board
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

#region Classes
physics = Lesson("Φυσική")
chemistry = Lesson("Χημεία")
language = Lesson("Νεοελληνική Γλώσσα και Λογοτεχνία")
math_dir = Lesson("Μαθηματικά Κατεύθυνσης")
biology = Lesson("Βιολογία")
history = Lesson("Ιστορία")
ancient = Lesson("Αρχαία Ελλήνικα")

positive = Direction("Θετική",[physics,chemistry,language])
theoritical = Direction("Θεωρητική",[history,ancient,language])

pos_sciences = Orientation("Θετικών Επιστημών",positive,math_dir)
med_sciences = Orientation("Επιστήμες Υγείας",positive,biology)

orientations = [med_sciences,pos_sciences]

departments =[]
department = Department(
    "Τμήμα Μηχανικών Η\Υ και πληροφορικής",
    [pos_sciences],
    "Πανεπιστήμιο Πατρών",
    "Πάτρα",
    14012
)
departments.append(department)

department = Department(
    "Χημικό",
    [pos_sciences,med_sciences],
    "ΕΚΠΑ",
    "Αθήνα",
    17523
)
departments.append(department)

#departments.append(Department("Φυσικο(Αθήνας)",[pos_sciences]))
# departments.append(Department("Φυσικο(Πάτρας)",[pos_sciences]))
# departments.append(Department("Χημικό(Αθήνας)",[med_sciences]))
# departments.append(Department("Χημικό(Πάτρας)",[med_sciences]))
# departments.append(Department("Μαθηματικό(Αθήνας)",[pos_sciences]))
# departments.append(Department("Μαθηματικό(Πάτρας)",[pos_sciences]))

students = []
student = Student(1,"ΣΤΥΛΙΑΝΟΣ ΒΑΖΑΙΟΣ", positive, [pos_sciences] , School("1ο Λύκειο Καισαριανής",None,None,None), [],[])
students.append(student)
student = Student(2,"ΖΗΣΗΣ-ΣΤΥΛΙΑΝΟΣ ΤΡΑΜΠΑΡΗΣ", positive, [pos_sciences] , School("12ο Λύκειο Πάτρων",None,None,None), [],[])
students.append(student)
student = Student(3,"ΠΑΝΑΓΙΩΤΗΣ ΣΤΑΥΡΟΠΟΥΛΟΣ", positive, [pos_sciences] , School("2ο Λύκειο Πάτρων",None,None,None), [],[])
students.append(student)
student = Student(4,"ΦΩΤΕΙΝΉ ΣΤΕΡΓΙΟΠΟΎΛΟΥ", positive, [pos_sciences] , School("3ο Λύκειο Φαρσάλων",None,None,None), [],[])
students.append(student)
student = Student(5,"ΑΝΑΣΑΣΙΑ ΣΒΙΓΓΟΥ", positive, [pos_sciences] , School("1ο Λύκειο Κλειτορίας",None,None,None), [],[])
students.append(student)
student = 0

applications = []

pen = "Pending"
rej = "Rejected"
appr = "Sapproved"

data =	{
    "name"       :  "Στυλιανός",
    "surname"    :  "Βαζαίος",
    "fname"      :  "Μπάμπης",
    "fsurname"   :  "Βαζαίος",
    "mname"      :  "Καλιοπη",
    "msurname"   :  "Βαζαιου",
    "bday"       :  "01/04/1998"
}
applications.append(Application(students[0],data,pen))

data =	{
    "name"       :  "Ζήσης-Στυλιανός",
    "surname"    :  "Τράμπαρης",
    "fname"      :  "Αναστάσιος",
    "fsurname"   :  "Τράμπαρης",
    "mname"      :  "Αναστασία",
    "msurname"   :  "Μαγεράκη",
    "bday"       :  "06/12/1998"
}
applications.append(Application(students[1],data,appr))

data =	{
    "name"       :  "Πάνος",
    "surname"    :  "Σταυρόπουλος",
    "fname"      :  "Θεοδωρος",
    "fsurname"   :  "Σταυρόπουλος",
    "mname"      :  "Αγγελική",
    "msurname"   :  "Καλαποδη",
    "bday"       :  "14/06/1998"
}
applications.append(Application(students[2],data,pen))

data =	{
    "name"       :  "Φωτείνη",
    "surname"    :  "Στεργιοπούλου",
    "fname"      :  "Βασίλης",
    "fsurname"   :  "Στεργιόπουλος",
    "mname"      :  "Μαρία",
    "msurname"   :  "Παπα",
    "bday"       :  "03/09/1998"
}
applications.append(Application(students[3],data,rej))

data =	{
    "name"       :  "Ανναστασία",
    "surname"    :  "Σβίγκου",
    "fname"      :  "Μήτσος",
    "fsurname"   :  "Σβίγκος",
    "mname"      :  "Ιωάννα",
    "msurname"   :  "Μητσοτάκη",
    "bday"       :  "22/02/1896"
}
applications.append(Application(students[4],data,pen))

data =	{
    "name"       :  "",
    "surname"    :  "",
    "fname"      :  "",
    "fsurname"   :  "",
    "mname"      :  "",
    "msurname"   :  "",
    "bday"       :  ""
}
appState = ""

applicationsx = []
department = departments[0]
seats = 100
reasoning = "ANNNNNNNNNNNNNNASTASIA SBINGKOU"
applicationsx.append(curDepartment.positionsub(seats,"-",reasoning,"Tubby.pdf"))

department = departments[1]
seats = 50
reasoning = "Αφού πάρθηκε η απόφαση της Κεντρικής Επιτροπής Μεταγωγών για να γυρίσει ο Βασίλης Δημάκης στο κελί του καθώς και μετά την ανακοίνωση του συνηγόρου του ότι προτίθεται να κινηθεί ποινικά για συκοφαντική δυσφήμιση απέναντι στα ψέματα του υπουργείου, η γενική γραμματέας Αντεγκληματικής Πολιτικής, Σοφία Νικολάου, εξέδωσε μια λιτή ανακοίνωση στην οποία παραδέχεται ότι ήταν ανακριβής η πληροφορία που το ίδιο το Υπουργείο Προστασίας του Πολίτη είχε υποστηρίξει, όταν χρέωνε στον Δημάκη ληστείες με Καλάσνικοφ. "
applicationsx.append(curDepartment.positionsub(seats,"-",reasoning,"Old.pdf"))

curApplicationx = Seatsapp(Department("Τμήμα",None,None,None,None),"-","-","","")

events = [
    calEvent("12/05/2020","Pliz work","Pliiiiz")
]
board = Board("12/6/2002","",Cal(events))

#endregion


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

####################################  DHLWSH
folder_path_list= StringVar()#label_graderslist
folder_path_list.set("")






####classes#####

#cur_Admin="Γεώργιος Δημητρόπουλος"

######################


#region frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="floral white")
application_Frame=Frame(all_Frame, bg="floral white")
pending_applic_Frame=Frame(all_Frame, bg="floral white") #aitiseis
applic_verify_Frame=Frame(all_Frame, bg="floral white")#pendingaitiseis
states_Frame=Frame(all_Frame, bg="floral white")#theseis
statement_Frame4=Frame(all_Frame, bg="floral white")#dhmiourgia
Panhellenic_Frame=Frame(all_Frame, bg="floral white")#panellhnies
panexams_program_Frame=Frame(all_Frame, bg="floral white")
department_Frame=Frame(all_Frame, bg="floral white")#programma
department_submit_Frame=Frame(all_Frame, bg="floral white")#eksetastiko kentro
graderslist_frame=Frame(all_Frame, bg="floral white") #vathmologites
acceptdeny_frame=Frame(all_Frame, bg="floral white") #apodoxi aporripsi 
processing_frame=Frame(all_Frame, bg="floral white") #epeksergasia
problems_frame=Frame(all_Frame, bg="floral white") #provlimata
exit_frame=Frame(all_Frame, bg="floral white") #eksodos
list_Frame=Frame(pending_applic_Frame,bg="white")
accept_Frame=Frame(pending_applic_Frame, bg="white")
dep_Frame = Frame()
list_Framex = Frame()
#endregion

folder_path_list = StringVar()#(ypovoli programmatos)
folder_path_list.set("")

def listsort(list):
    list.sort(key=lambda x: x.status)

def lsfrm():
    list_up = Label(list_Frame,bg="white",text ="Αιτήσεις:",font=("Calibri", 24, "bold"))
    list_left = Label(list_Frame, bg="white",font=("Calibri", 24, "bold")) 
    application_list = Listbox (list_left,width = 32, bg="white",font=("Calibri", 15, "bold"))

    scrollbar= Scrollbar(list_left, orient="vertical", command=application_list.yview)
    application_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    list_Frame.pack(side=LEFT,fill='y')
    list_up.pack(side = TOP)
    list_left.pack(side=LEFT, fill=BOTH, expand=1)
    application_list.pack(side=LEFT, fill=BOTH, expand=1)

    listsort(applications)

    for i in range(len(applications)):
        item = str(applications[i].student.name) + " #" + str(applications[i].student.id)
        application_list.insert(END, item )
        if applications[i].status is pen:
            application_list.itemconfig(END, {'bg':'yellow'})
        if applications[i].status is appr:
            application_list.itemconfig(END, {'bg':'green'})
        if applications[i].status is rej:
            application_list.itemconfig(END, {'bg':'red'})

    def onselect(evt):
        global accept_Frame
        global data
        global appState
        global curApplication 
        curApplication = applications[application_list.curselection()[0]]
        data = curApplication.data
        appState = curApplication.status
        accept_Frame.destroy()
        accept_Frame=Frame(pending_applic_Frame, bg="white")
        accfrm()
        
    application_list.bind('<<ListboxSelect>>', onselect)
lsfrm()

def edit_app(state):
    global curApplication
    global list_Frame
    global accept_Frame
    if state == "accept":
        curApplication.status = appr
    else:
        curApplication.status = rej
    list_Frame.destroy()
    list_Frame=Frame(pending_applic_Frame, bg="white")
    accept_Frame.destroy()
    accept_Frame=Frame(pending_applic_Frame, bg="white")
    lsfrm()
    accfrm()

def accfrm():
    folder_path_form = StringVar()#(label_Statement1_all_mt8l_left)
    folder_path_ID = StringVar()#(label_Statement1_all_mt9l_left)
    folder_path_form.set("")
    folder_path_ID.set("")

    def openapp(event):
        os.startfile("Tubby.pdf")

    def openid(event):
        os.startfile("Old.pdf")

    label_Statement1_all = Label(accept_Frame, bg="floral white")
    label_Statement1_all_top = Label(label_Statement1_all, text="Δήλωση Συμμετοχής",  bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    label_Statement1_all_mid_top = Label(label_Statement1_all, relief="groove", borderwidth=2, highlightthickness=2,  bg="floral white")
    label_Statement1_all_down = Label(label_Statement1_all, bg="floral white")

    label_Statement1_all_m_t1 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt1_left = Label(label_Statement1_all_m_t1, text="Όνομα: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_name = Label(label_Statement1_all_m_t1, text=data["name"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t2 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt2_left = Label(label_Statement1_all_m_t2, text="Επώνυμο: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_surname = Label(label_Statement1_all_m_t2, text=data["surname"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t3 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt3_left = Label(label_Statement1_all_m_t3, text="Ημερομηνία Γέννησης: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_bday = Label(label_Statement1_all_m_t3, text=data["bday"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t4 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt4_left = Label(label_Statement1_all_m_t4, text="Όνομα Πατρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_Fname = Label(label_Statement1_all_m_t4, text=data["fname"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t5 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt5_left = Label(label_Statement1_all_m_t5, text="Επώνυμο Πατρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_Fsurname = Label(label_Statement1_all_m_t5, text=data["fsurname"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t6 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt6_left = Label(label_Statement1_all_m_t6, text="Όνομα Μητρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_Mname = Label(label_Statement1_all_m_t6, text=data["mname"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t7 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt7_left = Label(label_Statement1_all_m_t7, text="Επώνυμο Μητρός: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_Msurname = Label(label_Statement1_all_m_t7, text=data["msurname"],  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t77 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt77_left = Label(label_Statement1_all_m_t77, text="Κατάσταση αίτησης: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    info_text_State = Label(label_Statement1_all_m_t77, text=appState,  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")

    label_Statement1_all_m_t8 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt8_left = Label(label_Statement1_all_m_t8, text="Αίτηση Συμμετοχής: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    label_Statement1_all_mt8l_left =  Label(label_Statement1_all_m_t8, text="Δήλωση",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="blue",cursor="hand2")
    label_Statement1_all_mt8l_left.bind("<Button-1>", lambda e:openapp(e))

    label_Statement1_all_m_t9 = Label(label_Statement1_all_mid_top, bg="floral white")
    label_Statement1_all_mt9_left = Label(label_Statement1_all_m_t9, text="Αστυνομική Ταυτότητα: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    label_Statement1_all_mt9l_left = Label(label_Statement1_all_m_t9, text="Ταυτότητα",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="blue",cursor="hand2")
    label_Statement1_all_mt9l_left.bind("<Button-1>", lambda e:openid(e))

    btn_accept = Button(label_Statement1_all_down, text="Αποδοχή", command=lambda: edit_app("accept"), bg="green3",font=("Calibri", 14, "bold"),height=1 ,width=12)
    btn_reject = Button(label_Statement1_all_down, text="Απόριψη", command=lambda: edit_app("reject"), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)

    accept_Frame.pack(side = LEFT,fill=BOTH,expand =1)

    label_Statement1_all.pack(side=TOP, expand=1, fill=BOTH)
    label_Statement1_all_top.pack(side=TOP)
    label_Statement1_all_mid_top.pack(side=TOP, expand=1,fill=BOTH, pady=0)
    label_Statement1_all_down.pack(side=TOP, expand=1,fill=BOTH)

    label_Statement1_all_m_t1.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt1_left.pack(side=LEFT,padx=10)
    info_text_name.pack(side=LEFT)

    label_Statement1_all_m_t2.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt2_left.pack(side=LEFT,padx=10)
    info_text_surname.pack(side=LEFT)

    label_Statement1_all_m_t3.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt3_left.pack(side=LEFT,padx=10)
    info_text_bday.pack(side=LEFT)

    label_Statement1_all_m_t4.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt4_left.pack(side=LEFT,padx=10)
    info_text_Fname.pack(side=LEFT)

    label_Statement1_all_m_t5.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt5_left.pack(side=LEFT,padx=10)
    info_text_Fsurname.pack(side=LEFT)

    label_Statement1_all_m_t6.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt6_left.pack(side=LEFT,padx=10)
    info_text_Mname.pack(side=LEFT)

    label_Statement1_all_m_t7.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt7_left.pack(side=LEFT,padx=10)
    info_text_Msurname.pack(side=LEFT)

    label_Statement1_all_m_t77.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt77_left.pack(side=LEFT,padx=10)
    info_text_State.pack(side=LEFT)

    label_Statement1_all_m_t8.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt8_left.pack(side=LEFT,padx=10)
    label_Statement1_all_mt8l_left.pack(side=LEFT)

    label_Statement1_all_m_t9.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
    label_Statement1_all_mt9_left.pack(side=LEFT,padx=10)
    label_Statement1_all_mt9l_left.pack(side=LEFT)

    btn_accept.pack(side=LEFT)
    btn_reject.pack(side=LEFT)
accfrm()



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
    butttonNext1 = Button(label_l_down, text="Αιτήσεις", command=lambda: raiseNdrop_frame(pending_applic_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2 = Button(label_l_down, text="Θέσεις Τμημάτων", command=lambda: raiseNdrop_frame(department_submit_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
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




    ############################# SINARTISI############

    



    # -------------------------------First Frame END, Start of ΑΙΤΗΣΕΙΣ------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    global dep_Frame
    global list_Framex
    department_sumbit= Label(department_submit_Frame, bg="floral white")
    department_sumbit_at_top = Label(department_sumbit, bg="floral white")
    department_sumbit_at_mid =  Label(department_sumbit, bg="floral white")
    

    list_Framex=Frame(department_sumbit_at_top,bg="white")
    dep_Frame=Frame(department_sumbit_at_top, bg="white")

    def listsortx(list):
        list.sort(key=lambda x: (x.fseats,x.department.name))

    def lsfrm():
        list_up = Label(list_Framex,bg="white",text ="Προτάσεις:",font=("Calibri", 24, "bold"))
        list_left = Label(list_Framex, bg="white",font=("Calibri", 24, "bold")) 
        application_list = Listbox (list_left,width = 20, bg="white",font=("Calibri", 15, "bold"))

        scrollbary= Scrollbar(list_left, orient="vertical", command=application_list.yview)
        scrollbarx= Scrollbar(list_left, orient="horizontal", command=application_list.xview)
        application_list.configure(xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.pack(side=BOTTOM, fill=X)

        list_Framex.pack(side=LEFT,fill='y')
        list_up.pack(side = TOP)
        list_left.pack(side=LEFT, fill=BOTH, expand=1)
        application_list.pack(side=LEFT, fill=BOTH, expand=1)

        listsortx(applicationsx)

        for i in range(len(applicationsx)):
            if applicationsx[i].fseats == "-":
                item = str(applicationsx[i].department.name) + ": " + str(applicationsx[i].rseats)
                application_list.insert(END, item )
                application_list.itemconfig(END, {'bg':'yellow'})
            else:
                item = str(applicationsx[i].department.name) + ": " + str(applicationsx[i].fseats)
                application_list.insert(END, item )
                application_list.itemconfig(END, {'bg':'green'})
            

        def onselectx(evt):
            global dep_Frame
            global curApplicationx
            print(application_list.curselection()[0])
            curApplicationx = applicationsx[application_list.curselection()[0]]
            dep_Frame.destroy()
            dep_Frame=Frame(department_sumbit_at_top, bg="white")
            depfrm()
            
        application_list.bind('<<ListboxSelect>>', onselectx)
    lsfrm()

    def sinput(seats):
        global curApplicationx
        global list_Framex
        global dep_Frame
        
        curApplicationx.fseats = seats
        list_Framex.destroy()
        list_Framex=Frame(department_sumbit_at_top,bg="white")
        dep_Frame.destroy()
        dep_Frame=Frame(department_sumbit_at_top, bg="white")
        lsfrm()
        depfrm()

    def depfrm():
        label_all = Label(dep_Frame, bg="floral white")

        label_up = Label(label_all, bg="floral white")

        label_head = Label(label_up, text=curApplicationx.department.name,  bg="floral white",font=("Times New Roman (Times)", 25, "bold"),fg="dodger blue")
        label_pos = Label(label_up, bg="floral white")
        
        label_req = Label(label_pos,bg = "floral white")
        label_req_tex = Label(label_req,text = "Προτεινόμενες θέσεις: "+str(curApplicationx.rseats),font=("Times New Roman (Times)", 18, "bold"),fg="black",bg="floral white")
        label_final = Label(label_pos, bg = "floral white")
        label_finseat = Label(label_final,text = "Τελικές Θέσεις: ",font=("Times New Roman (Times)", 18, "bold"),fg="black",bg="floral white")
        label_finseatin = Entry(label_final, bg="WHITE", fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
        label_finseatin.insert(0,curApplicationx.fseats)
        button = Button(label_final, text="Καταχώρηση", command=lambda: sinput(label_finseatin.get()), bg="green3",font=("Calibri", 14, "bold"),height=1 ,width=12)

        label_application_file  = Label(label_pos, bg = "floral white")
        label_application_file1 = Label(label_application_file, text="Αρχείο: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        label_application_file2 =  Label(label_application_file,text = curApplicationx.file, bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="blue",cursor="hand2")
        label_application_file2.bind("<Button-1>", lambda e:open(e))
        
        def open(event):
            os.startfile(curApplicationx.file)

        label_bottom = Label(label_all,  bg="floral white",font=("Times New Roman (Times)", 25, "bold"))
        
        label_text_resup = Label(label_bottom, bg="floral white")
        label_text_res = Label(label_text_resup,text = "Αιτιολογία:",font=("Times New Roman (Times)", 18, "bold"),fg="black",bg="floral white")

        label_reasoning = Text(label_bottom, bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        label_reasoning.insert(END, curApplicationx.reasoning)
        label_reasoning.config(state=DISABLED)


        dep_Frame.pack(side = LEFT,fill=BOTH,expand =1)

        label_all.pack(side = TOP, fill = BOTH, expand =1)
        
        label_up.pack(side = TOP,fill = 'x')
        label_bottom.pack(side = BOTTOM)

        label_head.pack(side = TOP)
        label_pos.pack(side = LEFT,fill = 'x')

        label_req.pack(side = TOP,fill = 'x')
        label_req_tex.pack(side = LEFT)
        label_final.pack(side = TOP)
        label_finseat.pack(side = LEFT)
        label_finseatin.pack(side = LEFT)

        label_application_file.pack(side=TOP)
        label_application_file1.pack(side=LEFT)
        label_application_file2.pack(side=LEFT)

        button.pack(side = LEFT)

        label_text_resup.pack(side=TOP,fill='x')
        label_text_res.pack(side = LEFT)

        label_reasoning.pack(side=TOP,fill='x',pady="10px")
    depfrm()


    department_date_lbl = Label(department_sumbit_at_mid, bg="floral white")
    department_date_0 = Label(department_date_lbl, text="Νεα Ημερομηνία: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    department_date_l = Label(department_date_lbl, bg="floral white")
    department_date_2 = Label(department_date_lbl, bg="floral white")
    department_date_3 = Label(department_date_lbl, bg="floral white")
    department_date_space1 = Label(department_date_lbl, text="/",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    department_date_space2 = Label(department_date_lbl, text="/",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    department_sumbit_at_bottom = Label(department_date_lbl, bg="floral white")
    
    buttton_accept_date = Button(department_sumbit_at_bottom, text="Αποδοχή", command=lambda: accept_date(), bg="green",font=("Calibri", 14, "bold"),height=1 ,width=12)
    #buttton_back_to_department = Button(department_sumbit_at_bottom, text="Επιστροφή", command=lambda: raiseNdrop_frame(department_Frame,previous_frame), bg="gray",font=("Calibri", 14, "bold"),height=1 ,width=12)
    
    #ΠΡΟΧΕΙΡΗ ΤΟΠΟΘΕΤΗΣΗ ΣΥΝΑΡΤΗΣΗΣ----------------------------------------------------------
    def accept_date():
        msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να είναι αυτή η ημερομηνία;',icon='warning')
        if msg_confirmation == 'yes':
            messagebox.showinfo('Oλοκλήρωση', 'Η ημερομηνία έγινε δεκτή με επιτυχία!')
            board.seatsDue = str(date_val.get()) + "/" + str(month_val.get()) + "/" + str(year_val.get())
            raiseNdrop_frame(menu_Frame,none) ###ενδεχομενως να βαλουμε εδω να διαγραφεται η αιτηση και να πηγαινει στο ιστορικο
        else:
            raiseNdrop_frame(department_submit_Frame,none)
 
    
    datetime_initialise()#kalesma synarthshs gia hmeromhnia
    dates = board.seatsDue.split("/")

    date_val = StringVar(department_date_l)
    date_val.set(date_options[date_options.index(int(dates[0]))])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    date_choice = OptionMenu(department_date_l, date_val, *date_options)
    date_choice.config(bg="snow",width=5)

    month_val = StringVar(department_date_2)
    month_val.set(month_options[month_options.index(int(dates[1]))])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    month_choice = OptionMenu(department_date_2, month_val, *month_options)
    month_choice.config(bg="snow",width=5)


    year_val = StringVar(department_date_3)
    year_val.set(year_options[year_options.index(int(dates[2]))])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    year_choice = OptionMenu(department_date_3, year_val, *year_options)
    year_choice.config(bg="snow",width=5)



    department_sumbit.pack(side=TOP,expand=1,fill=BOTH)
    department_sumbit_at_mid.pack(side=TOP)   
    
    department_sumbit_at_top.pack(side=TOP)
    
    department_date_lbl.pack(side=TOP)
    department_date_0.pack(side=LEFT)
    department_date_l.pack(side=LEFT)
    department_date_space1.pack(side=LEFT)
    department_date_2.pack(side=LEFT)
    department_date_space2.pack(side=LEFT)
    department_date_3.pack(side=LEFT)
    date_choice.pack(side=LEFT)
    month_choice.pack(side=LEFT)
    year_choice.pack(side=LEFT)
    department_sumbit_at_bottom.pack(side=LEFT)

    buttton_accept_date.pack(side=RIGHT,padx=25)
    #buttton_back_to_department.pack(side=RIGHT)



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
    btn_grader = Button(panexams_am_bot, text="Υποβολή Βαθμολογητών", command=lambda: raiseNdrop_frame(graderslist_frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    panexams_all.pack(side=TOP,expand=1,fill=BOTH)

    panexams_all.pack(side = TOP, fill=BOTH, expand=1)
    panexams_all_top.pack(side = TOP, fill=X, ipady=50)
    panexams_at_top.pack(side = TOP)
    panexams_all_mid.pack(side = TOP, fill=BOTH, expand=1, pady=50)
    panexams_am_top.pack(side = TOP)
    panexams_am_bot.pack(side = TOP, fill=BOTH, expand=1)

    btn_exams_program.pack(side = TOP,pady=20)
    btn_grade_center.pack(side = TOP)
    btn_grader.pack(side = TOP,pady=20)

    # # -------------------------------ΠΑΝΕΛΛΗΝΙΕΣ END, Start of ΠΡΟΓΡΑΜΜΑ ΠΑΝΕΛΛΗΝΙΩΝ------------------------
    # #---------------------------------------------------------------------------------------------------
    # #---------------------------------------------------------------------------------------------------
    # #---------------------------------------------------------------------------------------------------
    # #---------------------------------------------------------------------------------------------------
    # #---------------------------------------------------------------------------------------------------
    # #---------------------------------------------------------------------------------------------------

    

    #region Programma
    school_exams_all = Label(panexams_program_Frame, bg="floral white")
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
        event_ids = cal_exams.get_calevents()
        print("events:",event_ids)
        print("school exams confirmed")


    def add_school_exams():
        message = school_exams_ammmt_right.get("1.0",'end-1c')
        reminder = school_exams_ammmm_right.get("1.0",'end-1c')
        date = school_exams_ammmb_right.get("1.0",'end-1c')

        flag=0
        event = calEvent(None,None,None)
        if (date!=""):
            event.date = date
            date_time_obj = datetime.strptime(date, '%d/%m/%Y')
        if(date==""):
            messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε μια ημερομηνία για το μήνυμα ή την υπενθύμιση που θέλετε να προσθέσετε!',icon='warning')
        else:
            if(message!=""):
                event.message = message
                cal_exams.calevent_create(date_time_obj, message, 'message')
            if(reminder!=""):
                event.reminder = reminder
                cal_exams.calevent_create(date_time_obj, reminder, 'reminder')
            if(message=="" and reminder==""):
                flag=1
                messagebox.showinfo('Σφάλμα', 'Παρακαλώ εισάγετε ένα μήνυμα ή υπενθύμιση για την τρέχουσα ημερομηνία και δοκιμάστε να ξανακάνετε προσθήκη!',icon='warning')
        school_exams_ammmt_right.delete('1.0', END)
        school_exams_ammmm_right.delete('1.0', END)
        if(flag==0):
            school_exams_ammmb_right.delete('1.0', END)
        board.examCal.events.append(event)

    def delete_school_exams():
        #cal_exams.selection_clear(cur_exam_date.get())
        date_rem = datetime.strptime(cur_exam_date.get(), '%d/%m/%Y')
        cal_exams.calevent_remove(date=date_rem)
        for i in range(len(board.examCal.events)):
            if board.examCal.events[i].date == cur_exam_date.get():
                del board.examCal.events[i]
        print("school exams selected event deleted")
        cal_exams.selection_clear()

    def delete_school_exams_calendar():
        cal_exams.calevent_remove('all')
        board.examCal.events = []
        print("all school exams calendar events are deleted")

    #add 4 buttons
    btn_add_cal = Button(school_exams_amm_bot, text="Προσθήκη", state=NORMAL, command=lambda: add_school_exams(), bg="red3",font=("Calibri", 16, "bold"))
    btn_delete_cal = Button(school_exams_amm_bot, text="Διαγραφή", state=NORMAL, command=lambda: delete_school_exams(), bg="red3",font=("Calibri", 16, "bold"))
    btn_confirm_cal = Button(school_exams_a_bot, text="Επιβεβαίωση", state=NORMAL, command=lambda: conf_school_exams(), bg="red3",font=("Calibri", 16, "bold"))
    btn_return_cal = Button(school_exams_a_bot, text="Επιστροφή", state=NORMAL, command=lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="red3",font=("Calibri", 16, "bold"))
    btn_delete_cal_all = Button(school_exams_a_bot, text="Διαγραφή Ημερολογίου ", state=NORMAL, command=lambda: delete_school_exams_calendar(), bg="red3",font=("Calibri", 16, "bold"))
    

    #ορισμος ημερολογιου
    cal_exams = Calendar(school_exams_am_top, selectmode='day',textvariable=cur_exam_date, date_pattern='dd/mm/y')
    cal_exams.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')
    
    for i in range(len(board.examCal.events)):
        event = board.examCal.events[i]
        date_time_obj = datetime.strptime(event.date, '%d/%m/%Y')
        cal_exams.calevent_create(date_time_obj, event.message, 'message')
        cal_exams.calevent_create(date_time_obj, event.reminder, 'reminder')
    
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
    #endregion

    # -------------------------------ΠΡΟΓΡΑΜΜΑ ΠΑΝΕΛΛΗΝΙΩΝ END, Start of ΕΠΙΤΗΡΗΤΕΣ---------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    def openls(event):
        os.startfile(board.list)
    def listMk(): 
        global graderslist_frame   
        label_graderslist_all= Label(graderslist_frame,bg="floral white")
        label_graderslist_a_top = Label(label_graderslist_all, bg="floral white")
        label_graderslist_at_top = Label(label_graderslist_a_top, bg="floral white", text=" Υποβολή Λίστας Βαθμολογητών ",font=("Times New Roman (Times)", 36, "bold"),fg="black")
        label_graderslist_file = Label(label_graderslist_a_top,bg="floral white")
        label_graderslist_file_text = Label(label_graderslist_file, bg="floral white", text="Αρχείο",font=("Times New Roman (Times)", 20, "bold"),fg="black")
        label_graderslist_file_file =  Label(label_graderslist_file,width=40, text=board.list,  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="blue",cursor="hand2")
        label_graderslist_file_file.bind("<Button-1>", lambda e:openls(e))

        label_graderslist_at_bottom = Label(label_graderslist_a_top, bg="floral white")
        label_graderslist_a_bottom = Label(label_graderslist_at_bottom, bg="floral white")
        

        btn3_search_list = Button(label_graderslist_a_bottom, text="Αναζήτηση Αρχείου", command=lambda: browse_list(), bg="red3",font=("Calibri", 14, "bold"))
        button_return  = Button(label_graderslist_a_bottom, text="Επιστροφή", command= lambda: raiseNdrop_frame(Panhellenic_Frame,previous_frame), bg="gray",font=("Calibri", 14, "bold"),height=1 ,width=12)


        
        label_graderslist_all.pack(side=TOP,fill=BOTH,expand=1)
        label_graderslist_a_top.pack(side=TOP,fill=BOTH, expand=1)
        label_graderslist_at_top.pack(side=TOP, fill=BOTH, expand=1)
        label_graderslist_file.pack(side=TOP, fill=BOTH, expand=1,pady = 20)
        label_graderslist_file_text.pack(side = LEFT)
        label_graderslist_file_file.pack(side = LEFT,fill = X)
        label_graderslist_at_bottom.pack(side=TOP, fill=BOTH, expand=1, pady=100)
        label_graderslist_a_bottom.pack(side=BOTTOM,fill=X, expand=0, padx=100)
        #btn2_return_program.pack(side=RIGHT)
        btn3_search_list.pack(side=TOP)
        button_return.pack(side=RIGHT)
    listMk()
    def browse_list():  #filedialog documentation  για λεπτομερειες 
    # Allow user to select a file and store it in global variable folder_path_form  και ασφάλεια από λάθος αρχείο
        global folder_path_list
        global graderslist_frame
        filename_form = filedialog.askopenfilename()
        file_type2=filename_form.split(".")
        if(file_type2[-1]=="xls" ): #αν το τελευταιο στοιχειο της λιστας είναι το string xls
            folder_path_list.set(filename_form)
            msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να υποβάλετε αυτό το αρχείο;',icon='warning')
            if msg_confirmation == 'yes':
                messagebox.showinfo('Oλοκλήρωση', 'Επιτυχής υποβολή αρχείου!')
                board.list = filename_form
                graderslist_frame.destroy()
                graderslist_frame=Frame(all_Frame, bg="floral white") 
                listMk()
                raiseNdrop_frame(Panhellenic_Frame,previous_frame) 
            else:
                browse_list()

        else:
            msg_error_form = messagebox.showerror('Πρόβλημα Αρχείου!', 'Παρακαλώ επιλέξτε ένα αρχείο τύπου xls που να περιέχει τα στοιχεία της λίστας σας', icon='warning')
            filename_ID=""


##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()

main()