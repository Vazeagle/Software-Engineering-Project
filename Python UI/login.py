import os, sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from TkTreectrl import *
import TkTreectrl as treectrl
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import pyautogui
from datetime import datetime
from tkcalendar import Calendar, DateEntry
none="none" # προσωρινο για μεταβαση σε frames
previous_frame="previous_frame"
frame_counter=0
init_pass=0
mydir=os.getcwd()
memory_dir=None
selected_row=None  #αρχικοποίηση μεταβλητης για να παίρνω το row που έχει επιλεχθεί στα προγράμματα
user1=[]#arxikopoihsh pinaka
user2=[]
user3=[]
user4=[]
user5=[]


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

    
load2 = Image.open('P2.gif')
load2 = load2.resize((100, 100), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(load2)


def memory():    #function to create a folder that contains txts with memory
    global user1#arxikopoihsh pinaka
    global user2
    global user3
    global user4
    global user5
    try:
        if not os.path.exists('Memory'):
            os.makedirs('Memory')
            messagebox.showinfo('Προσοχή',"Ο φάκελος Memory μόλις δημιουργήθηκε\n")
            memory_dir = mydir+"\Memory"
            #αρχικοποίηση στοιχείων-data
            user1=['vastyl','24682468','id(1)']#arxikopoihsh pinaka
            user2=['ceidupatras','244466666','id(2)']
            user3=['1gelklytorias','qwerty','id(3)']
            user4=['sviganast','1357913579','id(4)']
            user5=['dimitrog','helpme','id(5)']
        else:
            #messagebox.showinfo('Προσοχή'," Folder Memory already exists\n")
            memory_dir = mydir+"\Memory"

            #path arxeiwn
            login_path = memory_dir + "\login.txt"

            #check if all needed files exist!
            if os.path.isfile(login_path):
                print ("File login exist")#read
                login_path = open(login_path, "r")
                print(login_path)
                login_data = login_path.readlines()
                line_count=0
                for usrline in login_data:
                    line_count+=1
                    cur_user = usrline.strip()#removes\n from each line of the text
                    if(line_count==1):
                       user1 = cur_user.split(",")
                    elif(line_count==2):
                        user2 = cur_user.split(",")
                    elif(line_count==3):
                        user3 = cur_user.split(",")
                    elif(line_count==4):
                        user4 = cur_user.split(",")
                    elif(line_count==5):
                        user5 = cur_user.split(",")

            else:
                print ("File login created")#created
                login_data = open(login_path, "w")
                login_data.close()
    except OSError:
        messagebox.showinfo('Προσοχή',"Error creating directory "+(mydir)+"\Memory")


###frames
frame_temp=Frame()#Frame to get as temp to successfull change between frames
intro_Frame = Frame(main_window, bg="floral white")
exit_frame=Frame(intro_Frame, bg="floral white") #eksodos


def main():
    
    login_all=Label(intro_Frame, borderwidth=1, highlightthickness=0, bg="floral white")
    
    label_top = Label(login_all, borderwidth=1, highlightthickness=0,bg="floral white")  # kalos orisate+ to eniaio susthma klp
    label_pic = Label(label_top, image=render2, borderwidth=1, highlightthickness=0, bg="floral white")
    label_parmen = Label(label_top, text="ΣΥΣΤΗΜΑ ΠΑΡΜΕΝΙΔΗΣ\n", borderwidth=0,highlightthickness=0, bg="floral white", font=("Times New Roman (Times)", 24, "bold"))
    label_top3 = Label(login_all,bg="white", borderwidth=2, highlightthickness=2, relief="groove")

    
    login_usr = Label(label_top3, bg="white")
    login_usr1 = Label(login_usr, text="Όνομα Χρήστη:",  bg="white",font=("Times New Roman (Times)", 16, "bold"),fg="black")
    login_usr2 = Text(login_usr, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))
    
    login_passw = Label(label_top3, bg="white")
    login_passw1 = Label(login_passw, text="Κωδικός Πρόσβασης:",  bg="white",font=("Times New Roman (Times)", 16, "bold"),fg="black")
    login_passw2 = Text(login_passw, bg="WHITE", height=1, width=40, fg="black", borderwidth=1, highlightthickness=2,font=("Times New Roman (Times)", 16))

    label_buttons = Label(label_top3, bg="floral white")
    btn_acccept = Button(label_buttons, text="Σύνδεση", command=lambda: datacheck(), bg="green3",font=("Times New Roman (Times)", 14, "bold"),height=1 ,width=12)
    btn_exit = Button(label_buttons, text="Έξοδος", command=lambda: ExitApp(), bg="gray",font=("Calibri", 14, "bold"),height=1 ,width=12)


    def datacheck():
        usr_name = login_usr2.get('1.0', 'end-1c')
        usr_pass = login_passw2.get('1.0', 'end-1c')
        

        if arr[0][0]==usr_name and arr[0][1]==usr_pass:
            main_window.destroy()
            from initUI import main
        elif arr[1][0]==usr_name and arr[1][1]==usr_pass:
            main_window.destroy()
            from department import main
        elif arr[2][0]==usr_name and arr[2][1]==usr_pass:
            main_window.destroy()
            from school import main
        elif arr[3][0]==usr_name and arr[3][1]==usr_pass:
            main_window.destroy()
            from Grader import main
        elif arr[4][0]==usr_name and arr[4][1]==usr_pass:
            main_window.destroy()
            from board import main    
        else:
            messagebox.showinfo('Ανεπιτυχής Σύνδεση', 'Παρακαλώ πληκτρολογείστε τα σωστά στοιχεία.', icon='error')



    login_all.pack(side = TOP, fill=BOTH, expand=1)


    label_top.pack(side=TOP,fill=X,expand=1)
    label_pic.pack(side=TOP)
    label_parmen.pack(side=TOP)
    label_top3.pack(side=TOP,fill=Y,expand=1)

    
    login_usr.pack(side=TOP)
    login_usr1.pack(side = LEFT, ipadx=35)
    login_usr2.pack(side = LEFT, ipadx=35)
    
    login_passw.pack(side=TOP)
    login_passw1.pack(side = LEFT, ipadx=35)
    login_passw2.pack(side = LEFT, ipadx=35)

    label_buttons.pack(side=TOP)
    btn_acccept.pack(side = LEFT, padx=10)
    btn_exit.pack(side = LEFT, padx=10)


    raiseNdrop_frame(intro_Frame,none)

    
    

##### AUTO EINAI TO TELEUTAIO KOMMATI TOU KWDIKA
    main_window.mainloop()

memory()
main()

