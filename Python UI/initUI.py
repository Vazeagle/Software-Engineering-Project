# CAUTION IN ORDER TO RUN YOU NEED TO DOWNLOAD THE FOLLOWING PACKAGES: MouseInfo, Pillow, PyAutoGUI, PyGetWindow, PyMsgBox, PyRect, PyScreeze, pyperclip.
# SEE THE PDF REPORT FOR MORE INSTRUCTIONS ON HOW TO USE THE PROGRAMM

######---------Packages Needed
import os, sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry

#Initialisation
getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])
main_window = Tk()
main_window.geometry(resolution) ###########################################resolution
main_window.title("Parmenidis")
main_window.configure()
none="none"

#Picture Insertion & Resize

####LOAD PICTURES

load0 = Image.open('backround.jpg')
load0 = load0.resize((getRes[0], getRes[1]), Image.ANTIALIAS)
render0 = ImageTk.PhotoImage(load0)
    
load1 = Image.open('P1.png')
load1 = load1.resize((140, 160), Image.ANTIALIAS)
render1 = ImageTk.PhotoImage(load1)
    
load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)

load3 = Image.open('profil.jpg')
load3 = load3.resize((100, 100), Image.ANTIALIAS)
render3 = ImageTk.PhotoImage(load3)

load4 = Image.open('gr.jpg')
load4 = load3.resize((100, 100), Image.ANTIALIAS)
render4 = ImageTk.PhotoImage(load4)

####END PICTURES


#Frames For Main Window

all_Frame=Frame(main_window, bg="white")
menu_Frame=Frame(all_Frame, bg="gray26")
intro_Frame = Frame(all_Frame, bg="blue")
statement_Frame=Frame(all_Frame,width=getRes[0], height=getRes[1], bg="salmon1")
weekly_program_Frame=Frame(all_Frame,width=getRes[0], height=getRes[0], bg="salmon1")
results_Frame=Frame(all_Frame, bg="salmon1",width=getRes[0], height=getRes[1])
institutions_Frame = Frame(all_Frame, bg="salmon1", width=getRes[0], height=getRes[1])
info_Frame = Frame(all_Frame, bg="salmon1", width=getRes[0], height=getRes[1])
announcements_Frame = Frame(all_Frame, bg="floral white", width=getRes[0]-1600, height=getRes[1])
problems_Frame = Frame(all_Frame, bg="salmon1", width=getRes[0], height=getRes[1])
#problems_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])


#Needed Functions

def raiseNdrop_frame(frameUp,frameDown):
    if(frameDown!="none"):
        #frameDown.pack_forget(frameDown)
        frameDown.destroy()
    if(frameUp==menu_Frame):
        frameUp.tkraise()
        frameUp.pack(side=LEFT, fill=Y)
    else:
        frameUp.tkraise()
        frameUp.pack(expand=1,fill=BOTH)   
    



def ExitApp():
    MsgBox = messagebox.askquestion('Έξοδος Εφαρμογής!', 'Είστε σίγουροι ότι θέλετε να αποσυνδεθείτε από το σύστημα Παρμενίδης ;',
                                       icon='warning')
    if MsgBox == 'yes':
        main_window.destroy()
    else:
        messagebox.showinfo('Επιστροφή', 'Θα επιστραφείτε στην προηγούμενη σας οθόνη !')

