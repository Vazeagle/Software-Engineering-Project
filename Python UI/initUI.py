

#CAUTION IN ORDER TO RUN YOU NEED TO DOWNLOAD THE FOLLOWING PACKAGES: MouseInfo, Pillow, PyAutoGUI, PyGetWindow, PyMsgBox, PyRect, PyScreeze, pyperclip.
#SEE THE PDF REPORT FOR MORE INSTRUCTIONS ON HOW TO USE THE PROGRAMM

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pyautogui
from datetime import datetime

getRes=pyautogui.size()
resolution=str(getRes[0])+"x"+str(getRes[1])

def raise_frame(frame):
    frame.tkraise()
    frame.grid(row=int(getRes[0]),column=0,sticky="news")

def main():
    #main window tkinter
    main_window=Tk()
    main_window.geometry(resolution) ###########################################resolution
    main_window.title("Parmenidis")
    main_window.configure(background='salmon1')
    #---------------------------------------------------
    container = ttk.Frame(main_window,width=getRes[0], height=getRes[1])
    canvas = Canvas(container, bg="salmon1",width=getRes[0]-50, height=getRes[1]-70,borderwidth=0,highlightthickness=0)
    scrollbarv = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbarh = ttk.Scrollbar(container, orient="vertical", command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbarv.set, xscrollcommand=scrollbarh.set)

    #---------------------------------------------------


    intro_Frame=Frame(scrollable_frame, bg="black",width=getRes[0], height=getRes[1])
    #statement_Frame=Frame(scrollable_frame,width=getRes[0], height=getRes[1], bg="salmon1")
    #weekly_program_Frame=Frame(scrollable_frame,width=getRes[0], height=getRes[0], bg="salmon1")
    #results_Frame=Frame(scrollable_frame, bg="salmon1",width=getRes[0], height=getRes[1])
    #institutions_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    #info_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    #announcements_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    #problems_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])

