import os, sys
from datetime import date
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
reasoning = "Αφού πάρθηκε η απόφαση της Κεντρικής Επιτροπής Μεταγωγών για να γυρίσει ο Βασίλης Δημάκης στο κελί του καθώς και μετά την ανακοίνωση του συνηγόρου του ότι προτίθεται να κινηθεί ποινικά για συκοφαντική δυσφήμιση απέναντι στα ψέματα του υπουργείου, η γενική γραμματέας Αντεγκληματικής Πολιτικής, Σοφία Νικολάου, εξέδωσε μια λιτή ανακοίνωση στην οποία παραδέχεται ότι ήταν ανακριβής η πληροφορία που το ίδιο το Υπουργείο Προστασίας του Πολίτη είχε υποστηρίξει, όταν χρέωνε στον Δημάκη ληστείες με Καλάσνικοφ. "
file = "Old.pdf"
applicationsx.append(Seatsapp(department,seats,"-",reasoning,file))

department = departments[0]
seats = 50
reasoning = "Αφού πάρθηκε η απόφαση της Κεντρικής Επιτροπής Μεταγωγών για να γυρίσει ο Βασίλης Δημάκης στο κελί του καθώς και μετά την ανακοίνωση του συνηγόρου του ότι προτίθεται να κινηθεί ποινικά για συκοφαντική δυσφήμιση απέναντι στα ψέματα του υπουργείου, η γενική γραμματέας Αντεγκληματικής Πολιτικής, Σοφία Νικολάου, εξέδωσε μια λιτή ανακοίνωση στην οποία παραδέχεται ότι ήταν ανακριβής η πληροφορία που το ίδιο το Υπουργείο Προστασίας του Πολίτη είχε υποστηρίξει, όταν χρέωνε στον Δημάκη ληστείες με Καλάσνικοφ. "
file = "Tubby.pdf"
applicationsx.append(Seatsapp(department,seats,"-",reasoning,file))

curApplicationx = Seatsapp(Department("Τμήμα",None,None,None,None),"-","-","","")

events = [
    calEvent("12/05/2020","Pliz work","Pliiiiz")
]
board = Board("12/6/2020",Cal(events))
curDepartment = departments[1]
#endregion

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


####################################  DHLWSH
folder_path_file= StringVar()#label_file
folder_path_file.set("")






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

folder_path_list = StringVar()#(ypovoli programmatos)
folder_path_list.set("")



