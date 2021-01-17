# iDigiHealth - Patient Information System
# GUI for Haematology laboratory 
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
HmLab = tk.Tk()

HmLab.title("Haematology Laboratory")
HmLab.iconbitmap('Lab.ico')
HmLab.geometry('800x800')
#photo=PhotoImage(file='031Blessing.png')
#HmLab.configure(bg='#00b0c6')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('031Blessing.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(HmLab, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)



# Defining functions
#def populate_list():
#    Test_TypeRes_Listbox.delete(0, END)
#    for row in mycursor.fetchall():
#        Test_TypeRes_Listbox.insert(END, row)

def add():

    if TestType_CB.get() == '' or TestResults_EB.get() == '':
        messagebox.showerror('Error Message', 'Please include all fields')
        return
        
    Test_TypeRes_Listbox.insert(END, (TestType_CB.get(), TestResults_EB.get()))
    
def removentry():

    Test_TypeRes_Listbox.delete(0, END)
    
def select_TypeRes(event):
    try:
        global selected_item
        index = (Test_TypeRes_Listbox.curselection())#[0]
        selected_item = Test_TypeRes_Listbox.get(index)
        TestType_CB.delete(0, END)
        TestType_CB.insert(END, selected_item[1])
        TestResults_EB.delete(0, END)
        TestResults_EB.insert(END, selected_item[2])
    except IndexError:
        pass

TestRes_List = []
TestType_List = []

def Enter():

    # process Listobox entries
    TTL = Test_TypeRes_Listbox.get(0, END)
    for item in TTL:
        TestType_List.append(item[0])
        TestRes_List.append(item[1])
    #print(TestType_List)
    #print(TestRes_List)
    HMTestType = str(",".join(TestType_List)) # Converting list to string
    HMTestResults =  str(",".join(TestRes_List)) # Converting list to string
