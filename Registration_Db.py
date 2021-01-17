# Patient Information System
# Registration of Patient and Appointment fixing dashboard
# Developed using Python and Tkinter
# Author - Dr. Ashalatha Sreshty Mamidi

import tkinter as tk
import mysql
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import __main__


mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "alsy", database = "idigihealth_db")
mycursor = mydb.cursor()

# Defining functions

#def populate_list():
#	patients_list.delete(0, END)
#	for row in mycursor.fetch():
#		patients_list.insert(END, row)

def select_record(event):
    try:
        global selected_item
        index = patients_list.curselection()[0]
        selected_item = patients_list.get(index)

        patientID_entrybox.delete(0, END)
        patientID_entrybox.insert(END, selected_item[1])
        firstname_entrybox.delete(0, END)
        firstname_entrybox.insert(END, selected_item[2])
        surname_entrybox.delete(0, END)
        surname_entrybox.insert(END, selected_item[3])
        age_entrybox.delete(0, END)
        age_entrybox.insert(END, selected_item[4])
        dob_entrybox.delete(0, END)
        dob_entrybox.insert(END, selected_item[5])
        gender_combobox.delete(0, END)
        gender_combobox.insert(END, selected_item[6])
        pin_entrybox.delete(0, END)
        pin_entrybox.insert(END, selected_item[7])
        mobile_entrybox.delete(0, END)
        mobile_entrybox.insert(END, selected_item[8])
        email_entrybox.delete(0, END)
        email_entrybox.insert(END, selected_item[9])
        address_entrybox.delete(0, END)
        address_entrybox.insert(END, selected_item[10])
        district_entrybox.delete(0, END)
        district_entrybox.insert(END, selected_item[11])
        state_entrybox.delete(0, END)
        state_entrybox.insert(END, selected_item[12])
        ethnicity_entrybox.delete(0, END)
        ethnicity_entrybox.insert(END, selected_item[13])
        pincode_entrybox.delete(0, END)
        pincode_entrybox.insert(END, selected_item[14])
    except IndexError:
        pass