###prwth sel

    load0 = Image.open('gr.jpg')
    load0 = load0.resize((getRes[0], getRes[1]), Image.ANTIALIAS)
    render0 = ImageTk.PhotoImage(load0)



    init_Label = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")


    label_left = Label(init_Label,text="Simplified-DES Encryption\Decryption\n", bg="salmon1",font=("Calibri", 24,"bold"))#aristero menu
    label_l_up = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#photo parmenidi
    label_l_down = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#button gia menu kai alla frames
    
    label_right = Label(init_Label,borderwidth=0,highlightthickness=0, bg="salmon1")#dexio menu
    label_r_up = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#panw meros me perilipsh kai hmerologio
    label_ru_up = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#kalos orisate+ to eniaio susthma klp
    label_ruu_up = Label(intro_Frame,text="Καλώς ήρθατε στον Παρμενίδη!\n",borderwidth=0,highlightthickness=0, bg="salmon1",font=("Calibri", 24,"bold"))
    label_ruu_down = Label(intro_Frame,text="Το ενιαίο σύστημα για τις Πανελλήνιες Εξετάσεις.\n",borderwidth=0,highlightthickness=0, bg="salmon1",font=("Calibri", 18))

    label_ru_left = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#foto parmenidi+ desription parmenidi
    label_rul_left = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#foto parmenidi
    label_rul_right = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#eniaio susthma bla bla
    
    label_ru_right = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#hmerologio gramma + hmerologio
    label_rur_up = Label(intro_Frame,text="Ημερολόγιο\n",borderwidth=0,highlightthickness=0, bg="salmon1",font=("Calibri", 18))#hmerologio gramma 
    label_rur_down = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1") #hmerologio
    
    label_r_down = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#sunoptiko profil
    label_rd_up = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#sunoptiko profil
    label_rd_down = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#onoma xrhsth kai alla
    label_rdd_left = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#eikona user
    label_rdd_right = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#onoma xrhsth status lukeio kai alla

    label_rddr_left = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#onoma xrhsth kai status
    label_rddrl_up = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#onoma xrhsth
    label_rddrl_down = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#katastash
    label_rddrld_left = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#katastash text
    label_rddrld_right = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#input katastashs apo data base

    label_rddr_right = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#lukeio kai kateu8unsh
    label_rddrr_top = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#lukeio
    label_rddrr_down = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#katey8unsh
    label_rddrrd_left = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#kateu8unsh text
    label_rddrrd_right = Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")#kateu8unsh input

    #descriptionText=Text(topLabel2,height=7,bg="salmon1",borderwidth=0,highlightthickness=0,font=("Calibri", 14), width = 100)
    #descriptionText.insert(INSERT,"Περιγραφή S-DES:\nΟ αλγόριθμος κρυπτογράφησης Simplified Data Encryption Standard (S-DES) βασίζεται στην κρυπτογράφηση μπλοκ.\n Παίρνει σαν είσοδο ένα μπλοκ 8-bit απλού κειμένου ή 8-bit και ένα κλειδί μεγέθους  10-bit και τελικά παράγει ένα\n κρυπτογραφημένο μπλοκ 8-bit ciphertext ως έξοδο.Πρόκειται για ένα συμμετρικό κρυπτογράφο που έχει δύο επαναλήψεις,\n ενώ για την κρυπτογράφηση\αποκρυπτογράφηση χρησιμοποιούνται συγκεκριμένες μεταθέσεις των bits που ορίζονται από τον ίδιο τον αλγόριθμο.\n")





    butttonNext0=Button(label_l_down,text="Αρχική Σελίδα",command=lambda:raise_frame(intro_Frame),bg="SteelBlue3")
    #butttonNext1=Button(label_l_down,text="Δηλώσεις",command=lambda:raise_frame(statement_Frame),bg="SteelBlue3")
    #butttonNext2=Button(label_l_down,text="Εβδομαδιαίο Πρόγραμμα",command=lambda:raise_frame(weekly_program_Frame),bg="SteelBlue3")
    #butttonNext3=Button(label_l_down,text="Αποτελέσματα",command=lambda:raise_frame(results_Frame),bg="SteelBlue3")
    #butttonNext4=Button(label_l_down,text="Πανεπιστημιακά Ιδρύματα",command=lambda:raise_frame(institutions_Frame),bg="SteelBlue3")
    #butttonNext5=Button(label_l_down,text="Πληροφορίες Χρήστη",command=lambda:raise_frame(info_Frame),bg="SteelBlue3")
    #butttonNext6=Button(label_l_down,text="Ανακοινώσεις",command=lambda:raise_frame(announcements_Frame),bg="SteelBlue3")
    #butttonNext7=Button(label_l_down,text="Προβλήματα",command=lambda:raise_frame(problems_Frame),bg="SteelBlue3")#,height = 2, width = 7
    #butttonNext8=Button(label_l_down,text="Έξοδος",command=lambda:raise_frame(problems_Frame),bg="SteelBlue3")#,height = 2, width = 7

    #bottomLabel=Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="white")
    #P1 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    #P2 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    #P3 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    #P3 = Label(bottomLabel,padx=(getRes[0]/10),bg="salmon1",borderwidth=0,highlightthickness=0)
    #P4 = Label(bottomLabel,image=render3,borderwidth=0,highlightthickness=0)
    
    P0=Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    P0.place(x=0, y=0, relwidth=1, relheight=1)
    L1.pack(side=TOP)
    topTitle.pack(side=TOP)
    topLabel2.pack(side=TOP)
    descriptionText.pack()
    
    ############################prepei na mpoun sto sygkekrimeno label tous
    #butttonNext0.pack(side=TOP)
    #butttonNext1.pack(side=TOP)
    #butttonNext2.pack(side=TOP)
    #butttonNext3.pack(side=TOP)
    #butttonNext4.pack(side=TOP)
    #butttonNext5.pack(side=TOP)
    #butttonNext6.pack(side=TOP)
    #butttonNext7.pack(side=TOP)
    #butttonNext8.pack(side=TOP)
    
    #P1.pack(side=LEFT)

    
    raise_frame(intro_Frame)
    #--------------------------------------------------------------------------------------------------First Frame END, Start of PAGE 1

    container.pack(side=TOP)
    canvas.pack(side="left", expand=True)
    scrollbarv.pack(side=RIGHT, fill="y")
    scrollbarh.pack(side=LEFT, fill="y")

    main_window.mainloop()#------------------------------Put always to end of frames

main()