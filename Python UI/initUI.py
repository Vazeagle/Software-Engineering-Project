# CAUTION IN ORDER TO RUN YOU NEED TO DOWNLOAD THE FOLLOWING PACKAGES: MouseInfo, Pillow, PyAutoGUI, PyGetWindow, PyMsgBox, PyRect, PyScreeze, pyperclip.
# SEE THE PDF REPORT FOR MORE INSTRUCTIONS ON HOW TO USE THE PROGRAMM

import os, sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry

getRes = pyautogui.size()
#resolution = str(getRes[0]-100) + "x" + str(getRes[1]-100)
main_window = Tk()


def raise_frame(frame):
    frame.tkraise()
    frame.grid(row=int(getRes[0]), column=0, sticky="news")

def ExitApp():
    MsgBox = messagebox.askquestion('Έξοδος Εφαρμογής!', 'Είστε σίγουροι ότι θέλετε να αποσυνδεθείτε από το σύστημα Παρμενίδης ;',
                                       icon='warning')
    if MsgBox == 'yes':
        main_window.destroy()
    else:
        messagebox.showinfo('Επιστροφή', 'Θα επιστραφείτε στην προηγούμενη σας οθόνη !')

def main():
    #main_window = Tk()
    #main_window.geometry(resolution) ###########################################resolution
    main_window.title("Parmenidis")
    main_window.configure()
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

    intro_Frame = Frame(main_window, bg="white")#, width=getRes[0], height=getRes[1])
    # statement_Frame=Frame(scrollable_frame,width=getRes[0], height=getRes[1], bg="salmon1")
    # weekly_program_Frame=Frame(scrollable_frame,width=getRes[0], height=getRes[0], bg="salmon1")
    # results_Frame=Frame(scrollable_frame, bg="salmon1",width=getRes[0], height=getRes[1])
    # institutions_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    # info_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    # announcements_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    # problems_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])

    ###prwth sel
    ####LOAD PICTURES
    load0 = Image.open('gr.jpg')
    load0 = load0.resize((getRes[0], getRes[1]), Image.ANTIALIAS)
    render0 = ImageTk.PhotoImage(load0)
    
    load1 = Image.open('P1.png')
    load1 = load1.resize((150, 200), Image.ANTIALIAS)
    render1 = ImageTk.PhotoImage(load1)
    
    load2 = Image.open('P2.gif')
    load2 = load2.resize((100, 100), Image.ANTIALIAS)
    render2 = ImageTk.PhotoImage(load2)

    load3 = Image.open('profil.jpg')
    load3 = load3.resize((100, 100), Image.ANTIALIAS)
    render3 = ImageTk.PhotoImage(load3)
    
    


    ####END PICTURES
    init_Label = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="SkyBlue1")

    #label_top = Label(init_Label, bg="gray26")  # TOP 8ESH
    #label_t_left = Label(label_top, text="test top left", bg="gray26",font=("Calibri", 24, "bold"))  # TOP 8ESH
    #label_t_right = Label(label_top, text="test top right", bg="gray26",font=("Calibri", 24, "bold"))  # TOP 8ESH

    label_left = Label(init_Label, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg="gray26",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, image=render2, text="ΦΩΤΟΓΤΑΦΙΑ\n ΠΑΡΜΕΝΊΔΗΣ", borderwidth=1, highlightthickness=0, bg="gray26")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray26")  # button gia menu kai alla frames

    label_right = Label(init_Label, borderwidth=1, highlightthickness=0, bg="salmon1")  # dexio menu
    label_r_up = Label(label_right, borderwidth=1, highlightthickness=0, bg="blue")  # panw meros me perilipsh kai hmerologio
    label_ru_up = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="red")  # kalos orisate+ to eniaio susthma klp
    label_ruu_up = Label(label_ru_up, text="Καλώς ήρθατε στον Παρμενίδη!\n", borderwidth=0, highlightthickness=0,bg="yellow", font=("Calibri", 24, "bold"))
    label_ruu_down = Label(label_ru_up, text="Το ενιαίο σύστημα για τις Πανελλήνιες Εξετάσεις.\n", borderwidth=0,highlightthickness=0, bg="salmon1", font=("Calibri", 18))

    # isws na 8elei up kai oxi left
    ####### kanoniko #####label_ru_left = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="salmon1")  # foto parmenidi+ desription parmenidi
    label_ru_left = Label(label_ru_up, borderwidth=1, highlightthickness=0,bg="salmon1")  # foto parmenidi+ desription parmenidi
    label_rul_left = Label(label_ru_left, image=render1, borderwidth=1, highlightthickness=0,bg="salmon1")  # foto parmenidi
    label_rul_right = Label(label_ru_left, borderwidth=1, highlightthickness=0,bg="salmon1")  # Ο παρμενιδης ειναι bla bla

    ########## KANONIKA ####label_ru_right = Label(label_r_up, borderwidth=0, highlightthickness=1,bg="salmon1")  # hmerologio gramma + hmerologio
    label_ru_right = Label(label_ru_up, borderwidth=0, highlightthickness=1,bg="salmon1")  # hmerologio gramma + hmerologio
    label_rur_up = Label(label_ru_right, text="Ημερολόγιο\n", borderwidth=1, highlightthickness=0, bg="salmon1",font=("Calibri", 18))  # hmerologio gramma
    label_rur_down = Label(label_ru_right, borderwidth=1, highlightthickness=0, bg="salmon1")  # hmerologio

    label_r_down = Label(label_right, borderwidth=1, highlightthickness=1, relief="solid", bg="salmon1")  # sunoptiko profil
    label_rd_up = Label(label_r_down, text="Συνοπτικό προφίλ:",relief="ridge", borderwidth=1, highlightthickness=0, bg="white",font=("Calibri", 18))  # sunoptiko profil
    label_rd_down = Label(label_r_down, borderwidth=1, highlightthickness=0, bg="salmon1")  # onoma xrhsth kai alla
    label_rdd_left = Label(label_rd_down,image=render3, borderwidth=0, highlightthickness=0, bg="white")  # eikona user
    label_rdd_right = Label(label_rd_down, borderwidth=1, highlightthickness=0,bg="salmon1")  # onoma xrhsth status lukeio kai alla

    label_rddr_left = Label(label_rdd_right, borderwidth=1, highlightthickness=0,bg="salmon1")  # onoma xrhsth kai status
    label_rddrl_up = Label(label_rddr_left, text="ΣΤΥΛΙΑΝΟΣ ΒΑΖΑΙΟΣ", borderwidth=1, highlightthickness=0, bg="salmon1",font=("Calibri", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="salmon1")  # katastash
    label_rddrld_left = Label(label_rddrl_down, text="Κατάσταση: ", borderwidth=1, highlightthickness=0, bg="salmon1",font=("Calibri", 14))  # katastash text
    label_rddrld_right = Label(label_rddrl_down, text="Προς Εξέταση", borderwidth=1, highlightthickness=1, relief="groove",bg="green2",font=("Calibri", 14))  # input katastashs apo data base

    label_rddr_right = Label(label_rdd_right, borderwidth=1, highlightthickness=1,bg="salmon1")  # lukeio kai kateu8unsh
    label_rddrr_up = Label(label_rddr_right, borderwidth=1, highlightthickness=1, bg="salmon1")  # lukeio genika
    label_rddrru_left = Label(label_rddrr_up, text=" Λύκειο: ", borderwidth=1, highlightthickness=1, bg="salmon1", font=("Calibri", 14))  # lukeio gramma
    label_rddrru_right = Label(label_rddrr_up,text="1ο Λύκειο Καισαριανής", borderwidth=1, highlightthickness=0,bg="salmon1", font=("Calibri", 14)) # lukeio input from db
    label_rddrr_down = Label(label_rddr_right, borderwidth=1, highlightthickness=1, bg="salmon1")  # katey8unsh
    label_rddrrd_left = Label(label_rddrr_down, text=" Κατεύθυνση: ", borderwidth=1, highlightthickness=1, bg="salmon1", font=("Calibri", 14))  # kateu8unsh text
    label_rddrrd_right = Label(label_rddrr_down, text="Θετική", borderwidth=2, highlightthickness=1, relief="sunken", bg="white", font=("Calibri", 14))  # kateu8unsh input

    descriptionText = Text(label_rul_right, height=8, bg="white", fg="gray44", borderwidth=0, highlightthickness=2,font=("Calibri", 12), width=55)
    descriptionText.insert(INSERT,"Ο Παρμενίδης ήταν αρχαίος έλληνας φιλόσοφος. Γεννήθηκε στην \nΕλέα της Μεγάλης Ελλάδας στα τέλη του 6ου αιώνα π.Χ., σε ένα \nπεριβάλλον επηρεασμένο από τις απόψεις του Πυθαγόρα και του Ξενοφάνη. Ο Παρμενίδης υποστήριξε ότι η πολλαπότητα των \nυπάρχοντων πραγμάτων, οι μεταβαλλόμενες μορφές και η κίνηση τους δεν είναι παρά μια εμφάνιση μιας ενιαίας αιώνιας \nπραγματικότητα (<<Όν>>), οδηγώντας έτσι στην παρμενίδια αρχή \nότι <<όλα είναι ένα>>.")
    descriptionText.config(state=DISABLED)#to be un editable

    ###sos gia na mhn bgalei erro bazw proxeira mono to prwto frame pou einia etoimo
    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext1 = Button(label_l_down, text="Δηλώσεις", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext2 = Button(label_l_down, text="Εβδομαδιαίο Πρόγραμμα", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext3 = Button(label_l_down, text="Αποτελέσματα", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext4 = Button(label_l_down, text="Πανεπιστημιακά Ιδρύματα", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext5 = Button(label_l_down, text="Πληροφορίες Χρήστη", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext6 = Button(label_l_down, text="Ανακοινώσεις", command=lambda: raise_frame(intro_Frame), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext7 = Button(label_l_down, text="Προβλήματα", command=lambda: raise_frame(intro_Frame) , bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))
    butttonNext8 = Button(label_l_down, text="Έξοδος", command=lambda: ExitApp(), bg="gray26",height = 2, width = 35,font=("Calibri", 14, "bold"))

    ############## CALENDAR################
    cal = Calendar(label_rur_down, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(label_rur_down, text="Hover over the events.").pack()





    #######################################     EMFANISH TOU UI apo ta teleutaia labels pros ta arxika

    #label_top.pack(side=TOP) # TOP 8ESH
    #label_t_left.pack(side=LEFT) # TOP 8ESH
    #label_t_right.pack(side=LEFT) # TOP 8ESH

   # w.pack(fill=tk.X, padx=10)

    #####SOS SOS SOS DOKIMH ME GRID GIA BELTISTO UI label_left.grid(row=0,column=0)
    
    label_left.pack(side=LEFT)
    label_l_up.pack(side=TOP)
    label_l_down.pack(side=TOP)

    label_right.pack(side=LEFT,ipady=40,ipadx=100)
    label_r_up.pack(side=TOP,ipady=10)#kalos hr8ate+eniaio susthma+perilhpsh+calendar
    label_ru_up.pack(side=TOP,ipady=60)
    label_ruu_up.pack(side=TOP,pady=10)
    label_ruu_down.pack(side=TOP)

    # isws na 8elei up kai oxi left
    label_ru_left.pack(side=LEFT)
    label_rul_left.pack(side=LEFT)#eikona pamenidi
    label_rul_right.pack(side=LEFT)#peilhpsh

    label_ru_right.pack(side=LEFT)
    label_rur_up.pack(side=TOP)#hmerologio gramma
    label_rur_down.pack(side=TOP,padx=50,ipady=30,ipadx=30)#,ipadx=40,ipady=30)#calendar

    label_r_down.pack(side=TOP,ipadx=50)
    label_rd_up.pack(side=TOP)
    label_rd_down.pack(side=BOTTOM)
    label_rdd_left.pack(side=LEFT)
    label_rdd_right.pack(side=RIGHT)

    label_rddr_left.pack(side=LEFT)
    label_rddrl_up.pack(side=TOP,ipady=5)
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
    init_Label.pack(ipady=120,ipadx=265)


    raise_frame(intro_Frame)
    # --------------------------------------------------------------------------------------------------First Frame END, Start of PAGE 1

    #container.pack(side=TOP)
    #canvas.pack(side=LEFT, fill = BOTH, expand = True)
    #scrollbarv.pack(side=RIGHT, fill="y")
    #scrollbarh.pack(side=LEFT, fill="y")

    main_window.mainloop()  # ------------------------------Put always to end of frames


main()