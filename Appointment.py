# Patient Information System
# Dashboard for Appointment fixing of Patient 
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
Appointment_top = tk.Tk()

Appointment_top.title("Fix an Appointment")
Appointment_top.iconbitmap('app1.ico')
Appointment_top.geometry('800x800')
    
#    Appointment_top.configure(bg='#00b0c6')

# Background Image
app_bg_image = ImageTk.PhotoImage(Image.open('AppPic.jpg'))
app_bg_label = Label(Appointment_top, image = app_bg_image)
app_bg_label.place(relwidth = 1, relheight = 1)
app_bg_label.image = app_bg_image

# Defining functions

def FixApp():
    App_ID=AppointmentID_App_EB.get()
    dbAppointment_ID=""
    Select="select Appointment_ID from appointment where Appointment_ID='%s'" %(App_ID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbAppointment_ID=i[0]
    if(App_ID == dbAppointment_ID):
        messagebox.askokcancel("Information","Appointment already taken")
    else:
        Insert="Insert into appointment (Appointment_ID, Date, Patient_ID, Doctor_ID) values(%s,%s,%s,%s)"
        Appointment_ID = AppointmentID_App_EB.get()
        Date = Date_App_EB.get()
        Patient_ID = PatientID_App_EB.get()
        Doctor_ID = DoctorID_App_EB.get()

        if (Date !="" and Patient_ID !="" and Doctor_ID !=""):
            Value=(Appointment_ID, Date, Patient_ID, Doctor_ID)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Appointment fixed successfully")
            AppointmentID_App_EB.delete(0, END)
            Date_App_EB.delete(0, END)
            PatientID_App_EB.delete(0, END)
            DoctorID_App_EB.delete(0, END)
        else:
            if (Date =="" and Patient_ID =="" and Doctor_ID ==""):
             messagebox.askokcancel("Information","New appointment fill all details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")
#        populate_list()

def FetApp():
    if(AppointmentID_App_EB.get() == ""):
        messagebox.showinfo("Fetch status", "Appointment ID is compulsory to fetch details")
    else:
        mycursor.execute("select * from appointment where Appointment_ID = '"+ AppointmentID_App_EB.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
#           patientID_entrybox.insert(0, row[0])        
            Date_App_EB.insert(0, row[1])        
            PatientID_App_EB.insert(0, row[2])      
            DoctorID_App_EB.insert(0, row[3])      
 
#        populate_list()

def DelApp():
    App_ID = AppointmentID_App_EB.get() # Appointment_ID here is a variable
    Delete="delete from appointment where Appointment_ID='%s'" %(App_ID)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Appointment record deleted")
    AppointmentID_App_EB.delete(0, END)   
    Date_App_EB.delete(0, END)
    PatientID_App_EB.delete(0, END)   
    DoctorID_App_EB.delete(0, END)
    
    
#    populate_list()

def UpdApp():
    App_ID = AppointmentID_App_EB.get()
    Date = Date_App_EB.get()
    Pat_ID = PatientID_App_EB.get()
    Doc_ID = DoctorID_App_EB.get()
    Update="Update appointment set Appointment_ID='%s', Date='%s', Patient_ID='%s', Doctor_ID='%s'" %(App_ID, Date, Pat_ID, Doc_ID)
    mycursor.execute(Update)
    mydb.commit()
 #   populate_list()
    messagebox.showinfo("Information","Record Updated successfully")

def ClrApp():
    AppointmentID_App_EB.delete(0, END)   
    Date_App_EB.delete(0, END)   
    PatientID_App_EB.delete(0, END) 
    DoctorID_App_EB.delete(0, END)
    

# Title Frame and Label
app_PIS = ttk.Label(Appointment_top, text = "SCHEDULE APPOINTMENT", font = "Helvetica 20 bold", background = '#ffffff')
app_PIS.place(relx=.50, rely=.03, anchor="n")

# Labels

AppointmentID_App = ttk.Label(Appointment_top, text = 'APPOINTMENT ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
AppointmentID_App.place(relx=.05, rely=.35, anchor="w")

Date_APP = ttk.Label(Appointment_top, text = 'DATE: ', font = "Helvetica 12 bold", background = '#fff6a4')
Date_APP.place(relx=.50, rely=.35, anchor="w")

PatientID_App =  ttk.Label(Appointment_top, text = 'PATIENT ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
PatientID_App.place(relx=.05, rely=.60, anchor="w")

DoctorID_App =  ttk.Label(Appointment_top, text = 'DOCTOR ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
DoctorID_App.place(relx=.50, rely=.60, anchor="w")

    
# Entry Buttons
    
AppointmentID_App_EB = Entry(Appointment_top, width = 40, bd = 5, font = 'Helvetica 12 bold')
AppointmentID_App_EB.place(relx=.20, rely=.35, anchor="w")

Date_App_EB = Entry(Appointment_top, width = 40, bd = 5, font = 'Helvetica 12 bold')
Date_App_EB.place(relx=.70, rely=.35, anchor="w")

PatientID_App_EB = Entry(Appointment_top, width = 40, bd = 5, font = 'Helvetica 12 bold')
PatientID_App_EB.place(relx=.20, rely=.60, anchor="w")

DoctorID_App_EB = Entry(Appointment_top, width = 40, bd = 5, font = 'Helvetica 12 bold')
DoctorID_App_EB.place(relx=.70, rely=.60, anchor="w")

    
# Create Buttons
fixApp_btn = Button(Appointment_top, text='FIX APPOINTMENT', width=20, command=FixApp)
fixApp_btn.place(relx=.10, rely=.85)

delApp_btn = Button(Appointment_top, text='DELETES APPOINTMENT', width=20, command=DelApp)
delApp_btn.place(relx=.25, rely=.85)

updApp_btn = Button(Appointment_top, text='UPDATES APPOINTMENT', width=20, command=UpdApp)
updApp_btn.place(relx=.40, rely=.85)

clrApp_btn = Button(Appointment_top, text='CLEAR APPOINTMENT', width=20, command=ClrApp)
clrApp_btn.place(relx=.55, rely=.85)

fetApp_btn = Button(Appointment_top, text='FETCH APPOINTMENT', width=20, command=FetApp)
fetApp_btn.place(relx=.70, rely=.85)

# Quit Button

quit_btn = Button(Appointment_top, text="Quit", width=8, command=Appointment_top.quit)
quit_btn.place(relx = .90, rely = .90)

# Start program

Appointment_top.mainloop()