def main():
    
    
    load3 = Image.open(curDepartment.site.logoImage)
    load3 = load3.resize((45, 45), Image.ANTIALIAS)
    render3 = ImageTk.PhotoImage(load3)

    load4 = Image.open(curDepartment.site.coverImage)
    load3 = load3.resize((30, 15), Image.ANTIALIAS)
    render4 = ImageTk.PhotoImage(load4)

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
    label_rddrl_up = Label(label_rddr_left, text=curDepartment.name, borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="floral white")  # katastash
    label_rddrld_left = Label(label_rddrl_down, text="Ίδρυμα: ", borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 14))  # katastash text
    label_rddrld_right = Label(label_rddrl_down, text=curDepartment.university, borderwidth=1, highlightthickness=1, relief="groove",bg="white",font=("Times New Roman (Times)", 14))  # input katastashs apo data base

    descriptionText = Text(label_rul_right, height=8, bg="floral white", fg="gray44", borderwidth=0, highlightthickness=2,font=("Times New Roman (Times)", 12), width=55)
    descriptionText.insert(INSERT,"Ο Παρμενίδης ήταν αρχαίος έλληνας φιλόσοφος. Γεννήθηκε στην \nΕλέα της Μεγάλης Ελλάδας στα τέλη του 6ου αιώνα π.Χ., σε ένα \nπεριβάλλον επηρεασμένο από τις απόψεις του Πυθαγόρα και του Ξενοφάνη. Ο Παρμενίδης υποστήριξε ότι η πολλαπότητα των \nυπάρχοντων πραγμάτων, οι μεταβαλλόμενες μορφές και η κίνηση τους δεν είναι παρά μια εμφάνιση μιας ενιαίας αιώνιας \nπραγματικότητα (<<Όν>>), οδηγώντας έτσι στην παρμενίδια αρχή \nότι <<όλα είναι ένα>>.")
    descriptionText.config(state=DISABLED)#to be un editable

    
    label_left = Label(menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames
    
    #label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    #label_ruu_up = Label(label_right, text="Καλώς ήρθατε!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Calibri", 24, "bold"))

    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1 = Button(label_l_down, text="Θέσεις Επιτυχόντων", command=lambda: raiseNdrop_frame(capacity_submit_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2 = Button(label_l_down, text="Σελίδα Τμήματος", command=lambda: raiseNdrop_frame(page_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
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

    


    

    # -------------------------------ΘΕΣΕΙΣ ΕΠΙΤΥΧΟΝΤΩΝ END, Start of ΥΠΟΒΟΛΗ---------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    def capMk():
        global capacity_submit_Frame
        capacity_submit_all= Label(capacity_submit_Frame, bg="floral white")
        capacity_submit_a_top = Label(capacity_submit_all, bg="floral white")
        capacity_submit_at_top = Label(capacity_submit_a_top, bg="floral white", text="Υποβολή Θέσεων",font=("Times New Roman (Times)", 36, "bold"),fg="black")
        capacity_submit_all_mid =  Label(capacity_submit_all, bg="floral white")
        capacity_submit_am_top = Label(capacity_submit_all_mid, text="Επιλογές: ", bg="floral white",font=("Times New Roman (Times)", 30, "bold"),fg="black")
        capacity_submit_am_bot = Label(capacity_submit_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
        

        capacity_date = Label(capacity_submit_am_bot, text="Ημερομηνία Υποβολής: "+board.seatsDue,  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        capacity_date_check = Label(capacity_submit_am_bot, text="Βάσει ημερομηνίας, η υποβολή είναι:",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        
        if datetime.strptime(board.seatsDue, '%d/%m/%Y')>date.today():
            due = "ΕΦΙΚΤΗ"
        else:
            due = "ΑΝΕΦΙΚΤΗ"

        capacity_date_check1 = Label(capacity_submit_am_bot, text = due, borderwidth=1, highlightthickness=1, relief="groove",bg="floral white",font=("Times New Roman (Times)", 14))
        capacity_submit_check = Label(capacity_submit_am_bot, text="Στο σύστημα υπάρχει αίτηση;",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    
        found = False 
        for i in range(len(applicationsx)):
            if curDepartment == applicationsx[i].department:
                exists = "NAI"
                butOn = "Επεξεργασία Αίτησης"
                curApplicationx = applicationsx[i]
                found = True
                break
        if not found:
            exists = "OXI"
            butOn = "Νεα Αίτηση"
            applicationsx.append(curDepartment.positionsub("","",""))
            curApplicationx = applicationsx[-1]

            
        capacity_submit_check1 = Label(capacity_submit_am_bot, text=exists, borderwidth=1, highlightthickness=1, relief="groove",bg="floral white",font=("Times New Roman (Times)", 14))
        btn_new_submission = Button(capacity_submit_am_bot, text=butOn, command=lambda: raiseNdrop_frame(department_application_Frame,previous_frame), bg="gray26",height = 2, width = 25,font=("Calibri", 14, "bold"))
    

        capacity_submit_all.pack(side=TOP,expand=1,fill=BOTH)
        capacity_submit_a_top.pack(side=TOP)
        capacity_submit_at_top.pack(side=TOP)
        capacity_submit_all_mid.pack(side = TOP, fill=BOTH, expand=1)
        capacity_submit_am_top.pack(side = TOP)
        capacity_submit_am_bot.pack(side = LEFT, fill=BOTH, expand=1)
        
        capacity_date.pack(side=TOP)
        capacity_date_check.pack(side=TOP)
        capacity_date_check1.pack(side=TOP)
        capacity_submit_check.pack(side=TOP)
        capacity_submit_check1.pack(side=TOP)
        
        btn_new_submission.pack(side=TOP)
    capMk()


    # -------------------------------ΥΠΟΒΟΛΗ END, Start of ΝΕΑ ΑΙΤΗΣΗ-----------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    def seatMk():
        global department_application_Frame
        label_department_application_all = Label(department_application_Frame, bg="floral white")
        label_department_application_a_top = Label(label_department_application_all, bg="floral white")
        label_department_application_top = Label(label_department_application_a_top, bg="floral white", text="Δήλωση Θέσεων ",font=("Times New Roman (Times)", 36, "bold"),fg="black")
        label_department_application_mid = Label(label_department_application_all, bg="floral white")
        label_department_application_bottom = Label(label_department_application_all, bg="floral white")
        
        label_application_number = Label(label_department_application_mid, bg="floral white")
        label_application_number1 = Label(label_application_number, text="Υποβολή Αριθμού Θέσεων: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        info_number = Text(label_application_number,bg="WHITE", height=1, width=5, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
        info_number.insert('1.0', curApplicationx.rseats)

        label_application_file = Label(label_department_application_mid, bg="floral white")
        label_application_file1 = Label(label_application_file, text="Υποβολή Αρχείου: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        label_application_file2=  Label(label_application_file,text = curApplicationx.file, bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="blue",cursor="hand2")
        label_application_file2.bind("<Button-1>", lambda e:open(e))
        buttton_browse_file = Button(label_application_file, text="Αναζήτηση", command=lambda:browse_files(), bg="red3",font=("Times New Roman (Times)", 14, "bold"))
    
        def open(event):
            os.startfile(curApplicationx.file)

        label_application_comments = Label(label_department_application_mid, bg="floral white")
        label_application_comments1 = Label(label_application_comments, text="Αιτιολόγηση: ",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        info_comments = Text(label_application_comments, bg="WHITE", height=15, width=50, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
        info_comments.insert('1.0', curApplicationx.reasoning)



        button_accept = Button(label_department_application_bottom, text="Αποδοχή", command=lambda: accept_cap(info_number,info_comments), bg="green",font=("Calibri", 14, "bold"),height=1 ,width=12)
        btn_rtn = Button(label_department_application_bottom, text="Επιστροφή", command=lambda: raiseNdrop_frame(capacity_submit_Frame,previous_frame), bg="red3",font=("Calibri", 14, "bold"),height=1 ,width=12)
        
        label_department_application_all.pack(side=TOP,fill=BOTH, expand=1)
        label_department_application_a_top.pack(side=TOP)
        label_department_application_top.pack(side=TOP)
        label_department_application_mid.pack(side=TOP, fill=BOTH, expand=1)
        label_department_application_bottom.pack(side=TOP,fill=X, expand=0, padx=100)

        label_application_number.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
        label_application_number1.pack(side=LEFT,padx=10)
        info_number.pack(side=LEFT,padx=10)

        label_application_file.pack(side=TOP,pady=2,expand=1,fill=X, padx=30)
        label_application_file1.pack(side=LEFT,padx=10)
        label_application_file2.pack(side=LEFT,padx=10)
        buttton_browse_file.pack(side=LEFT,padx=10)

        label_application_comments.pack(side=LEFT,pady=2,expand=1)
        label_application_comments1.pack(side=TOP)
        info_comments.pack(side=LEFT)

        button_accept.pack(side=RIGHT)
        btn_rtn.pack(side=RIGHT)
    
    seatMk() 
    
    def browse_files():  #filedialog documentation  για λεπτομερειες 
    # Allow user to select a file and store it in global variable folder_path_form  και ασφάλεια από λάθος αρχείο
        global folder_path_file
        global department_application_Frame
        filename_form = filedialog.askopenfilename()
        file_type2=filename_form.split(".")
        if(file_type2[-1]=="pdf" ): #αν το τελευταιο στοιχειο της λιστας είναι το string pdf
            folder_path_file.set(filename_form)
            msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να υποβάλετε αυτό το αρχείο;',icon='warning')
            if msg_confirmation == 'yes':
                curApplicationx.file = filename_form
                messagebox.showinfo('Oλοκλήρωση', 'Επιτυχής υποβολή αρχείου!') 
                department_application_Frame.destroy()
                department_application_Frame=Frame(all_Frame, bg="floral white") 
                seatMk()
                raiseNdrop_frame(department_application_Frame,previous_frame)
            else:
                browse_files()

        else:
            msg_error_form = messagebox.showerror('Πρόβλημα Αρχείου!', 'Παρακαλώ επιλέξτε ένα αρχείο τύπου pdf που να περιέχει τα στοιχεία της δήλωσης σας', icon='warning')
            filename_ID=""   
    #####συναρτηση ελεγχου αριθμου#######################################

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    
    
    ##################SINARTISI##############
   


    def accept_cap(info_number,info_comments):
        global department_application_Frame
        global capacity_submit_Frame
        msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να αποδεχτείτε αυτή τη δήλωση;',icon='warning')
        if msg_confirmation== 'yes':
            std_number = info_number.get('1.0', 'end-1c')
            is_number(std_number)
            if is_number(std_number) == False:
                messagebox.showinfo('Αποτυχία', 'Παρακαλώ εισχωρήστε αριθμό θέσεων!')

            else:
                messagebox.showinfo('Oλοκλήρωση', 'Η δήλωση έγινε δεκτή με επιτυχία!')
                curApplicationx.rseats = info_number.get('1.0', 'end-1c')
                curApplicationx.reasoning = info_comments.get('1.0', 'end-1c')
                department_application_Frame.destroy()
                department_application_Frame=Frame(all_Frame, bg="floral white") 
                seatMk()
                capacity_submit_Frame.destroy()
                capacity_submit_Frame=Frame(all_Frame, bg="floral white")
                capMk()
                raiseNdrop_frame(capacity_submit_Frame,previous_frame)
                
        else:
            messagebox.showinfo('Αποτυχία', 'Αποτυχία καταχώρησης δήλωσης!')
            

    # -------------------------------ΝΕΑ ΑΙΤΗΣΗ END, Start of ΣΕΛΙΔΑ ΤΜΗΜΑΤΟΣ---------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    def siteMk():
        global page_Frame
        page_all=Label(page_Frame,bg="floral white")

        page_all_top = Label(page_all, bg="floral white")
        page_at_top = Label(page_all_top, text="Επισκόπηση:",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        page_all_mid =  Label(page_all, bg="floral white")
        page_at_mid = Label(page_all_mid,bg = "floral white")
        page_am_bot = Label(page_at_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")
        page_all_bottom =  Label(page_all, bg="floral white")

        page_cover = Label(page_all_mid,image=render4, borderwidth=0, highlightthickness=0, bg="floral white")
        
        page_label1 = Label(page_am_bot, bg="floral white")
        page_depart_logo= Label(page_label1,image=render3, borderwidth=0, highlightthickness=0, bg="floral white")
        page_depart_title = Label(page_label1, text=curDepartment.name,  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
        
        page_label2 = Label(page_am_bot, bg="floral white")
        page_depart_city = Label(page_label2, text="Έδρα:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
        page_depart_city1 = Label(page_label2, text=curDepartment.university+","+curDepartment.city,  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="black")
        
        page_label3 = Label(page_am_bot, bg="floral white")
        page_depart_orientaion = Label(page_label3, text="Προσανατολισμοί:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
        texOr = ""
        for i in range(len(curDepartment.orientations)):
            texOr += curDepartment.orientations[i].name + " "
        page_depart_orientation1 = Label(page_label3, text=texOr, bg="floral white", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
        
        page_label4 = Label(page_am_bot, bg="floral white")
        page_depart_vasi = Label(page_label4, text="Βάσεις 2019:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
        page_depart_vasi1 = Label(page_label4, text=curDepartment.base,  bg="floral white", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))

        page_label5 = Label(page_am_bot, bg="floral white")
        page_depart_site = Label(page_label5, text="Ιστοσελίδα:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
        page_depart_site1 = Label(page_label5, text=curDepartment.site.link,  bg="floral white", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))

        page_label6 = Label(page_am_bot, bg="floral white")
        page_depart_descr = Label(page_label6, text="Περιγραφή:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
        page_depart_descr1 = Text(page_label6, bg="floral white", height=6, width=60, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 14))
        page_depart_descr1.insert('1.0', curDepartment.site.description)
        page_depart_descr1.config(state=DISABLED)
        page_label7 = Label(page_all, bg="floral white")
        btn_page_edit = Button(page_label7, text="Επεξεργασία", command=lambda: raiseNdrop_frame(page_edit_Frame,previous_frame), bg="gray",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)

        page_all.pack(side = TOP, fill=BOTH, expand=1)
        page_all_top.pack(side = TOP, fill=X)
        page_at_top.pack(side = TOP)
        page_all_mid.pack(side = TOP, fill=BOTH, expand=1)
        page_cover.pack(side = TOP)
        page_at_mid.pack(side = LEFT, fill=BOTH, expand=1)
        page_all_bottom.pack(side = TOP)
        page_am_bot.pack(side = LEFT,fill = X)

        

        page_label1.pack(side=TOP,fill = X)
        page_depart_logo.pack(side = LEFT)
        page_depart_title.pack(side = LEFT)

        page_label2.pack(side=TOP,fill = X)
        page_depart_city.pack(side = LEFT)
        page_depart_city1.pack(side = LEFT)
        
        page_label3.pack(side=TOP,fill = X)
        page_depart_orientaion.pack(side = LEFT)
        page_depart_orientation1.pack(side = LEFT)
        
        page_label4.pack(side=TOP,fill = X)
        page_depart_vasi.pack(side = LEFT)
        page_depart_vasi1.pack(side = LEFT) 

        page_label5.pack(side=TOP,fill = X)
        page_depart_site.pack(side = LEFT,)
        page_depart_site1.pack(side = LEFT)

        page_label6.pack(side=TOP,fill = X)
        page_depart_descr.pack(side = LEFT)
        page_depart_descr1.pack(side = LEFT)

        page_label7.pack(side=RIGHT)
        btn_page_edit.pack(side=RIGHT)
    siteMk()

    # -------------------------------ΣΕΛΙΔΑ ΤΜΗΜΑΤΟΣ END, Start of ΕΠΕΞΕΡΓΑΣΙΑ ΣΕΛΙΔΑΣ------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    page_edit_all=Label(page_edit_Frame,bg="floral white")

    page_edit_all_top = Label(page_edit_all, bg="floral white")
    page_edit_at_top = Label(page_edit_all_top, text="Επεξεργασία Σελίδας:",  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    page_edit_all_mid =  Label(page_edit_all, bg="floral white")
    page_edit_am_bot = Label(page_edit_all_mid,bg="floral white", borderwidth=2, highlightthickness=2, relief="groove")

    page_edit_cover = Label(page_edit_am_bot,image=render4, borderwidth=0, highlightthickness=0, bg="floral white")
    
    page_edit_label1 = Label(page_edit_am_bot, bg="floral white")
    page_edit_depart_logo= Label(page_edit_label1,image=render3, borderwidth=0, highlightthickness=0, bg="floral white")
    page_edit_depart_title = Label(page_edit_label1, text=curDepartment.name,  bg="floral white",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    
    page_edit_label5 = Label(page_edit_am_bot, bg="floral white")
    page_edit_depart_site = Label(page_edit_label5, text="Ιστοσελίδα:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
    page_edit_depart_site1 = Text(page_edit_label5, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    page_edit_depart_site1.insert('1.0', curDepartment.site.link)
    page_edit_label6 = Label(page_edit_am_bot, bg="floral white")
    page_edit_depart_descr = Label(page_edit_label6, text="Περιγραφή:",  bg="floral white",font=("Times New Roman (Times)", 16, "bold"),fg="gray")
    page_edit_depart_descr1 = Text(page_edit_label6, bg="WHITE", height=8, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    page_edit_depart_descr1.insert('1.0', curDepartment.site.description)
    page_edit_label7 = Label(page_edit_am_bot, bg="floral white")
    btn_page_acccept = Button(page_edit_label7, text="Αποδοχή", command=lambda: accept_edit(), bg="green3",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)
    btn_page_rtn = Button(page_edit_label7, text="Επιστροφή", command=lambda: return_edit(), bg="gray",font=("Calibri", 14, "bold"),height=1 ,width=12)

    
    def accept_edit():
        global page_Frame
        msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να αποδεχτείτε αυτή την εμφάνιση της σελίδας;',icon='warning')
        if msg_confirmation == 'yes':
            messagebox.showinfo('Oλοκλήρωση', 'Η εμφάνιση έγινε δεκτή με επιτυχία!')
            
            curDepartment.siteedit(page_edit_depart_site1.get('1.0', 'end-1c'),page_edit_depart_descr1.get('1.0', 'end-1c'))

            page_Frame.destroy()
            page_Frame=Frame(all_Frame, bg="floral white")
            siteMk()
            raiseNdrop_frame(page_Frame,previous_frame)
        else:
            raiseNdrop_frame(page_edit_Frame,previous_frame)

    
    def return_edit():
        msg_confirmation = messagebox.askquestion('Επιβεβαίωση!', 'Είστε σίγουροι ότι θέλετε να φύγετε από την επεξεργασία; Οι αλλαγές δε θα αποθηκευτόυν.',icon='warning')
        if msg_confirmation == 'yes':
            raiseNdrop_frame(page_Frame,previous_frame) 
        else:
            raiseNdrop_frame(page_edit_Frame,previous_frame)



    page_edit_all.pack(side=TOP,expand=1,fill=BOTH)

    page_edit_all.pack(side = TOP, fill=BOTH, expand=1)
    page_edit_all_top.pack(side = TOP, fill=X)
    page_edit_at_top.pack(side = TOP)
    page_edit_all_mid.pack(side = TOP, fill=BOTH)
    page_edit_am_bot.pack(side = LEFT)

    page_edit_cover.pack(side = TOP)

    page_edit_label1.pack(side=TOP)
    page_edit_depart_logo.pack(side = LEFT, padx=10)
    page_edit_depart_title.pack(side = LEFT, padx=10)

    page_edit_label5.pack(side=TOP)
    page_edit_depart_site.pack(side = TOP, padx=10)
    page_edit_depart_site1.pack(side = TOP, padx=10)

    page_edit_label6.pack(side=TOP)
    page_edit_depart_descr.pack(side = TOP, padx=10)
    page_edit_depart_descr1.pack(side = TOP, padx=10)

    page_edit_label7.pack(side=RIGHT)
    btn_page_acccept.pack(side=RIGHT)
    btn_page_rtn.pack(side=RIGHT)
    

##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()

main()