#    print(HMTestType)
#    print(HMTestResults)

    # Entering data into database table
    Hm_ID=HmLabID_EB.get()
    dbHm_ID=""
    Select="SELECT Haematology_Lab_ID FROM haematology_lab WHERE Haematology_Lab_ID='%s'" %(Hm_ID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbHm_ID=i[0]
    if(Hm_ID == dbHm_ID):
        messagebox.askokcancel("Information","Record already taken")
    else:
        Insert="INSERT INTO haematology_lab (Haematology_Lab_ID, Consultation_ID, HM_Test_Type, HM_Test_Results, HM_Test_Cost) values(%s,%s,%s,%s,%s)"
        Haematology_Lab_ID = HmLabID_EB.get()
        Consultation_ID = ConsultID_EB.get()
        HM_Test_Type = HMTestType
        HM_Test_Results = HMTestResults
        HM_Test_Cost = TotalCost_EB.get()
        print(Haematology_Lab_ID, Consultation_ID, HM_Test_Type, HM_Test_Results, HM_Test_Cost)

        if (Consultation_ID !="" and HM_Test_Cost !=""):
            Value=(Haematology_Lab_ID, Consultation_ID, HM_Test_Type, HM_Test_Results, HM_Test_Cost)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted successfully")
            HmLabID_EB.delete(0, END)
            ConsultID_EB.delete(0, END)
            Test_TypeRes_Listbox.delete(0, END)
            TotalCost_EB.delete(0, END)
            
        else:
            if (Consultation_ID =="" and HM_Test_Type =="" and HM_Test_Results =="" and HM_Test_Cost ==""):
             messagebox.askokcancel("Information","New Patient - fill all details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")

def Fetch():
    if(HmLabID_EB.get() == ""):
        messagebox.showinfo("Fetch status", "Haematology Lab ID is compulsory to fetch details")
    else:
        mycursor.execute("SELECT * FROM haematology_lab WHERE Haematology_Lab_ID = '"+ HmLabID_EB.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
            Test_TypeRes_Listbox.insert(0, END)
#            ConsultID_EB.insert(0, row[1])        
#            TestType_CB.insert(0, row[2])
#            TestResults_EB.insert(0, row[3])
#            TotalCost_EB.insert(0, row[4])
#        populate_list()

def Remove():
    Hm_ID=HmLabID_EB.get() # Hm_Lab_ID here is a variable
    Delete="DELETE FROM haematology_lab WHERE Haematology_Lab_ID ='%s'" %(Hm_ID)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Record removed")
    HmLabID_EB.delete(0, END)
    ConsultID_EB.delete(0, END)
    Test_TypeRes_Listbox.delete(0, END)
    TotalCost_EB.delete(0, END)
#    populate_list()

def Update():

    # process Listobox entries
    TTL = Test_TypeRes_Listbox.get(0, END)
    for item in TTL:
        TestType_List.append(item[0])
        TestRes_List.append(item[1])
    #print(TestType_List)
    #print(TestRes_List)
    HMTestType = str(",".join(TestType_List)) # Converting list to string
    HMTestResults =  str(",".join(TestRes_List)) # Converting list to string
    print(HMTestType)
    print(HMTestResults)

    Haematology_Lab_ID = HmLabID_EB.get()
    Consultation_ID = ConsultID_EB.get()
    HM_Test_Type = HMTestType
    HM_Test_Results = HMTestResults
    HM_Test_Cost = TotalCost_EB.get()

    Update="UPDATE haematology_lab SET Haematology_Lab_ID='%s' Consultation_ID='%s', HM_Test_Type='%s', HM_Test_Results='%s', HM_Test_Cost='%s'" %(Consultation_ID, HM_Test_Type, HM_Test_Results, HM_Test_Cost, Haematology_Lab_ID)
    mycursor.execute(Update)
    mydb.commit()    
    messagebox.showinfo("Information","Record updated successfully")
#    populate_list()

def Clear():
    HmLabID_EB.delete(0, END)   
    ConsultID_EB.delete(0, END)
    Test_TypeRes_Listbox.delete(0, END)
    TotalCost_EB.delete(0, END) 
    
# Labels

# Title Frame and Label
HmLab_Title = ttk.Label(HmLab, text = "HAEMATOLOGY LABORATORY", font = "Helvetica 30 bold", background = '#d1fdff', borderwidth = 5)
HmLab_Title.place(relx=.5, rely=.01, anchor="n")

# Patient Details
heading2_PIS = ttk.Label(HmLab, text = "Blood Test Details", font = "Helvetica 15 bold", background = '#d1fdff')
heading2_PIS.place(relx=.05, rely=.20, anchor="w")

# Create Labels
HmLab_ID =  ttk.Label(HmLab, text = 'HAEMATOLOGY LAB ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
HmLab_ID.place(relx=.05, rely=.30, anchor="w")

Consultation_ID = ttk.Label(HmLab, text = 'CONSULTATION ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
Consultation_ID.place(relx=.50, rely=.30, anchor="w")

Test_Type = ttk.Label(HmLab, text = 'TEST TYPE: ', font = "Helvetica 12 bold", background = '#fff6a4')
Test_Type.place(relx=.05, rely=.35, anchor="w")

Test_Results = ttk.Label(HmLab, text = 'TEST RESULTS: ', font = "Helvetica 12 bold", background = '#fff6a4')
Test_Results.place(relx=.50, rely=.35, anchor="w")

Total_Cost = ttk.Label(HmLab, text = 'TOTAL COST: ', font = "Helvetica 12 bold", background = '#fff6a4')
Total_Cost.place(relx=.05, rely=.65, anchor="w")

# Create Entry Boxes

# Create Entry Box
HmLabID_EB = Entry(HmLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
HmLabID_EB.place(relx=.25, rely=.30, anchor="w")
HmLabID_EB.focus()

ConsultID_EB = Entry(HmLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
ConsultID_EB.place(relx=.65, rely=.30, anchor="w")

# create combobox
TestType_CB = ttk.Combobox(HmLab, width = 30, font = 'Helvetica 12 bold', state = 'readonly')
TestType_CB['values'] = ('Hemoglobin', 'RBC_Count', 'WBC_Count', 'Granulocytes', 'Lymphocytes', 'Monocytes', 'Eosinophils', 'Basophils', 'Platelets')
TestType_CB.current(0)
TestType_CB.place(relx=.25, rely=.35, anchor="w")

TestResults_EB = Entry(HmLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
TestResults_EB.place(relx=.65, rely=.35, anchor="w")

TotalCost_EB = Entry(HmLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
TotalCost_EB.place(relx=.25, rely=.65, anchor="w")

# Buttons

add_btn = Button(HmLab, text="ADD", width=8, command = add)
add_btn.place(relx = .90, rely = .33)

rmventry_btn = Button(HmLab, text="REMOVE", width=8, command = removentry)
rmventry_btn.place(relx = .90, rely = .64)

enter_btn = Button(HmLab, text='ENTER RECORD', width=20, command=Enter)
enter_btn.place(relx=.10, rely=.85)

fetch_btn = Button(HmLab, text='FETCH RECORD', width=20, command=Fetch)
fetch_btn.place(relx=.70, rely=.85)

remove_btn = Button(HmLab, text='DELETES RECORD', width=20, command=Remove)
remove_btn.place(relx=.25, rely=.85)

update_btn = Button(HmLab, text='UPDATES RECORD', width=20, command=Update)
update_btn.place(relx=.40, rely=.85)

clear_btn = Button(HmLab, text='CLEAR RECORD', width=20, command=Clear)
clear_btn.place(relx=.55, rely=.85)

# ListBox

Test_TypeRes_Listbox = Listbox(HmLab, height=10, width=45, border=3)
Test_TypeRes_Listbox.place(relx=.65, rely=.55, anchor="w")

# Create scrollbar
scrollbar = Scrollbar(HmLab)
scrollbar.place(relx=.90, rely=.47, anchor="e")
# Set scroll to listbox
Test_TypeRes_Listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=Test_TypeRes_Listbox.yview)
# Bind select
Test_TypeRes_Listbox.bind('<<ListboxSelect>>', select_TypeRes)

# Populate data
#populate_list()

# Quit Button
exit_btn = Button(HmLab, text="EXIT", width=8, command=HmLab.quit)
exit_btn.place(relx = .90, rely = .90)

# Start program
HmLab.mainloop()