# CAUTION IN ORDER TO RUN YOU NEED TO DOWNLOAD THE FOLLOWING PACKAGES: MouseInfo, Pillow, PyAutoGUI, PyGetWindow, PyMsgBox, PyRect, PyScreeze, pyperclip.
# SEE THE PDF REPORT FOR MORE INSTRUCTIONS ON HOW TO USE THE PROGRAMM

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import pyautogui
from datetime import datetime

getRes = pyautogui.size()
resolution = str(getRes[0]) + "x" + str(getRes[1])


def raise_frame(frame):
    frame.tkraise()
    frame.grid(row=int(getRes[0]), column=0, sticky="news")


def main():
    main_window = Tk()
    main_window.geometry(resolution) ###########################################resolution
    main_window.title("Parmenidis")
    main_window.configure(background='green')
    # ---------------------------------------------------
    container = ttk.Frame(main_window, width=getRes[0], height=getRes[1])
    canvas = Canvas(container, bg="blue", width=getRes[0] - 50, height=getRes[1] - 70, borderwidth=0, highlightthickness=0)
    scrollbarv = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbarh = ttk.Scrollbar(container, orient="vertical", command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbarv.set, xscrollcommand=scrollbarh.set)

    # ---------------------------------------------------

    intro_Frame = Frame(scrollable_frame, bg="white", width=getRes[0], height=getRes[1])
    # statement_Frame=Frame(scrollable_frame,width=getRes[0], height=getRes[1], bg="salmon1")
    # weekly_program_Frame=Frame(scrollable_frame,width=getRes[0], height=getRes[0], bg="salmon1")
    # results_Frame=Frame(scrollable_frame, bg="salmon1",width=getRes[0], height=getRes[1])
    # institutions_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    # info_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    # announcements_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])
    # problems_Frame = Frame(scrollable_frame, bg="salmon1", width=getRes[0], height=getRes[1])

    ###prwth sel

    load0 = Image.open('gr.jpg')
    load0 = load0.resize((getRes[0], getRes[1]), Image.ANTIALIAS)
    render0 = ImageTk.PhotoImage(load0)

    init_Label = Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="salmon1")

    label_left = Label(init_Label, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", bg="gray17",font=("Calibri", 24, "bold"))  # aristero menu
    label_l_up = Label(label_left, text="ΦΩΤΟΓΤΑΦΙΑ\n ΠΑΡΜΕΝΊΔΗΣ", borderwidth=1, highlightthickness=0, bg="gray17")  # photo parmenidi
    label_l_down = Label(label_left, borderwidth=1, highlightthickness=0,bg="gray17")  # button gia menu kai alla frames

    label_right = Label(init_Label, borderwidth=1, highlightthickness=0, bg="salmon1")  # dexio menu
    label_r_up = Label(label_right, borderwidth=1, highlightthickness=0, bg="salmon1")  # panw meros me perilipsh kai hmerologio
    label_ru_up = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="salmon1")  # kalos orisate+ to eniaio susthma klp
    label_ruu_up = Label(label_ru_up, text="Καλώς ήρθατε στον Παρμενίδη!\n", borderwidth=0, highlightthickness=0,bg="salmon1", font=("Calibri", 24, "bold"))
    label_ruu_down = Label(label_ru_up, text="Το ενιαίο σύστημα για τις Πανελλήνιες Εξετάσεις.\n", borderwidth=0,highlightthickness=0, bg="salmon1", font=("Calibri", 18))

    # isws na 8elei up kai oxi left
    label_ru_left = Label(label_r_up, borderwidth=1, highlightthickness=0,bg="salmon1")  # foto parmenidi+ desription parmenidi
    label_rul_left = Label(label_ru_left, text="PHOTO PARMENIDI", borderwidth=1, highlightthickness=0,bg="salmon1")  # foto parmenidi
    label_rul_right = Label(label_ru_left, borderwidth=1, highlightthickness=0,bg="salmon1")  # Ο παρμενιδης ειναι bla bla

    label_ru_right = Label(label_r_up, borderwidth=0, highlightthickness=1,bg="salmon1")  # hmerologio gramma + hmerologio
    label_rur_up = Label(label_ru_right, text="Ημερολόγιο\n", borderwidth=1, highlightthickness=0, bg="salmon",font=("Calibri", 18))  # hmerologio gramma
    label_rur_down = Label(label_ru_right, borderwidth=1, highlightthickness=0, bg="salmon1")  # hmerologio

    label_r_down = Label(label_right, borderwidth=1, highlightthickness=0, bg="salmon1")  # sunoptiko profil
    label_rd_up = Label(label_r_down, text="Συνοπτικό προφίλ:", borderwidth=1, highlightthickness=0, bg="salmon",font=("Calibri", 18))  # sunoptiko profil
    label_rd_down = Label(label_r_down, borderwidth=1, highlightthickness=0, bg="salmon1")  # onoma xrhsth kai alla
    label_rdd_left = Label(label_rd_down, text="eikona user", borderwidth=1, highlightthickness=0, bg="salmon1")  # eikona user
    label_rdd_right = Label(label_rd_down, borderwidth=1, highlightthickness=0,
                            bg="salmon1")  # onoma xrhsth status lukeio kai alla

    label_rddr_left = Label(label_rdd_right, borderwidth=1, highlightthickness=0,bg="salmon1")  # onoma xrhsth kai status
    label_rddrl_up = Label(label_rddr_left, text="Όνομα χρήστη\t", borderwidth=1, highlightthickness=0, bg="salmon1",font=("Calibri", 18))  # onoma xrhsth
    label_rddrl_down = Label(label_rddr_left, borderwidth=1, highlightthickness=0, bg="salmon1")  # katastash
    label_rddrld_left = Label(label_rddrl_down, text="Κατάσταση:\t", borderwidth=1, highlightthickness=0, bg="salmon1",font=("Calibri", 18))  # katastash text
    label_rddrld_right = Label(label_rddrl_down, borderwidth=1, highlightthickness=0,bg="salmon1")  # input katastashs apo data base

    label_rddr_right = Label(label_rdd_right, borderwidth=1, highlightthickness=0,bg="salmon1")  # lukeio kai kateu8unsh
    label_rddrr_up = Label(label_rddr_right, borderwidth=1, highlightthickness=0, bg="salmon1")  # lukeio genika
    label_rddrru_left = Label(label_rddrr_up, borderwidth=1, highlightthickness=0, bg="salmon1")  # lukeio gramma
    label_rddrru_right = Label(label_rddrr_up,text="Λύκειο: ", borderwidth=0, highlightthickness=0,bg="salmon1", font=("Calibri", 18)) # lukeio input from db
    label_rddrr_down = Label(label_rddr_right, borderwidth=1, highlightthickness=0, bg="salmon1")  # katey8unsh
    label_rddrrd_left = Label(label_rddrr_down, borderwidth=1, highlightthickness=0, bg="salmon1")  # kateu8unsh text
    label_rddrrd_right = Label(label_rddrr_down, borderwidth=1, highlightthickness=0, bg="salmon1")  # kateu8unsh input

    descriptionText = Text(label_rul_right, height=7, bg="green", borderwidth=2, highlightthickness=0,font=("Calibri", 14), width=100)
    descriptionText.insert(INSERT,"Ο Παρμενίδης ήταν αρχαίος έλληνας φιλόσοφος. Γεννήθηκε στην Ελέα της Μεγάλης Ελλάδας\n στα τέλητου 6ου αιώνα π.Χ., ....")

    ###sos gia na mhn bgalei erro bazw proxeira mono to prwto frame pou einia etoimo
    butttonNext0 = Button(label_l_down, text="Αρχική Σελίδα", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext1 = Button(label_l_down, text="Δηλώσεις", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext2 = Button(label_l_down, text="Εβδομαδιαίο Πρόγραμμα", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext3 = Button(label_l_down, text="Αποτελέσματα", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext4 = Button(label_l_down, text="Πανεπιστημιακά Ιδρύματα", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext5 = Button(label_l_down, text="Πληροφορίες Χρήστη", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext6 = Button(label_l_down, text="Ανακοινώσεις", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")
    butttonNext7 = Button(label_l_down, text="Προβλήματα", command=lambda: raise_frame(intro_Frame) , bg="SteelBlue3")  # ,height = 2, width = 7
    butttonNext8 = Button(label_l_down, text="Έξοδος", command=lambda: raise_frame(intro_Frame), bg="SteelBlue3")  # ,height = 2, width = 7

    # P1 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    # P2 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    # P3 = Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    # P3 = Label(bottomLabel,padx=(getRes[0]/10),bg="salmon1",borderwidth=0,highlightthickness=0)
    # P4 = Label(bottomLabel,image=render3,borderwidth=0,highlightthickness=0)
    # P1.pack(side=LEFT)

    # P0=Label(bottomLabel,image=render0,borderwidth=0,highlightthickness=0)
    # P0.place(x=0, y=0, relwidth=1, relheight=1)
    # L1.pack(side=TOP)
    # topTitle.pack(side=TOP)
    # topLabel2.pack(side=TOP)
    # 
    #######################################     EMFANISH TOU UI apo ta teleutaia labels pros ta arxika

    label_left.pack(side=LEFT)
    label_l_up.pack(side=TOP)
    label_l_down.pack(side=BOTTOM)

    label_right.pack(side=RIGHT)
    label_r_up.pack(side=TOP)
    label_ru_up.pack(side=TOP)
    label_ruu_up.pack(side=TOP)
    label_ruu_down.pack(side=BOTTOM)

    # isws na 8elei up kai oxi left
    label_ru_left.pack(side=LEFT)
    label_rul_left.pack(side=LEFT)
    label_rul_right.pack(side=RIGHT)

    label_ru_right.pack(side=RIGHT)
    label_rur_up.pack(side=TOP)
    label_rur_down.pack(side=BOTTOM)

    label_r_down.pack(side=BOTTOM)
    label_rd_up.pack(side=TOP)
    label_rd_down.pack(side=BOTTOM)
    label_rdd_left.pack(side=LEFT)
    label_rdd_right.pack(side=RIGHT)

    label_rddr_left.pack(side=LEFT)
    label_rddrl_up.pack(side=TOP)
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

    butttonNext0.pack(side=TOP)
    butttonNext1.pack(side=TOP)
    butttonNext2.pack(side=TOP)
    butttonNext3.pack(side=TOP)
    butttonNext4.pack(side=TOP)
    butttonNext5.pack(side=TOP)
    butttonNext6.pack(side=TOP)
    butttonNext7.pack(side=TOP)
    butttonNext8.pack(side=TOP)

    descriptionText.pack()

    init_Label.pack(fill=BOTH)

    raise_frame(intro_Frame)
    # --------------------------------------------------------------------------------------------------First Frame END, Start of PAGE 1

    container.pack(side=TOP)
    canvas.pack(side="left", expand=True)
    scrollbarv.pack(side=RIGHT, fill="y")
    scrollbarh.pack(side=LEFT, fill="y")

    main_window.mainloop()  # ------------------------------Put always to end of frames


main()