#ΒΑΖΑΙΟΣ ΣΤΥΛΙΑΝΟΣ Α.Μ.: 1054284

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



    load0 = Image.open('gr.jpg')
    load0 = load0.resize((getRes[0], getRes[1]), Image.ANTIALIAS)
    render0 = ImageTk.PhotoImage(load0)
    P0=Label(image=render0)
    P0.place(x=0, y=0, relwidth=1, relheight=1)


    topTitle=Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")
    L1=Label(topTitle,text="Simplified-DES Encryption\Decryption\n", bg="salmon1",font=("Calibri", 24,"bold"))
    topLabel2=Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")
    descriptionText=Text(topLabel2,height=7,bg="salmon1",borderwidth=0,highlightthickness=0,font=("Calibri", 14), width = 100)
    descriptionText.insert(INSERT,"Περιγραφή S-DES:\nΟ αλγόριθμος κρυπτογράφησης Simplified Data Encryption Standard (S-DES) βασίζεται στην κρυπτογράφηση μπλοκ.\n Παίρνει σαν είσοδο ένα μπλοκ 8-bit απλού κειμένου ή 8-bit και ένα κλειδί μεγέθους  10-bit και τελικά παράγει ένα\n κρυπτογραφημένο μπλοκ 8-bit ciphertext ως έξοδο.Πρόκειται για ένα συμμετρικό κρυπτογράφο που έχει δύο επαναλήψεις,\n ενώ για την κρυπτογράφηση\αποκρυπτογράφηση χρησιμοποιούνται συγκεκριμένες μεταθέσεις των bits που ορίζονται από τον ίδιο τον αλγόριθμο.\n")

    butttonNext0=Button(topLabel2,text="Αρχική Σελίδα",command=lambda:raise_frame(intro_Frame),bg="SteelBlue3")
    #butttonNext1=Button(topLabel2,text="Δηλώσεις",command=lambda:raise_frame(statement_Frame),bg="SteelBlue3")
    #butttonNext2=Button(topLabel2,text="Εβδομαδιαίο Πρόγραμμα",command=lambda:raise_frame(weekly_program_Frame),bg="SteelBlue3")
    #butttonNext3=Button(topLabel2,text="Αποτελέσματα",command=lambda:raise_frame(results_Frame),bg="SteelBlue3")
    #butttonNext4=Button(topLabel2,text="Πανεπιστημιακά Ιδρύματα",command=lambda:raise_frame(institutions_Frame),bg="SteelBlue3")
    #butttonNext5=Button(topLabel2,text="Πληροφορίες Χρήστη",command=lambda:raise_frame(info_Frame),bg="SteelBlue3")
    #butttonNext6=Button(topLabel2,text="Ανακοινώσεις",command=lambda:raise_frame(announcements_Frame),bg="SteelBlue3")
    #butttonNext7=Button(topLabel2,text="Προβλήματα",command=lambda:raise_frame(problems_Frame),bg="SteelBlue3")#,height = 2, width = 7

    bottomLabel=Label(intro_Frame,borderwidth=0,highlightthickness=0, bg="salmon1")
    P1 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    #P2 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    #P3 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    #P3 = Label(bottomLabel,padx=(getRes[0]/10),bg="salmon1",borderwidth=0,highlightthickness=0)
    #P4 = Label(bottomLabel,image=render3,borderwidth=0,highlightthickness=0)
    L1.pack(side=TOP)
    topTitle.pack(side=TOP)
    topLabel2.pack(side=TOP)
    descriptionText.pack()
    butttonNext0.pack(side=RIGHT)
    #buttonExit1.pack(side=LEFT)
    P1.pack(side=LEFT)
    #P2.pack(side=LEFT)
    #P3.pack(side=RIGHT)
    bottomLabel.pack(side=BOTTOM)
    raise_frame(intro_Frame)
    #--------------------------------------------------------------------------------------------------First Frame END, Start of PAGE 1

    container.pack(side=TOP)
    canvas.pack(side="left", expand=True)
    scrollbarv.pack(side=RIGHT, fill="y")
    scrollbarh.pack(side=LEFT, fill="y")

    main_window.mainloop()#------------------------------Put always to end of frames

main()