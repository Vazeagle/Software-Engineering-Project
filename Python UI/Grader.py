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
import yagmail




#Initialisation
getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])
main_window = Tk()
main_window.geometry(resolution) ###########################################resolution
main_window.title("Parmenidis")
main_window.configure()
main_window.state("zoomed")
main_window.attributes('-fullscreen', True)
none="none" #για μεταβαση σε frames
previous_frame="previous_frame"
frame_counter=0
init_pass=0
temp_image= None

#Frames For Main Window
frame_temp=Frame()#Frame to get as temp to successfull change between frames
grader_Frame=Frame(main_window, bg="white")
grader_menu_Frame=Frame(grader_Frame, bg="gray26")
grader_intro_Frame = Frame(grader_Frame, bg="floral white")
graderInfo_Frame = Frame(grader_Frame, bg="floral white") 
pexams_Frame = Frame(grader_Frame, bg="floral white") #Πανελλήνιες
grader_grading_Frame=Frame(grader_Frame, bg="floral white") #εκχώρηση βαθμολογιών  
grader_problems_Frame = Frame(grader_Frame, bg="floral white") #προβλήματα με την εφαρμογή

def ExitApp():
    MsgBox = messagebox.askquestion('Έξοδος Εφαρμογής!', 'Είστε σίγουροι ότι θέλετε να αποσυνδεθείτε από το σύστημα Παρμενίδης ;', icon='warning')
    if MsgBox == 'yes':
        main_window.destroy()
    else:
        messagebox.showinfo('Επιστροφή', 'Θα επιστραφείτε στην προηγούμενη σας οθόνη !')

def raiseNdrop_frame(frameUp,frameDown):
    global frame_counter
    global init_pass #flag to see if menu frame has appeared (0 is  no, 1 is yes)
    global frame_temp #απλα οριζω οτι το frame temp ειναι τυπου frame γιατι αλλιως προβλημα στο forget γτ το διαβάζει ως string
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
    

    if(frameUp==grader_menu_Frame):
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

load3 = Image.open('profil.jpg')
load3 = load3.resize((100, 100), Image.ANTIALIAS)
render3 = ImageTk.PhotoImage(load3)

