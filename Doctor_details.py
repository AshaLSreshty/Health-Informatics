# iDigiHealth - Patient Information System
# Dashboard for entering Doctor details 
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
DocDetails = tk.Tk()

DocDetails.title("Doctor Details")
DocDetails.iconbitmap('doc.ico')
DocDetails.geometry('800x800')
    
# Appointment_top.configure(bg='#00b0c6')

# Background Image
doc_bg_image = ImageTk.PhotoImage(Image.open('RegPic2.jpg'))
doc_bg_label = Label(DocDetails, image = doc_bg_image)
doc_bg_label.place(relwidth = 1, relheight = 1)
doc_bg_label.image = doc_bg_image

# Defining functions

def Enter():
    Doc_ID=DoctorID_EB.get()
    dbDoc_ID=""
    Select="select Doctor_ID from doctor_details where Doctor_ID='%s'" %(Doc_ID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbDoc_ID=i[0]
    if(Doc_ID == dbDoc_ID):
        messagebox.askokcancel("Information","Record already taken")
    else:
        Insert="Insert into doctor_details (Doctor_ID, Doctor_name, Specialization) values(%s,%s,%s)"
        Doc_ID = DoctorID_EB.get()
        Docname = Doctor_name_EB.get()
        Docspl = DocSpecialization_EB.get()
       
        if (Docname !="" and Docspl !=""):
            Value=(Doc_ID, Docname, Docspl)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted successfully")
            DoctorID_EB.delete(0, END)
            Doctor_name_EB.delete(0, END)
            DocSpecialization_EB.delete(0, END)
            
        else:
            if (Doctor_name =="" and Specialization ==""):
             messagebox.askokcancel("Information","New Doctor - fill all details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")
#        populate_list()

def Fetch():
    if(DoctorID_EB.get() == ""):
        messagebox.showinfo("Fetch status", "Doctor ID is compulsory to fetch details")
    else:
        mycursor.execute("select * from doctor_details where Doctor_ID = '"+ DoctorID_EB.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
#           patientID_entrybox.insert(0, row[0])        
            Doctor_name_EB.insert(0, row[1])        
            DocSpecialization_EB.insert(0, row[2])      
            
#        populate_list()

def Remove():
    Doc_ID=DoctorID_EB.get() # Appointment_ID here is a variable
    Delete="delete from doctor_details where Doctor_ID='%s'" %(Doc_ID)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Doctor details record removed")
    DoctorID_EB.delete(0, END)   
    Doctor_name_EB.delete(0, END)
    DocSpecialization_EB.delete(0, END)   
        
#    populate_list()

def Update():
    Doc_ID = DoctorID_EB.get()
    Docname = Doctor_name_EB.get()
    Docspl = DocSpecialization_EB.get()
    Update="Update doctor_details set Doctor_name='%s', Specialization='%s', Doctor_ID='%s'" %(Docname, Docspl, Doc_ID)
    mycursor.execute(Update)
    mydb.commit()
 #   populate_list()
    messagebox.showinfo("Information","Record updated successfully")

def Clear():
    DoctorID_EB.delete(0, END)   
    Doctor_name_EB.delete(0, END)   
    DocSpecialization_EB.delete(0, END) 
    

# Title Frame and Label
doc_PIS = ttk.Label(DocDetails, text = "DOCTOR DETAILS", font = "Helvetica 20 bold", background = '#ffffff')
doc_PIS.place(relx=.50, rely=.03, anchor="n")

# Labels

DoctorID = ttk.Label(DocDetails, text = 'DOCTOR ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
DoctorID.place(relx=.05, rely=.35, anchor="w")

Doctor_name = ttk.Label(DocDetails, text = 'DOCTOR NAME: ', font = "Helvetica 12 bold", background = '#fff6a4')
Doctor_name.place(relx=.50, rely=.35, anchor="w")

DocSpecialization =  ttk.Label(DocDetails, text = 'SPECIALIZATION: ', font = "Helvetica 12 bold", background = '#fff6a4')
DocSpecialization.place(relx=.05, rely=.60, anchor="w")

   
# Entry Buttons
    
DoctorID_EB = Entry(DocDetails, width = 40, bd = 5, font = 'Helvetica 12 bold')
DoctorID_EB.place(relx=.20, rely=.35, anchor="w")

Doctor_name_EB = Entry(DocDetails, width = 40, bd = 5, font = 'Helvetica 12 bold')
Doctor_name_EB.place(relx=.70, rely=.35, anchor="w")

DocSpecialization_EB = Entry(DocDetails, width = 40, bd = 5, font = 'Helvetica 12 bold')
DocSpecialization_EB.place(relx=.20, rely=.60, anchor="w")

 
# Create Buttons
enter_btn = Button(DocDetails, text='ENTER RECORD', width=20, command=Enter)
enter_btn.place(relx=.10, rely=.85)

fetch_btn = Button(DocDetails, text='FETCH RECORD', width=20, command=Fetch)
fetch_btn.place(relx=.70, rely=.85)

remove_btn = Button(DocDetails, text='DELETES RECORD', width=20, command=Remove)
remove_btn.place(relx=.25, rely=.85)

update_btn = Button(DocDetails, text='UPDATES RECORD', width=20, command=Update)
update_btn.place(relx=.40, rely=.85)

clear_btn = Button(DocDetails, text='CLEAR RECORD', width=20, command=Clear)
clear_btn.place(relx=.55, rely=.85)

# Quit Button

quit_btn = Button(DocDetails, text="Quit", width=8, command=DocDetails.quit)
quit_btn.place(relx = .90, rely = .90)

# Start program

DocDetails.mainloop()