def Register():
    Patient_ID=patientID_entrybox.get()
    dbPatient_ID=""
    Select="select Patient_ID from patient_details where Patient_ID='%s'" %(Patient_ID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbPatient_ID=i[0]
    if(Patient_ID == dbPatient_ID):
        messagebox.askokcancel("Information","Record Already exists")
    else:
        Insert="Insert into patient_details(Patient_ID, First_name, Surname, Age, Date_of_Birth, Gender, Personal_Indentity_Proof, Mobile, Email, Address, District, State, Ethnicity, Pincode) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        Patient_ID = patientID_entrybox.get()
        First_name = firstname_entrybox.get()
        Surname = surname_entrybox.get()
        Age = age_entrybox.get()
        Date_of_Birth = dob_entrybox.get()
        Gender = gender_combobox.get()
        Personal_Indentity_Proof = pin_entrybox.get()
        Mobile = mobile_entrybox.get()
        Email = email_entrybox.get()
        Address = address_entrybox.get()
        District = district_entrybox.get()
        State = state_entrybox.get()
        Ethnicity = ethnicity_entrybox.get()
        Pincode = pincode_entrybox.get()

        if (First_name !="" and Surname !="" and Age !="" and Date_of_Birth !="" and Gender !="" and Personal_Indentity_Proof !="" and Mobile !="" and Email !="" and Address !="" and District !="" and State !="" and Ethnicity !="" and Pincode !=""):
            Value=(Patient_ID, First_name, Surname, Age, Date_of_Birth, Gender, Personal_Indentity_Proof, Mobile, Email, Address, District, State, Ethnicity, Pincode)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted Successfully")
            patientID_entrybox.delete(0, END)
            firstname_entrybox.delete(0, END)
            surname_entrybox.delete(0, END)
            age_entrybox.delete(0, END)
            dob_entrybox.delete(0, END)
            gender_combobox.delete(0, END)
            pin_entrybox.delete(0, END)
            mobile_entrybox.delete(0, END)
            email_entrybox.delete(0, END)
            address_entrybox.delete(0, END)
            district_entrybox.delete(0, END)
            state_entrybox.delete(0, END)
            ethnicity_entrybox.delete(0, END)
            pincode_entrybox.delete(0, END)
        else:
            if (First_name =="" and Surname =="" and Age =="" and Date_of_Birth =="" and Gender =="" and Personal_Indentity_Proof =="" and Mobile =="" and Email =="" and Address =="" and District =="" and State =="" and Ethnicity =="" and Pincode ==""):
             messagebox.askokcancel("Information","New Entry Fill All Details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")
#        populate_list()

def Fetchrecord():
    if(patientID_entrybox.get() == ""):
        messagebox.showinfo("Fetch status", "Patient ID is compulsory to fetch record")
    else:
        mycursor.execute("select * from patient_details where Patient_ID = '"+ patientID_entrybox.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
#           patientID_entrybox.insert(0, row[0])        
            firstname_entrybox.insert(0, row[1])        
            surname_entrybox.insert(0, row[2])      
            age_entrybox.insert(0, row[3])      
            dob_entrybox.insert(0, row[4])      
            gender_combobox.insert(0, row[5])       
            pin_entrybox.insert(0, row[6])      
            mobile_entrybox.insert(0, row[7])       
            email_entrybox.insert(0, row[8])        
            address_entrybox.insert(0, row[9])      
            district_entrybox.insert(0, row[10])        
            state_entrybox.insert(0, row[11])       
            ethnicity_entrybox.insert(0, row[12])       
            pincode_entrybox.insert(0, row[13])
#        populate_list()

def Delete():
    Patient_ID=patientID_entrybox.get()
    Delete="delete from patient_details where Patient_ID='%s'" %(Patient_ID)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Record Deleted")
    patientID_entrybox.delete(0, END)   
    firstname_entrybox.delete(0, END)   
    surname_entrybox.delete(0, END) 
    age_entrybox.delete(0, END)
    dob_entrybox.delete(0, END) 
    gender_combobox.delete(0, END)  
    pin_entrybox.delete(0, END) 
    mobile_entrybox.delete(0, END)  
    email_entrybox.delete(0, END)   
    address_entrybox.delete(0, END) 
    district_entrybox.delete(0, END)    
    state_entrybox.delete(0, END)   
    ethnicity_entrybox.delete(0, END)   
    pincode_entrybox.delete(0, END)
#    populate_list()

def Update():
    Patient_ID = patientID_entrybox.get()
    First_name = firstname_entrybox.get()
    Surname = surname_entrybox.get()
    Age = age_entrybox.get()
    Date_of_Birth = dob_entrybox.get()
    Gender = gender_combobox.get()
    Personal_Indentity_Proof = pin_entrybox.get()
    Mobile = mobile_entrybox.get()
    Email = email_entrybox.get()
    Address = address_entrybox.get()
    District = district_entrybox.get()
    State = state_entrybox.get()
    Ethnicity = ethnicity_entrybox.get()
    Pincode = pincode_entrybox.get()
    Update="Update patient_details set First_name='%s', Surname='%s', Age='%s', Date_of_Birth='%s', Gender='%s', Personal_Indentity_Proof='%s', Mobile='%s', Email='%s', Address='%s', District='%s', State='%s', Ethnicity ='%s', Pincode ='%s' where Patient_ID='%s'" %(First_name, Surname, Age, Date_of_Birth, Gender, Personal_Indentity_Proof, Mobile, Email, Address, District, State, Ethnicity, Pincode, Patient_ID)
    mycursor.execute(Update)
    mydb.commit()
 #   populate_list()
    messagebox.showinfo("Information","Record Update Successfully")

def Clear():
    patientID_entrybox.delete(0, END)   
    firstname_entrybox.delete(0, END)   
    surname_entrybox.delete(0, END) 
    age_entrybox.delete(0, END)
    dob_entrybox.delete(0, END) 
    gender_combobox.delete(0, END)  
    pin_entrybox.delete(0, END) 
    mobile_entrybox.delete(0, END)  
    email_entrybox.delete(0, END)   
    address_entrybox.delete(0, END) 
    district_entrybox.delete(0, END)    
    state_entrybox.delete(0, END)   
    ethnicity_entrybox.delete(0, END)   
    pincode_entrybox.delete(0, END)

# Create window object
PIS = tk.Tk()
PIS.title('iDigiHealth - Patient Information System')
PIS.iconbitmap('Hosp1.ico')
PIS.geometry('800x800')
PIS.configure(bg='#00b0c6')

# Background Image
background_image = ImageTk.PhotoImage(Image.open('RegPic3.jpg'))
background_label = Label(PIS, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# Title Frame and Label
heading_PIS = ttk.Label(PIS, text = "iDigiHealth - Patient Care System", font = "Helvetica 30 bold", background = '#00b0c6')
heading_PIS.place(relx=.5, rely=.01, anchor="n")

# Sub-Title
heading2_PIS = ttk.Label(PIS, text = "Patient Information System", font = "Helvetica 20 bold", background = '#00b0c6')
heading2_PIS.place(relx=.5, rely=.1, anchor="n")

# Patient Details
heading2_PIS = ttk.Label(PIS, text = "Patient Details", font = "Helvetica 15 bold", background = '#ff4d4d')
heading2_PIS.place(relx=.05, rely=.2, anchor="w")

# Create Labels
PatientID =  ttk.Label(PIS, text = 'PATIENT ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
PatientID.place(relx=.05, rely=.30, anchor="w")

First_name = ttk.Label(PIS, text = 'FIRST NAME: ', font = "Helvetica 12 bold", background = '#fff6a4')
First_name.place(relx=.05, rely=.35, anchor="w")

Surname = ttk.Label(PIS, text = 'SURNAME: ', font = "Helvetica 12 bold", background = '#fff6a4')
Surname.place(relx=.50, rely=.35, anchor="w")

Age = ttk.Label(PIS, text = 'AGE: ', font = "Helvetica 12 bold", background = '#fff6a4')
Age.place(relx=.05, rely=.40, anchor="w")

Date_of_Birth = ttk.Label(PIS, text = 'DATE OF BIRTH: ', font = "Helvetica 12 bold", background = '#fff6a4')
Date_of_Birth.place(relx=.50, rely=.40, anchor="w")

Gender = ttk.Label(PIS, text = 'GENDER: ', font = "Helvetica 12 bold", background = '#fff6a4')
Gender.place(relx=.05, rely=.45, anchor="w")

Personal_Indentity_Proof = ttk.Label(PIS, text = 'PERSONAL IDENTITY PROOF: ', font = "Helvetica 12 bold", background = '#fff6a4')
Personal_Indentity_Proof.place(relx=.50, rely=.45, anchor="w")

Mobile = ttk.Label(PIS, text = 'MOBILE NUMBER: ', font = "Helvetica 12 bold", background = '#fff6a4')
Mobile.place(relx=.05, rely=.50, anchor="w")

Email = ttk.Label(PIS, text = 'EMAIL: ', font = "Helvetica 12 bold", background = '#fff6a4')
Email.place(relx=.50, rely=.50, anchor="w")

ContactDetails =  ttk.Label(PIS, text = 'CONTACT DETAILS: ', font = "Helvetica 12 bold", background = '#fff6a4')
ContactDetails.place(relx=.05, rely=.55, anchor="w")

Address = ttk.Label(PIS, text = 'ADDRESS: ', font = "Helvetica 12 bold", background = '#fff6a4')
Address.place(relx=.05, rely=.60, anchor="w")

District = ttk.Label(PIS, text = 'DISTRICT: ', font = "Helvetica 12 bold", background = '#fff6a4')
District.place(relx=.50, rely=.60, anchor="w")

State = ttk.Label(PIS, text = 'STATE: ', font = "Helvetica 12 bold", background = '#fff6a4')
State.place(relx=.05, rely=.65, anchor="w")

Ethnicity = ttk.Label(PIS, text = 'Ethnicity: ', font = "Helvetica 12 bold", background = '#fff6a4')
Ethnicity.place(relx=.50, rely=.65, anchor="w")

Pincode = ttk.Label(PIS, text = 'PINCODE: ', font = "Helvetica 12 bold", background = '#fff6a4')
Pincode.place(relx=.05, rely=.70, anchor="w")

# Create Entry Box
patientID_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
patientID_entrybox.place(relx=.20, rely=.30, anchor="w")
patientID_entrybox.focus()

firstname_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
firstname_entrybox.place(relx=.20, rely=.35, anchor="w")

surname_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
surname_entrybox.place(relx=.70, rely=.35, anchor="w")

age_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
age_entrybox.place(relx=.20, rely=.40, anchor="w")

dob_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
dob_entrybox.place(relx=.70, rely=.40, anchor="w")

# create combobox
gender_combobox = ttk.Combobox(PIS, width = 20, font = 'Helvetica 12 bold')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.place(relx=.20, rely=.45, anchor="w")

# Create Entry Box
pin_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
pin_entrybox.place(relx=.70, rely=.45, anchor="w")

mobile_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
mobile_entrybox.place(relx=.20, rely=.50, anchor="w")

email_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
email_entrybox.place(relx=.70, rely=.50, anchor="w")

address_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
address_entrybox.place(relx=.20, rely=.60, anchor="w")

district_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
district_entrybox.place(relx=.70, rely=.60, anchor="w")

state_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
state_entrybox.place(relx=.20, rely=.65, anchor="w")

ethnicity_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
ethnicity_entrybox.place(relx=.70, rely=.65, anchor="w")

pincode_entrybox = Entry(PIS, width = 40, bd = 5, font = 'Helvetica 12 bold')
pincode_entrybox.place(relx=.20, rely=.70, anchor="w")

# Create Buttons
add_btn = Button(PIS, text='ADD RECORD', width=15, command=Register)
add_btn.place(relx=.10, rely=.75)

remove_btn = Button(PIS, text='DELETES RECORD', width=15, command=Delete)
remove_btn.place(relx=.30, rely=.75)

update_btn = Button(PIS, text='UPDATES RECORD', width=15, command=Update)
update_btn.place(relx=.50, rely=.75)

clear_btn = Button(PIS, text='CLEAR RECORDS', width=15, command=Clear)
clear_btn.place(relx=.70, rely=.75)

fetch_btn = Button(PIS, text='FETCH RECORDS', width=15, command=Fetchrecord)
fetch_btn.place(relx=.90, rely=.75)

# Appointment window
#appointment_btn = Button(PIS, text = 'Take an Appointment', width=20, command=popup_Appointment)
#appointment_btn.place(relx=.40, rely=.90)

# Quit Button
quit_btn = Button(PIS, text="Quit", width=8, command=PIS.quit)
quit_btn.place(relx = .90, rely = .90)

# Start program
PIS.mainloop()