def main():
    

    # ---------------------------------------------------
    #container = ttk.Frame(main_window)
    #canvas = Canvas(container, bg="white", borderwidth=2, highlightthickness=0)#-50 -70
    #container = ttk.Frame(main_window)#, width=getRes[0]-100, height=getRes[1]-100)
    #canvas = Canvas(container, bg="white", borderwidth=2, highlightthickness=0)#-50 -70
    #scrollbarv = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    #scrollbarh = ttk.Scrollbar(container, orient="vertical", command=canvas.xview)
    #scrollable_frame = ttk.Frame(canvas)

    #scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    #canvas.configure(yscrollcommand=scrollbarv.set, xscrollcommand=scrollbarh.set)

    # ---------------------------------------------------
    #all_Frame=Frame(main_window, bg="white")
    #menu_Frame=Frame(all_Frame, bg="gray26")
    #intro_Frame = Frame(all_Frame, bg="white")#, width=getRes[0], height=getRes[1])



    #init_Label = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="SkyBlue1") MALLON DELETE

    label_left = Label(menu_Frame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, text="ΦΩΤΟΓΤΑΦΙΑ\n ΠΑΡΜΕΝΊΔΗΣ", borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    label_right = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")  # dexio menu
    label_r_up = Label(label_right, borderwidth=1, highlightthickness=0, bg="floral white")  # panw meros me perilipsh kai hmerologio
    label_ru_up = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="floral white")  # kalos orisate+ to eniaio susthma klp
    label_ruu_up = Label(label_ru_up, text="Καλώς ήρθατε στον Παρμενίδη!\n", borderwidth=0, highlightthickness=0,bg="floral white", font=("Calibri", 24, "bold"))
    label_ruu_down = Label(label_ru_up, text="Το ενιαίο σύστημα για τις Πανελλήνιες Εξετάσεις.\n", borderwidth=0,highlightthickness=0, bg="floral white", font=("Calibri", 18))

    # isws na 8elei up kai oxi left
    ####### kanoniko #####label_ru_left = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="salmon1")  # foto parmenidi+ desription parmenidi
    label_ru_left = Label(label_ru_up, borderwidth=1, highlightthickness=0,bg="floral white")  # foto parmenidi+ desription parmenidi
    label_rul_left = Label(label_ru_left, image=render1, borderwidth=1, highlightthickness=0,bg="floral white")  # foto parmenidi
    label_rul_right = Label(label_ru_left, borderwidth=1, highlightthickness=0,bg="floral white")  # Ο παρμενιδης ειναι bla bla

    ########## KANONIKA ####label_ru_right = Label(label_r_up, borderwidth=0, highlightthickness=1,bg="salmon1")  # hmerologio gramma + hmerologio
    label_ru_right = Label(label_ru_up, borderwidth=0, highlightthickness=1,bg="floral white")  # hmerologio gramma + hmerologio
    label_rur_up = Label(label_ru_right, text="Ημερολόγιο\n", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 18))  # hmerologio gramma
    label_rur_down = Label(label_ru_right, borderwidth=1, highlightthickness=0, bg="floral white")  # hmerologio

    label_r_down = Label(label_right, borderwidth=20, highlightthickness=0, relief="raised", bg="floral white")  # sunoptiko profil
    label_rd_up = Label(label_r_down, text=" Συνοπτικό προφίλ: ",relief="groove", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 18, "bold"))  # sunoptiko profil
    label_rd_down = Label(label_r_down, borderwidth=1, highlightthickness=0, bg="floral white")  # onoma xrhsth kai alla
    label_rdd_left = Label(label_rd_down,image=render3, borderwidth=0, highlightthickness=0, bg="floral white")  # eikona user
    label_rdd_right = Label(label_rd_down, borderwidth=1, highlightthickness=0,bg="floral white")  # onoma xrhsth status lukeio kai alla

    label_rddr_left = Label(label_rdd_right, borderwidth=1, highlightthickness=0,bg="floral white")  # onoma xrhsth kai status
    label_rddrl_up = Label(label_rddr_left, text="ΣΤΥΛΙΑΝΟΣ ΒΑΖΑΙΟΣ", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="floral white")  # katastash
    label_rddrld_left = Label(label_rddrl_down, text="Κατάσταση: ", borderwidth=1, highlightthickness=0, bg="floral white",font=("Calibri", 14))  # katastash text
    label_rddrld_right = Label(label_rddrl_down, text="Προς Εξέταση", borderwidth=1, highlightthickness=1, relief="groove",bg="green2",font=("Calibri", 14))  # input katastashs apo data base

    label_rddr_right = Label(label_rdd_right, borderwidth=1, highlightthickness=1,bg="floral white")  # lukeio kai kateu8unsh
    label_rddrr_up = Label(label_rddr_right, borderwidth=1, highlightthickness=1, bg="floral white")  # lukeio genika
    label_rddrru_left = Label(label_rddrr_up, text=" Λύκειο: ", borderwidth=1, highlightthickness=1, bg="floral white", font=("Calibri", 14))  # lukeio gramma
    label_rddrru_right = Label(label_rddrr_up,text="1ο Λύκειο Καισαριανής", borderwidth=1, highlightthickness=0,bg="floral white", font=("Calibri", 14)) # lukeio input from db
    label_rddrr_down = Label(label_rddr_right, borderwidth=1, highlightthickness=1, bg="floral white")  # katey8unsh
    label_rddrrd_left = Label(label_rddrr_down, text=" Κατεύθυνση: ", borderwidth=1, highlightthickness=1, bg="floral white", font=("Calibri", 14))  # kateu8unsh text
    label_rddrrd_right = Label(label_rddrr_down, text="Θετική", borderwidth=2, highlightthickness=1, relief="sunken", bg="floral white", font=("Calibri", 14))  # kateu8unsh input

    descriptionText = Text(label_rul_right, height=8, bg="floral white", fg="gray44", borderwidth=0, highlightthickness=2,font=("Calibri", 12), width=55)
    descriptionText.insert(INSERT,"Ο Παρμενίδης ήταν αρχαίος έλληνας φιλόσοφος. Γεννήθηκε στην \nΕλέα της Μεγάλης Ελλάδας στα τέλη του 6ου αιώνα π.Χ., σε ένα \nπεριβάλλον επηρεασμένο από τις απόψεις του Πυθαγόρα και του Ξενοφάνη. Ο Παρμενίδης υποστήριξε ότι η πολλαπότητα των \nυπάρχοντων πραγμάτων, οι μεταβαλλόμενες μορφές και η κίνηση τους δεν είναι παρά μια εμφάνιση μιας ενιαίας αιώνιας \nπραγματικότητα (<<Όν>>), οδηγώντας έτσι στην παρμενίδια αρχή \nότι <<όλα είναι ένα>>.")
    descriptionText.config(state=DISABLED)#to be un editable

    ###sos gia na mhn bgalei erro bazw proxeira mono to prwto frame pou einia etoimo
    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raiseNdrop_frame(intro_Frame,none), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1 = Button(label_l_down, text="Δηλώσεις", command=lambda: raiseNdrop_frame(intro_Frame,none), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2 = Button(label_l_down, text="Εβδομαδιαίο Πρόγραμμα", command=lambda: raiseNdrop_frame(intro_Frame,none), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext3 = Button(label_l_down, text="Αποτελέσματα", command=lambda: raiseNdrop_frame(intro_Frame,none), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext4 = Button(label_l_down, text="Πανεπιστημιακά Ιδρύματα", command=lambda: raiseNdrop_frame(intro_Frame,none), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext5 = Button(label_l_down, text="Πληροφορίες Χρήστη", command=lambda: raiseNdrop_frame(intro_Frame,none), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext6 = Button(label_l_down, text="Ανακοινώσεις", command=lambda: raiseNdrop_frame(announcements_Frame,intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext7 = Button(label_l_down, text="Προβλήματα", command=lambda: raiseNdrop_frame(intro_Frame,announcements_Frame) , bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext8 = Button(label_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    ############## CALENDAR################
    cal = Calendar(label_rur_down, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', normalforeground ='black', weekendforeground='black', weekendbackground='gray63', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(label_rur_down, text="Hover over the events.").pack()





    #######################################     EMFANISH TOU UI apo ta teleutaia labels pros ta arxika
 
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

    label_rddr_right.pack(side=RIGHT)
    label_rddrr_up.pack(side=TOP)
    label_rddrru_left.pack(side=LEFT)
    label_rddrru_right.pack(side=RIGHT)
    label_rddrr_down.pack(side=BOTTOM)
    label_rddrrd_left.pack(side=LEFT)
    label_rddrrd_right.pack(side=RIGHT)

    ###########################################

    butttonNext0.pack(side=TOP,pady=2,ipady=5)
    butttonNext1.pack(side=TOP,pady=2,ipady=5)
    butttonNext2.pack(side=TOP,pady=2,ipady=5)
    butttonNext3.pack(side=TOP,pady=2,ipady=5)
    butttonNext4.pack(side=TOP,pady=2,ipady=5)
    butttonNext5.pack(side=TOP,pady=2,ipady=5)
    butttonNext6.pack(side=TOP,pady=2,ipady=5)
    butttonNext7.pack(side=TOP,pady=2,ipady=5)
    butttonNext8.pack(side=TOP,pady=2,ipady=5)

    descriptionText.pack()
    #init_Label.pack(fill=BOTH,expand=1)

    raiseNdrop_frame(menu_Frame,none)
    raiseNdrop_frame(intro_Frame,none)   
    raiseNdrop_frame(all_Frame,none)
    # --------------------------------------------------------------------------------------------------First Frame END, Start of PAGE ΑΝΑΚΟΙΝΩΣΕΙΣ
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    #announcements_Frame
    
    label_Announce = Label(announcements_Frame, text="Ανακοινώσεις", bg="floral white",font=("Times New Roman (Times)", 36, "bold"),fg="dodger blue")
    label_sortBy = Label(announcements_Frame, bg="floral white")
    label_sortBy1 = Label(label_sortBy, text="Ταξινόμηση κατά: ", bg="floral white", font=("Calibri", 18, "bold"))
    label_sortBy2 = Label(label_sortBy, bg="floral white")
    label_left = Label(announcements_Frame, bg="floral white")
    container_list = Frame(announcements_Frame)
    announcement_list  = Listbox (container_list, bg="floral white", borderwidth=2, highlightthickness=0)#width=getRes[0]-50, height=getRes[1]-70

    scrollbarh = Scrollbar(container_list, orient="horizontal", command=announcement_list.xview)
    scrollbarv= Scrollbar(container_list, orient="vertical", command=announcement_list.yview)
    container_list.bind("<Configure>",lambda e: announcement_list.configure(scrollregion=announcement_list.bbox("all")))
    announcement_list.configure(yscrollcommand=scrollbarv.set, xscrollcommand=scrollbarh.set, font=("Calibri", 40))
    container_list.bind("<MouseWheel>", scrollbarv)#ΚΑΘΕΤΟ SCROLL ΜΕ ΡΟΔΑ ΠΟΝΤΙΚΙΟΥ


    #####SOS SOS SOS selectmode  σαν atribute για επιλογη ανακοινωσεις απο λιστα και αντιστοιχο ανοιγμα αν πχ λινκ κλπ


    #DROP DOWN MENU ΓΙΑ ΕΠΙΛΟΓΗ SELECT ΑΠΟ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ
    sort_options=["Νεότερα", "Παλαιότερα", "Πιο Δημοφιλή"]
    sortBy_var = StringVar(label_sortBy2)
    sortBy_var.set(sort_options[0])#ΑΡΧΙΚΗ ΤΙΜΗ ΤΑ ΝΕΟΤΕΡΑ
    sort_choice = OptionMenu(label_sortBy2, sortBy_var, *sort_options)
    buttton_sort = Button(label_sortBy2, text="Επιβεβαίωση", command=lambda: sort_announcements, bg="gray26",font=("Calibri", 14, "bold"))
    
    #ΠΡΟΧΕΙΡΗ ΤΟΠΟΘΕΤΗΣΗ ΣΥΝΑΡΤΗΣΗΣ----------------------------------------------------------
    def sort_announcements():
    
        sort=sortBy_var.get()
        announcement_list.delete(0, END)#DELETE ΠΑΛΙΩΝ ΔΕΔΟΜΕΝΩΝ ΑΠΟ ΛΙΣΤΑ
        if sort=="Παλαιότερα":
            #ΕΝΤΟΛΕΣ ΔΙΑΣΥΝΔΕΣΗΣ ΜΕ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΜΕ SELECT ΜΕ ΒΑΣΗ ΗΜΕΡΟΜΗΝΙΑ ΑΝΑΚΟΙΝΩΣΕΩΝ
            #listbox.insert(position,item-string) #ισως να θελει for
            print("old news")
        elif sort=="Πιο Δημοφιλή":
            #ΕΝΤΟΛΕΣ ΔΙΑΣΥΝΔΕΣΗΣ ΜΕ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΜΕ SELECT ΜΕ ΒΑΣΗ ΗΜΕΡΟΜΗΝΙΑ ΑΝΑΚΟΙΝΩΣΕΩΝ
            #listbox.insert(position,item-string) #ισως να θελει for
            print("popular news")
        else: #sort==Νεότερα
            #ΕΝΤΟΛΕΣ ΔΙΑΣΥΝΔΕΣΗΣ ΜΕ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΜΕ SELECT ΜΕ ΒΑΣΗ ΗΜΕΡΟΜΗΝΙΑ ΑΝΑΚΟΙΝΩΣΕΩΝ
            #listbox.insert(position,item-string) #ισως να θελει for
            print("new news")


    #Εμφάνιση Labels κλπ στο frame ανακοινωσεων
    label_Announce.pack(side=TOP,ipady=10)
    label_sortBy.pack(side=TOP,pady=20)
    label_sortBy1.pack(side=LEFT)
    label_sortBy2.pack(side=LEFT)
    sort_choice.pack(side=LEFT,padx=20)
    buttton_sort.pack(side=LEFT,padx=20)
    container_list.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbarv.pack(side=RIGHT, fill=Y)
    scrollbarh.pack(side=BOTTOM, fill=X)
    announcement_list.pack(side=LEFT, fill=BOTH, expand=1)
    
    ###Test of insertion to ListBox ΚΑΝΟΝΙΚΑ ΑΥΤΑ ΘΑ ΤΑ ΠΑΡΕΙ ΜΕ SELECT ΑΠΟ ΤΗΝ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΜΑΣ
    #ΕΔΩ ΘΑ ΚΑΝΕΙ ΑΡΧΙΚΟ INSERT ΑΠΟ ΤΗΝ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ ΜΕ ΣΥΝΑΡΤΗΣΗ ΕΙΤΕ ΚΑΙ TRIGGER UPDATE ΑΠΟ ΕΝΗΜΕΡΩΣΕΙΣ TABLE
    announcement_list.insert(1, "This is a test to see if the listBox works as it should be")
    announcement_list.insert(2, "Ανακοινωση Ημερομηνίας Δηλώσεων")
    announcement_list.insert(3, "Πρόγραμμα εξεταστικής έτους 2020-2021")
    announcement_list.insert(4, "#ΜΕΝΟΥΜΕ_ΣΠΙΤΙ")
    announcement_list.insert(5, "PYTHON")
    announcement_list.insert(6, "ΠΑΡΜΕΝΙΔΗΣ ΜΕ TKINTER ΓΙΑ GUI")
    announcement_list.insert(7, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(8, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(9, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(10, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(11, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(12, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(13, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(14, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")
    announcement_list.insert(15, "Πεισσότερες Ανακοινώσεις για να δούμε σε πράξη το κάθετο scroll και το horizontal scroll")

    main_window.mainloop()  # ------------------------------Put always to end of frames

main()