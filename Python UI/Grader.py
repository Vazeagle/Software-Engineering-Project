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


#Frames For Main Window
frame_temp=Frame()#Frame to get as temp to successfull change between frames
grader_Frame=Frame(main_window, bg="white")
grader_menu_Frame=Frame(grader_Frame, bg="gray26")
grader_intro_Frame = Frame(grader_Frame, bg="floral white")
grader_graderInfo_Frame = Frame(grader_Frame, bg="floral white") 
grader_pexams_Frame = Frame(grader_Frame, bg="floral white") #Πανελλήνιες
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

def main():

    grader_menu = Label(grader_menu_Frame, bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
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
    ministry_news_list.configure(yscrollcommand=scrollv.set, xscrollcommand=scrollh.set, font=("Calibri", 36))
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
    btn_next1 = Button(gmenu_l_down, text="Πρόγραμματα", command=lambda: raiseNdrop_frame(grader_graderInfo_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    btn_next2 = Button(gmenu_l_down, text="Εγγραφές", command=lambda: raiseNdrop_frame(grader_pexams_Frame,previous_frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold")) 
    btn_next3 = Button(gmenu_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    

    #packs εμφάνιση στοιχείων
    grader_menu.pack(side=LEFT,expand=1,fill=Y)
    gmenu_l_up.pack(side=TOP,pady=50)#PARMENIDIS LOGO
    gmenu_l_down.pack(side=TOP)#CONTAINS BUTTONS
    initialGrader_all.pack(side=TOP,fill=BOTH,expand=1)#δεξιο μενου-αρχικη σελίδα
    initialGrader_all_top.pack(side=TOP,fill=X,pady=50)
    initialGrader_all_bot.pack(side=LEFT, expand=1, fill=BOTH)
    initialGrader_ab_top.pack(side=TOP, expand=1, fill=BOTH, ipady=100)
    #αριστερη πλευρα με ονομα σχολειου-χρηστη
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

    #add elements to announcements
    ministry_news_list.insert(1, "This is a test to see if the announcements works as it should be")
    ministry_news_list.insert(2, "Ανακοινωση Ημερομηνίας Δηλώσεων")
    ministry_news_list.insert(3, "Πρόγραμμα εξεταστικής έτους 2020-2021")
    ministry_news_list.insert(4, "#ΜΕΝΟΥΜΕ_ΣΠΙΤΙ")
    ministry_news_list.insert(5, "Έναρξη δηλώσεων μαθητών")
    ministry_news_list.insert(6, "ΠΑΡΜΕΝΙΔΗΣ ΜΕ TKINTER ΓΙΑ GUI")
    ministry_news_list.insert(7, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")

    #ΑΡΧΙΚΑ FRAMES ΕΜΦΑΝΙΣΗ
    raiseNdrop_frame(grader_Frame,none)
    raiseNdrop_frame(grader_menu_Frame,none)
    raiseNdrop_frame(grader_intro_Frame,none)  

    main_window.mainloop()  # ------------------------------Put always to end of frames

main()