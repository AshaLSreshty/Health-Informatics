#iDigiHealth - Patient Information System
# Dashboard for Doctor Consultation of Patient
# Developed using Python and Tkinter
# Database - MySQL, MySQL Workbench, mysql-connector-python 
# Author - Dr. Ashalatha Sreshty Mamidi
import tkinter as tk
import mysql
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "alsy", database = "idigihealth_db")
mycursor = mydb.cursor()

#Appointment_top = tk.Toplevel(PIS)
Consultn = tk.Tk()
Consultn.title("Doctor Consultation")
Consultn.iconbitmap('Lab.ico')
Consultn.geometry('800x800')
#photo=PhotoImage(file='031Blessing.png')
#HmLab.configure(bg='#00b0c6')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('014AmyCrisp.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(Consultn, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

# Defining functions

def Enter():
    Con_ID=ConsultnID_EB.get()
    dbCon_ID=""
    Select="SELECT Consultation_ID FROM consultation WHERE Consultation_ID='%s'" %(Con_ID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbCon_ID=i[0]
    if(Con_ID == dbCon_ID):
        messagebox.askokcancel("Information","Record already taken")
    else:
        Insert="INSERT INTO consultation (Consultation_ID, Appointment_ID, Medical_History, Diagnosis, Assessment, Treatment_Plan, Consultation_Fees) values(%s,%s,%s,%s,%s,%s,%s)"
        Con_ID = ConsultnID_EB.get()
        App_ID = AppointmentID_EB.get()
        MedHis = MedHistory_EB.get("1.0","end-1c")
        Diags = Diagnosis_EB.get("1.0","end-1c")
        Assess = Assessment_EB.get("1.0","end-1c")
        TrtPln = TreatPlan_EB.get("1.0","end-1c")
        ConFee = ConsultFees_EB.get()
       
        if (App_ID !="" and MedHis !="" and Diags !="" and Assess !="" and TrtPln !="" and ConFee !=""):
            Value=(Con_ID, App_ID, MedHis, Diags, Assess,TrtPln, ConFee)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted successfully")
            ConsultnID_EB.delete(0, END)
            AppointmentID_EB.delete(0, END)
            MedHistory_EB.delete(0, END)
            Diagnosis_EB.delete(0, END)
            Assessment_EB.delete(0, END)
            TreatPlan_EB.delete(0, END)
            ConsultFees_EB.delete(0, END)

        else:
            if (Appointment_ID =="" and Medical_History =="" and Diagnosis =="" and Assessment =="" and Treatment_Plan =="" and Consultation_Fees ==""):
             messagebox.askokcancel("Information","New Doctor - fill all details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")
#        populate_list()

def Fetch():
    if(ConsultnID_EB.get() == ""):
        messagebox.showinfo("Fetch status", "Consultation ID is compulsory to fetch details")
    else:
        mycursor.execute("SELECT * FROM consultation WHERE Consultation_ID = '"+ ConsultnID_EB.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
            AppointmentID_EB.insert(0, row[1])
            MedHistory_EB.insert(0, row[2])
            Diagnosis_EB.insert(0, row[3])
            Assessment_EB.insert(0, row[4])
            TreatPlan_EB.insert(0, row[5])
            ConsultFees_EB.insert(0, row[6])
            populate_list()

def Remove():
    Con_ID=ConsultnID_EB.get() # Appointment_ID here is a variable
    Delete="DELETE FROM consultation WHERE Consultation_ID='%s'" %(Con_ID)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Record removed")
    ConsultnID_EB.delete(0, END)
    AppointmentID_EB.delete(0, END)
    MedHistory_EB.delete(0, END)
    Diagnosis_EB.delete(0, END)
    Assessment_EB.delete(0, END)
    TreatPlan_EB.delete(0, END)
    ConsultFees_EB.delete(0, END)

#    populate_list()

def Update():
    Con_ID = ConsultnID_EB.get()
    App_ID = AppointmentID_EB.get()
    MedHis = MedHistory_EB.get("1.0","end-1c")
    Diags = Diagnosis_EB.get("1.0","end-1c")
    Assess = Assessment_EB.get("1.0","end-1c")
    TrtPln = TreatPlan_EB.get("1.0","end-1c")
    ConFee = ConsultFees_EB.get()
    Update="UPDATE consultation SET Consultation_ID ='%s', Appointment_ID ='%s', Medical_History ='%s', Diagnosis = '%s', Assessment = '%s', Treatment_Plan = '%s', Consultation_Fees = '%s'" %(Con_ID, App_ID, MedHis, Diags, Assess, TrtPln, ConFee)
    mycursor.execute(Update)
    mydb.commit()
 #   populate_list()
    messagebox.showinfo("Information","Record updated successfully")

def Clear():
    ConsultnID_EB.delete(0, END)
    AppointmentID_EB.delete(0, END)
    MedHistory_EB.delete(0, END)
    Diagnosis_EB.delete(0, END)
    Assessment_EB.delete(0, END)
    TreatPlan_EB.delete(0, END)
    ConsultFees_EB.delete(0, END)    

# Title Frame and Label
Cons_PIS = ttk.Label(Consultn, text = "DOCTOR CONSULTATION", font = "Helvetica 20 bold", background = '#ffffff')
Cons_PIS.place(relx=.50, rely=.03, anchor="n")

# Create Labels
Consultn_ID =  ttk.Label(Consultn, text = 'CONSULTATION ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
Consultn_ID.place(relx=.05, rely=.25, anchor="w")

Appointment_ID = ttk.Label(Consultn, text = 'APPOINTMENT ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
Appointment_ID.place(relx=.55, rely=.25, anchor="w")

Med_History = ttk.Label(Consultn, text = 'MEDICAL HISTORY: ', font = "Helvetica 12 bold", background = '#fff6a4')
Med_History.place(relx=.05, rely=.40, anchor="w")

Diagnosis = ttk.Label(Consultn, text = 'DIAGNOSIS: ', font = "Helvetica 12 bold", background = '#fff6a4')
Diagnosis.place(relx=.55, rely=.40, anchor="w")

Assessment = ttk.Label(Consultn, text = 'ASSESSMENT: ', font = "Helvetica 12 bold", background = '#fff6a4')
Assessment.place(relx=.05, rely=.60, anchor="w")

Treat_Plan = ttk.Label(Consultn, text = 'TREATMENT PLAN: ', font = "Helvetica 12 bold", background = '#fff6a4')
Treat_Plan.place(relx=.55, rely=.60, anchor="w")

Consult_Fees = ttk.Label(Consultn, text = 'CONSULTATION FEES: ', font = "Helvetica 12 bold", background = '#fff6a4')
Consult_Fees.place(relx=.05, rely=.80, anchor="w")

  
# Entry Buttons
    
ConsultnID_EB = Entry(Consultn, width = 40, bd = 5, font = 'Helvetica 12 bold')
ConsultnID_EB.place(relx=.20, rely=.25, anchor="w")

AppointmentID_EB = Entry(Consultn, width = 40, bd = 5, font = 'Helvetica 12 bold')
AppointmentID_EB.place(relx=.70, rely=.25, anchor="w")

MedHistory_EB = Text(Consultn, width = 40, height = 3, bd = 5, font = 'Helvetica 12 bold')
MedHistory_EB.place(relx=.20, rely=.43, anchor="w")

Diagnosis_EB = Text(Consultn, width = 40, height = 3, bd = 5, font = 'Helvetica 12 bold')
Diagnosis_EB.place(relx=.70, rely=.43, anchor="w")

Assessment_EB = Text(Consultn, width = 40, height = 3, bd = 5, font = 'Helvetica 12 bold')
Assessment_EB.place(relx=.20, rely=.63, anchor="w")

TreatPlan_EB = Text(Consultn, width = 40, height = 3, bd = 5, font = 'Helvetica 12 bold')
TreatPlan_EB.place(relx=.70, rely=.63, anchor="w")

ConsultFees_EB = Entry(Consultn, width = 40, bd = 5, font = 'Helvetica 12 bold')
ConsultFees_EB.place(relx=.20, rely=.80, anchor="w")
 
# Create Buttons
enter_btn = Button(Consultn, text='ENTER RECORD', width=20, command=Enter)
enter_btn.place(relx=.10, rely=.90)

fetch_btn = Button(Consultn, text='FETCH RECORD', width=20, command=Fetch)
fetch_btn.place(relx=.70, rely=.90)

remove_btn = Button(Consultn, text='DELETES RECORD', width=20, command=Remove)
remove_btn.place(relx=.25, rely=.90)

update_btn = Button(Consultn, text='UPDATES RECORD', width=20, command=Update)
update_btn.place(relx=.40, rely=.90)

clear_btn = Button(Consultn, text='CLEAR RECORD', width=20, command=Clear)
clear_btn.place(relx=.55, rely=.90)

# Quit Button

quit_btn = Button(Consultn, text="Quit", width=8, command=Consultn.quit)
quit_btn.place(relx = .90, rely = .90)

# Start program

Consultn.mainloop()