def main():

    grader_menu = Label(grader_menu_Frame, bg="gray26",font=("Times New Roman (Times)", 24, "bold"))  # aristero menu
    gmenu_l_up = Label(grader_menu, image=render2, borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    gmenu_l_down = Label(grader_menu, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    initialGrader_all = Label(grader_intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexia arxikh selida
    initialGrader_all_top = Label(initialGrader_all, text='Καλώς ορίσατε στον Παρμενίδη!',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 36, "bold"))
    initialGrader_all_bot = Label(initialGrader_all, borderwidth=1, highlightthickness=0, bg="floral white")
    initialGrader_ab_top = Label(initialGrader_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include user name and calendar
    initialGrader_abt_left = Label(initialGrader_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#user grader name left side
    initialGrader_abtl_top = Label(initialGrader_abt_left, borderwidth=1, highlightthickness=0, bg="floral white")#user grader name top left previous side
    initialGrader_abtlt_left = Label(initialGrader_abtl_top, borderwidth=1, highlightthickness=0, bg="floral white")#user grader name top of left side
    initialGrader_abtltl_left = Label(initialGrader_abtlt_left, text='Είστε συνδεδεμένοι ως: ',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    initialGrader_abtltl_right = Label(initialGrader_abtlt_left, text='Σβίγγου Αναστασία',borderwidth=1, highlightthickness=0, bg="cyan2",font=("Times New Roman (Times)", 18, "bold"))
    initialGrader_abt_right = Label(initialGrader_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#calenar and text include
    initialGrader_abtr_top = Label(initialGrader_abt_right, text='Ημερολόγιο', borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#calendar text
    initialGrader_abtr_bot = Label(initialGrader_abt_right, borderwidth=1, highlightthickness=0, bg="floral white")#calendar
    initialGrader_ab_bot = Label(initialGrader_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include announcements
    initialGrader_abb_top = Label(initialGrader_ab_bot, borderwidth=1, highlightthickness=0, bg="floral white")
    initialGrader_abbt_left = Label(initialGrader_abb_top, text='Ανακοινώσεις',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#announcement title
    initialGrader_abb_bot = Frame(initialGrader_ab_bot, bg="cyan2")#announcement box

    #orismos listbox anakoinwsewn
    ministry_news_list  = Listbox (initialGrader_abb_bot, bg="floral white", borderwidth=2, highlightthickness=0)#width=getRes[0]-50, height=getRes[1]-70
    
    scrollh = Scrollbar(initialGrader_abb_bot, orient="horizontal", command=ministry_news_list.xview)
    scrollv= Scrollbar(initialGrader_abb_bot, orient="vertical", command=ministry_news_list.yview)
    initialGrader_abb_bot.bind("<Configure>",lambda e: ministry_news_list.configure(scrollregion=ministry_news_list.bbox("all")))
    ministry_news_list.configure(yscrollcommand=scrollv.set, xscrollcommand=scrollh.set, font=("Times New Roman (Times)", 36))
    initialGrader_abb_bot.bind("<MouseWheel>", scrollv)#ΚΑΘΕΤΟ SCROLL ΜΕ ΡΟΔΑ ΠΟΝΤΙΚΙΟΥ
    
    #ορισμος ημερολογιου
    cal_intro = Calendar(initialGrader_abtr_bot, selectmode='none')
    date = cal_intro.datetime.today() + cal_intro.timedelta(days=2)
    cal_intro.calevent_create(date, 'Hello World', 'message')
    cal_intro.calevent_create(date, 'Reminder 2', 'reminder')
    cal_intro.calevent_create(date + cal_intro.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal_intro.calevent_create(date + cal_intro.timedelta(days=3), 'Message', 'message')
    cal_intro.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')




    #orismos buttons
    btn_next0 = Button(gmenu_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(grader_intro_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_next1 = Button(gmenu_l_down, text="Στοιχεία Χρήστη", command=lambda: raiseNdrop_frame(graderInfo_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_next2 = Button(gmenu_l_down, text="Πανελλήνιες", command=lambda: raiseNdrop_frame(pexams_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold")) 
    btn_next3 = Button(gmenu_l_down, text="Προβλήματα", command=lambda: raiseNdrop_frame(pexams_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold")) 
    btn_next4 = Button(gmenu_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    

    #packs εμφάνιση στοιχείων
    grader_menu.pack(side=LEFT,expand=1,fill=Y)
    gmenu_l_up.pack(side=TOP,pady=50)#PARMENIDIS LOGO
    gmenu_l_down.pack(side=TOP)#CONTAINS BUTTONS
    initialGrader_all.pack(side=TOP,fill=BOTH,expand=1)#δεξιο μενου-αρχικη σελίδα
    initialGrader_all_top.pack(side=TOP,fill=X,pady=50)
    initialGrader_all_bot.pack(side=LEFT, expand=1, fill=BOTH)
    initialGrader_ab_top.pack(side=TOP, expand=1, fill=BOTH, ipady=100)
    #αριστερη πλευρα με ονομα βαθμολογητή
    initialGrader_abt_left.pack(side=LEFT, fill=Y, padx=50)
    initialGrader_abtl_top.pack(side=TOP, fill=X)
    initialGrader_abtlt_left.pack(side=LEFT)
    initialGrader_abtltl_left.pack(side=TOP, pady=20)
    initialGrader_abtltl_right.pack(side=TOP)
    #δεξια πλευρα με ημερολογιο
    initialGrader_abt_right.pack(side=RIGHT, expand=1, fill=BOTH, padx=40)
    initialGrader_abtr_top.pack(side=TOP, fill=X) 
    initialGrader_abtr_bot.pack(side=TOP, fill=BOTH, expand=1)#hmerologio
    cal_intro.pack(fill=BOTH, expand=1)
    ttk.Label(initialGrader_abtr_bot, text="Hover over the events.").pack()
    #κατω πλευρα με ανακοινωσεις
    initialGrader_ab_bot.pack(side=TOP, expand=1, fill=BOTH)
    initialGrader_abb_top.pack(side=TOP, fill=X)
    initialGrader_abbt_left.pack(side=LEFT)
    initialGrader_abb_bot.pack(side=TOP, expand=1, fill=BOTH)
    scrollv.pack(side=RIGHT, fill=Y)
    scrollh.pack(side=BOTTOM, fill=X)
    ministry_news_list.pack(side=BOTTOM, expand=1, fill=BOTH)
    initialGrader_abb_bot.pack(side=BOTTOM, expand=1, fill=BOTH)

    #buttons MENU
    btn_next0.pack(side=TOP,pady=2,ipady=5)
    btn_next1.pack(side=TOP,pady=2,ipady=5)
    btn_next2.pack(side=TOP,pady=2,ipady=5)
    btn_next3.pack(side=TOP,pady=2,ipady=5)
    btn_next4.pack(side=TOP,pady=2,ipady=5)    

    #add elements to announcements
    ministry_news_list.insert(1, "This is a test to see if the announcements works as it should be")
    ministry_news_list.insert(2, "Ανακοινωση Ημερομηνίας Δηλώσεων")
    ministry_news_list.insert(3, "Πρόγραμμα εξεταστικής έτους 2020-2021")
    ministry_news_list.insert(4, "#ΜΕΝΟΥΜΕ_ΣΠΙΤΙ")
    ministry_news_list.insert(5, "Έναρξη δηλώσεων μαθητών")
    ministry_news_list.insert(6, "ΠΑΡΜΕΝΙΔΗΣ ΜΕ TKINTER ΓΙΑ GUI")
    ministry_news_list.insert(7, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")




    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #graderInfo_Frame

    graderinfo_all = Label(graderInfo_Frame, bg="floral white")
    graderinfo_a_top = Label(graderinfo_all, bg="floral white", text="Πληροφορίες Χρήστη",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    graderinfo_a_mid = Label(graderinfo_all, bg="floral white")#info
    graderinfo_a_bot = Label(graderinfo_a_mid, bg="floral white")# buttons

    graderinfo_am_general = Label(graderinfo_a_mid, bg="floral white")
    graderinfo_am_gen_title = Label(graderinfo_am_general, bg="SkyBlue1", text="Γενικά:",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_am_gen_info = Label(graderinfo_am_general, bg="floral white")# containt text and photo

    graderinfo_am_gen_info_left = Label(graderinfo_am_gen_info, bg="floral white")#text info container
    #id
    graderinfo_id = Label(graderinfo_am_gen_info_left, bg="floral white")
    graderinfo_id_left = Label(graderinfo_id, bg="floral white", text="ID Χρήστη:\t",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_id_right = Text(graderinfo_id, bg="WHITE", height=1, width=30, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    graderinfo_id_right.config(state=DISABLED)
    
    #password
    graderinfo_password = Label(graderinfo_am_gen_info_left, bg="floral white")
    graderinfo_pass_left = Label(graderinfo_password, bg="floral white", text="Κωδικός:\t",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_pass_right = Text(graderinfo_password, bg="WHITE", height=1, width=30, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    graderinfo_pass_right.config(state=DISABLED)

    #fullname
    graderinfo_fullname = Label(graderinfo_am_gen_info_left, bg="floral white")
    graderinfo_fullname_left = Label(graderinfo_fullname, bg="floral white", text="Ονοματεπώνυμο:\t",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_fullname_right = Text(graderinfo_fullname, bg="WHITE", height=1, width=30, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    graderinfo_fullname_right.config(state=DISABLED)
    
    #school
    graderinfo_school = Label(graderinfo_am_gen_info_left, bg="floral white")
    graderinfo_school_left = Label(graderinfo_school, bg="floral white", text="Σχολείο:\t\t",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_school_right = Text(graderinfo_school, bg="WHITE", height=1, width=30, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    graderinfo_school_right.config(state=DISABLED)
    
    #photo
    graderinfo_am_gen_info_right = Label(graderinfo_am_gen_info, bg="floral white")#photo info container
    graderinfo_photo_top = Label(graderinfo_am_gen_info_right, bg="floral white", text="Εικόνα Προφιλ:",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_photo_mid = Label(graderinfo_am_gen_info_right, bg="floral white",image=render3)
    graderinfo_photo_bot = Label(graderinfo_am_gen_info_right, bg="floral white")#button change invisible

    #contact information
    graderinfo_am_contact_info = Label(graderinfo_a_mid, bg="floral white")
    graderinfo_contact = Label(graderinfo_am_contact_info, bg="SkyBlue1", text="Επικοινωνία:",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_contact_all = Label(graderinfo_am_contact_info, bg="floral white")#contain email and number
    
    #email
    graderinfo_contact_email = Label(graderinfo_contact_all, bg="floral white")#email container
    graderinfo_contact_email_left = Label(graderinfo_contact_email, bg="floral white", text="E-mail:\t\t",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_contact_email_right = Text(graderinfo_contact_email, bg="WHITE", height=1, width=30, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    graderinfo_contact_email_right.config(state=DISABLED)
   
    #number
    graderinfo_contact_number = Label(graderinfo_contact_all, bg="floral white")#contain number
    graderinfo_contact_number_left = Label(graderinfo_contact_number, bg="floral white", text="Αριθμός Τηλεφώνου:",font=("Times New Roman (Times)", 18, "bold"),fg="black")
    graderinfo_contact_number_right = Text(graderinfo_contact_number, bg="WHITE", height=1, width=30, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    graderinfo_contact_number_right.config(state=DISABLED)

    btn_grader_info_edit = Button(graderinfo_a_bot, text="Επεξεργασία", command=lambda: edit_profile(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)
    btn_grader_save = Button(graderinfo_a_bot, state=DISABLED,text="Αποθήκευση", command=lambda: save_profile(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)
    btn_grader_pic_edit = Button(graderinfo_photo_bot, state=DISABLED, text="Αλλαγή Εικόνας", command=lambda: edit_pic(), bg="floral white",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)
    
    #χρειαζόμαστε συνάρτηση για τα αρχικά Data sos
    def edit_pic():
        global temp_image
        path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
        im = Image.open(path)
        im = im.resize((100, 100), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(im)
        graderinfo_photo_mid.configure(image=render3)
        graderinfo_photo_mid.image=render3
        temp_image = render3

    def edit_profile():
        #kane editable ta Text 
        graderinfo_id_right.config(state=DISABLED)
        graderinfo_pass_right.config(state=NORMAL)
        graderinfo_fullname_right.config(state=DISABLED)
        graderinfo_school_right.config(state=DISABLED)
        graderinfo_contact_email_right.config(state=NORMAL)
        graderinfo_contact_number_right.config(state=NORMAL)
        btn_grader_pic_edit.config(state=NORMAL)
        btn_grader_save.config(state=NORMAL)
        
        #Emfanise duo koympia stis 8eseis pou prepei cancel kai save
        #pop-ups gia la8oi xrhsth
        #old password confirmation
        #password_btn)change
        
        print("edit")

        
    def save_profile():
        
        global temp_image #Αποθηκευση Φωτογραφίας στη ΒΔ
        passw = graderinfo_pass_right.get("1.0",'end-1c')
        email = graderinfo_contact_email_right.get("1.0",'end-1c')
        phone = graderinfo_contact_number_right.get("1.0",'end-1c')

        btn_grader_save.config(state=DISABLED)
        btn_grader_pic_edit.config(state=DISABLED)
        graderinfo_pass_right.config(state=DISABLED)
        graderinfo_contact_email_right.config(state=DISABLED)
        graderinfo_contact_number_right.config(state=DISABLED)

        print("save")

    #pack reveal
    #general labels
    graderinfo_all.pack(side=TOP, expand=1, fill=BOTH)
    graderinfo_a_top.pack(side=TOP)
    graderinfo_a_mid.pack(side=LEFT, expand=1, fill=BOTH, pady=50)
    graderinfo_a_bot.pack(side=BOTTOM, fill=X)
    
    #grader
    graderinfo_am_general.pack(side=TOP, expand=1, fill=BOTH)
    graderinfo_am_gen_title.pack(side=TOP, fill=X)
    graderinfo_am_gen_info.pack(side=TOP, fill=X)
    graderinfo_am_gen_info_left.pack(side=LEFT)
   
    #id
    graderinfo_id.pack(side=TOP, fill=X)
    graderinfo_id_left.pack(side=LEFT)
    graderinfo_id_right.pack(side=LEFT)
    
   
    #password
    graderinfo_password.pack(side=TOP, fill=X)
    graderinfo_pass_left.pack(side=LEFT)
    graderinfo_pass_right.pack(side=LEFT)
   
    #fullname
    graderinfo_fullname.pack(side=TOP, fill=X)
    graderinfo_fullname_left.pack(side=LEFT)
    graderinfo_fullname_right.pack(side=LEFT)
    
    #school
    graderinfo_school.pack(side=TOP, fill=X)
    graderinfo_school_left.pack(side=LEFT)
    graderinfo_school_right.pack(side=LEFT)
    
    #photo
    graderinfo_am_gen_info_right.pack(side=RIGHT,ipadx=100, fill=Y)
    graderinfo_photo_top.pack(side=TOP)
    graderinfo_photo_mid.pack(side=TOP)
    graderinfo_photo_bot.pack(side=TOP)
   
    #contact information
    graderinfo_am_contact_info.pack(side=TOP, expand=0, fill=X)
    graderinfo_contact.pack(side=TOP, fill=X)
    graderinfo_contact_all.pack(side=LEFT, expand=1, fill=BOTH)
    #email
    graderinfo_contact_email.pack(side=TOP, fill=X)
    graderinfo_contact_email_left.pack(side=LEFT)
    graderinfo_contact_email_right.pack(side=LEFT)
    #number
    graderinfo_contact_number.pack(side=TOP, fill=X)
    graderinfo_contact_number_left.pack(side=LEFT)
    graderinfo_contact_number_right.pack(side=LEFT)
    #button edit
    btn_grader_info_edit.pack(side=RIGHT, padx=50)
    btn_grader_save.pack(side=RIGHT)
    btn_grader_pic_edit.pack()

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #pexams_Frame

    pexams_all = Label(pexams_Frame, borderwidth=0, highlightthickness=0, bg="floral white")  # dexia arxikh selida
    pexams_all_top = Label(pexams_all, text='Εκχώρηση Βαθμολογίας',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 36, "bold"))
    pexams_all_bot = Label(pexams_all, borderwidth=1, highlightthickness=0, bg="floral white")
    pexams_ab_top = Label(pexams_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include user name

    #ONOMA LISTAS
    std_reg_create_abt_top = Label(pexams_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#LIST  name
    #ΣΤΟΙΧΕΙΑ ΜΑΘΗΤΗ
    pexams_abt_top1 = Label(pexams_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student  name 
    pexams_abt_top2 = Label(pexams_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student  lastname 
    pexams_abt_top3 = Label(pexams_ab_top, borderwidth=1, highlightthickness=0, bg="floral white")#student email 

    std_reg_create_abtltl_l1 = Label(pexams_abt_top1, text='Κωδικός Υποψηφίου:',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l2 = Label(pexams_abt_top2, text='Μάθημα:',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    std_reg_create_abtltl_l3 = Label(pexams_abt_top3, text='Βαθμός:', borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))
    
    
    #TEXTS AS INPUTS!!!!!!!!!!!
    std_reg_create_abtltl_r1 = Text(pexams_abt_top1, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r2 = Label(pexams_abt_top2, bg="WHITE", fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))
    std_reg_create_abtltl_r3 = Text(pexams_abt_top3, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Calibri", 16))

    #DROP DOWN MENU ΓΙΑ ΕΠΙΛΟΓΗ SELECT ΑΠΟ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ
    lesson_choice=["Μαθηματικά", "Φυσική", "Χημεία"]
    lesson_var = StringVar(std_reg_create_abtltl_r2)
    lesson_var.set(lesson_choice[0])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    lesson_choice = OptionMenu(std_reg_create_abtltl_r2, lesson_var, *lesson_choice)
    lesson_choice.config(bg="snow", width=20)
    

   
    std_reg_create_ab_mid = Label(pexams_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#include announcements
    std_reg_create_abm_top = Label(std_reg_create_ab_mid, borderwidth=1, highlightthickness=0, bg="floral white")
    std_reg_create_abmt_left = Label(std_reg_create_abm_top, text='Λίστα Βαθμαλογιών: ',borderwidth=1, highlightthickness=0, bg="floral white",font=("Times New Roman (Times)", 18, "bold"))#announcement title
    std_reg_create_abm_bot = Label(std_reg_create_ab_mid, bg="floral white")#announcement box

    std_reg_create_ab_bot = Label(pexams_all_bot, borderwidth=1, highlightthickness=0, bg="floral white")#ΚΑΤΩ ΠΛΕΥΡΑ ΜΕ ΚΟΥΜΠΙΑ NEXT KAI RETURN
    
    


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


    def delete_user():
        print("deleted user")

    def confirm_registry():

       print("registry confirmed")

    #ORISMOS BTNS
    btn_reg_create_return = Button(std_reg_create_ab_bot, text="Επιστροφή", command=lambda: raiseNdrop_frame(school_std_reg_Frame,previous_frame), bg="red3",height = 1, width = 12,font=("Calibri", 16, "bold"))
    btn_reg_create_confirm = Button(std_reg_create_ab_bot, text="Επιβεβαίωση", state=DISABLED, command=lambda: confirm_registry(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_delete_list = Button(std_reg_create_ab_bot, text="Διαγραφή Λίστας", state=DISABLED, command=lambda: delete_list(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_add = Button(pexams_ab_top, text="Προσθήκη Εγγραφής", state=DISABLED, command=lambda: add_user(), bg="red3",font=("Calibri", 16, "bold"))
    btn_reg_delete = Button(pexams_ab_top, text="Διαγραφή Εγγραφής", state=DISABLED, command=lambda: delete_user(), bg="red3",font=("Calibri", 16, "bold"))

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
    pexams_all.pack(side=TOP,fill=BOTH,expand=1)#δεξιο μενου-αρχικη σελίδα
    pexams_all_top.pack(side=TOP,fill=X)

    pexams_all_bot.pack(side=TOP, expand=1, fill=BOTH,pady=30)
    pexams_ab_top.pack(side=TOP, fill=X, ipady=10)#expand=1
    
    #αριστερη πλευρα με  στοιχεια εγγραφης
    std_reg_create_abt_top.pack(side=TOP, fill=X)
    pexams_abt_top1.pack(side=TOP, fill=X)
    pexams_abt_top2.pack(side=TOP, fill=X)
    pexams_abt_top3.pack(side=TOP, fill=X)

    std_reg_create_abtltl_l1.pack(side=LEFT, padx=10)#ονομα
    std_reg_create_abtltl_l2.pack(side=LEFT, padx=10)#επωνυμο
    std_reg_create_abtltl_l3.pack(side=LEFT, padx=10)#e-mail
    


    std_reg_create_abtltl_r1.pack(side=LEFT)#ονομα
    std_reg_create_abtltl_r2.pack(side=LEFT)#επωνυμο
    std_reg_create_abtltl_r3.pack(side=LEFT)#e-mail
    lesson_choice.pack()
    
    #κατω πλευρα με Λίστα
    std_reg_create_ab_mid.pack(side=TOP, fill=BOTH,expand=1)#,ipady=100)#, expand=1, fill=X)#BOTH
    std_reg_create_abm_top.pack(side=TOP, fill=X)
    std_reg_create_abmt_left.pack(side=LEFT,padx=10)
    #std_reg_create_abm_bot.pack(side=TOP, expand=1, fill=BOTH)#BOTH
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
    btn_reg_delete_list.pack(side=LEFT, padx=50) 
    

    #ΑΡΧΙΚΑ FRAMES ΕΜΦΑΝΙΣΗ
    raiseNdrop_frame(grader_Frame,none)
    raiseNdrop_frame(grader_menu_Frame,none)
    raiseNdrop_frame(grader_intro_Frame,none)  

    main_window.mainloop()  # ------------------------------Put always to end of frames

main()