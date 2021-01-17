# Patient Information System
# Dashboard for Image Lab
import tkinter as tk
import mysql
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import glob
from tkinter import filedialog
import base64
import cStringIO

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "alsy", database = "idigihealth_db")
mycursor = mydb.cursor()

#Appointment_top = tk.Toplevel(PIS)
ImageLab = tk.Tk()
ImageLab.title("Doctor Consultation")
ImageLab.iconbitmap('Lab.ico')
ImageLab.geometry('800x800')
#photo=PhotoImage(file='031Blessing.png')
#HmLab.configure(bg='#00b0c6')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('053SoftGrass.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(ImageLab, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

# Browse and show images

def show(event):
	n = ImgDisplayBox.curselection()
	fname = ImgDisplayBox.get(n)
	img = tk.PhotoImage(file = fname)
	lab.config(image = img)
	lab.image = img
	print(fname)
	return(fname)

def load_directory(path='F:\\PROJECT\\HealthInfo\\iDiGiHealth\\Dashboards\\Images'):
        """
        :param path: Provide Path of File Directory
        :return: List of image Names
        """
	for x in os.listdir(path):
    	image_name.append(x)
    	return image_name

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
    print(binaryData)


image_name[]
def Enter():

	image = Image.open('F:\\PROJECT\\HealthInfo\\iDiGiHealth\\Dashboards\\Images\\fmri.jpg')
	photo = open('F:\\PROJECT\\HealthInfo\\iDiGiHealth\\Dashboards\\Images\\fmri.jpg', 'rb').read()
	

    # Entering data into database table
    Img_ID=ImgLabID_EB.get()
    dbImg_ID=""
    Select="SELECT Imaging_Lab FROM imaging_lab WHERE Imaging_Lab='%s'" %(Img_ID)
    mycursor.execute(Select)
    result=mycursor.fetchall()

#   print(convertToBinaryData(photo))
 #   encodestring = base64.b64encode(photo)

    for i in result:
        dbImg_ID=i[0]
    if(Img_ID == dbImg_ID):
        messagebox.askokcancel("Information","Record already taken")
    else:
        Insert="INSERT INTO imaging_lab (Imaging_Lab, Consultation_ID, IMG_Test_Type, IMG_Test_Results, IMG_Test_Cost) values(%s,%s,%s,%s,%s)"
        Imaging_Lab = ImgLabID_EB.get()
        Consultation_ID = ConsultID_EB.get()
        IMG_Test_Type = ImgTestType_CB.get()
        IMG_Test_Results = photo
        IMG_Test_Cost = ImgCost_EB.get()
        
        if (Consultation_ID !="" and IMG_Test_Type !="" and IMG_Test_Cost !=""):
            Value=(Imaging_Lab, Consultation_ID, IMG_Test_Type, IMG_Test_Results, IMG_Test_Cost)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted successfully")
            ImgLabID_EB.delete(0, END)
            ConsultID_EB.delete(0, END)
            ImgTestType_CB.delete(0, END)
            TestResults_EB.delete(0, END)
            ImgCost_EB.delete(0, END)
            
        else:
            if (Consultation_ID =="" and IMG_Test_Type =="" and IMG_Test_Results =="" and IMG_Test_Cost ==""):
             messagebox.askokcancel("Information","New Patient - fill all details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")

def Fetch():
    if(ImgLabID_EB.get() == ""):
        messagebox.showinfo("Fetch status", "Imaging Lab ID is compulsory to fetch details")
    else:
        mycursor.execute("SELECT * FROM imaging_lab WHERE Imaging_Lab = '"+ ImgLabID_EB.get() +"'")
        rows = mycursor.fetchall()

        for row in rows:
            print("Image lab Id = ", row[0], )
            print("Consultation ID = ", row[1])
            print("Test type - ", row[2])
            image = row[2]
            print("Test cost - ", row[4])
            print("Storing image on disk \n")
            write_file(image, photo)
            

def Remove():
    Img_Lab = ImgLabID_EB.get() # Img_Lab_ID here is a variable
    Delete="DELETE FROM imaging_lab WHERE Imaging_Lab ='%s'" %(Img_Lab)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Record removed")
    ImgLabID_EB.delete(0, END)
    ConsultID_EB.delete(0, END)
    ImgTestType_CB.delete(0, END)
    ImgCost_EB.delete(0, END)
#    populate_list()

def Update():

    Imaging_Lab = ImgLabID_EB.get()
    Consultation_ID = ConsultID_EB.get()
    IMG_Test_Type = ImgTestType_CB.get()
    IMG_Test_Results = convertToBinaryData(photo)
    IMG_Test_Cost = ImgCost_EB.get()

    Update="UPDATE imaging_lab SET Consultation_ID='%s', IMG_Test_Type='%s', IMG_Test_Results='%s', IMG_Test_Cost='%s' WHERE Imaging_Lab='%s'" %(Consultation_ID, HM_Test_Type, HM_Test_Results, HM_Test_Cost, Haematology_Lab_ID)
    mycursor.execute(Update)
    mydb.commit()    
    messagebox.showinfo("Information","Record updated successfully")
#    populate_list()

def Clear():
    ImgLabID_EB.delete(0, END)
    ConsultID_EB.delete(0, END)
    ImgTestType_CB.delete(0, END)
    ImgCost_EB.delete(0, END)







# Title Frame and Label
Img_PIS = ttk.Label(ImageLab, text = "IMAGING LABORATORY", font = "Helvetica 20 bold", background = '#ffffff')
Img_PIS.place(relx=.50, rely=.03, anchor="n")

# Create Labels
ImageLab_ID =  ttk.Label(ImageLab, text = 'IMAGE LAB ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
ImageLab_ID.place(relx=.05, rely=.20, anchor="w")

Consulation_ID = ttk.Label(ImageLab, text = 'CONSULTATION ID: ', font = "Helvetica 12 bold", background = '#fff6a4')
Consulation_ID.place(relx=.50, rely=.20, anchor="w")

Img_Test_Type = ttk.Label(ImageLab, text = 'IMAGE TEST TYPE: ', font = "Helvetica 12 bold", background = '#fff6a4')
Img_Test_Type.place(relx=.05, rely=.30, anchor="w")

Img_Test_Cost = ttk.Label(ImageLab, text = 'IMAGE TEST COST: ', font = "Helvetica 12 bold", background = '#fff6a4')
Img_Test_Cost.place(relx=.50, rely=.30, anchor="w")

Image_Test_Results = ttk.Label(ImageLab, text = 'IMAGE RESULTS: ', font = "Helvetica 12 bold", background = '#fff6a4')
Image_Test_Results.place(relx=.05, rely=.40, anchor="w")

# Images List Box
Disp_label = tk.Label(ImageLab, text = 'IMAGE DISPLAY: ', font = "Helvetica 12 bold", background = '#fff6a4')
Disp_label.place(relx=.05, rely=.50, anchor="w")

ImgDisplayBox = Listbox(ImageLab)
ImgDisplayBox.place(relx=.20, rely=.65, anchor="w")
list_images = [i for i in glob.glob("*.jpg")]

for fname in list_images:
	ImgDisplayBox.insert(tk.END, fname)

ImgDisplayBox.bind("<<ListboxSelect>>", show)
img = tk.PhotoImage(file = "starlrg.png")
lab = tk.Label(ImageLab, image = img)
lab.place(relx=.50, rely=.65, anchor="w")

# Entry Buttons
    
# Create Entry Box
ImgLabID_EB = Entry(ImageLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
ImgLabID_EB.place(relx=.20, rely=.20, anchor="w")
ImgLabID_EB.focus()

ConsultID_EB = Entry(ImageLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
ConsultID_EB.place(relx=.65, rely=.20, anchor="w")

# create combobox
ImgTestType_CB = ttk.Combobox(ImageLab, width = 30, font = 'Helvetica 12 bold', state = 'readonly')
ImgTestType_CB['values'] = ('Microscopy', 'CT Scan', 'Ultrasound', 'MRI Scan', 'X-ray')
ImgTestType_CB.current(0)
ImgTestType_CB.place(relx=.20, rely=.30, anchor="w")

ImgCost_EB = Entry(ImageLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
ImgCost_EB.place(relx=.65, rely=.30, anchor="w")

TestResults_EB = Entry(ImageLab, width = 30, bd = 5, font = 'Helvetica 12 bold')
TestResults_EB.place(relx=.20, rely=.40, anchor="w")



# Buttons

#add_btn = Button(ImageLab, text="ADD", width=8)#, command = add)
#add_btn.place(relx = .90, rely = .33)

#rmventry_btn = Button(ImageLab, text="REMOVE", width=8)#, command = removentry)
#rmventry_btn.place(relx = .90, rely = .64)

Next_img = Button(ImageLab, text="NEXT IMAGE", width=17, default=ACTIVE, borderwidth=0)#, command=Read_image)
Next_img.place(relx=.50, rely=.85)

enter_btn = Button(ImageLab, text='ENTER RECORD', width=20)#, command=Enter)
enter_btn.place(relx=.10, rely=.90)

fetch_btn = Button(ImageLab, text='FETCH RECORD', width=20)#, command=Fetch)
fetch_btn.place(relx=.70, rely=.90)

remove_btn = Button(ImageLab, text='DELETES RECORD', width=20)#, command=Remove)
remove_btn.place(relx=.25, rely=.90)

update_btn = Button(ImageLab, text='UPDATES RECORD', width=20)#, command=Update)
update_btn.place(relx=.40, rely=.90)

clear_btn = Button(ImageLab, text='CLEAR RECORD', width=20)#, command=Clear)
clear_btn.place(relx=.55, rely=.90)

# ListBox

#Test_TypeRes_Listbox = Listbox(ImageLab, height=15, width=140, border=3)
#Test_TypeRes_Listbox.place(relx=.20, rely=.67, anchor="w")

# Create scrollbar
#scrollbar = Scrollbar(ImageLab)
#scrollbar.place(relx=.90, rely=.47, anchor="e")
# Set scroll to listbox
#Test_TypeRes_Listbox.configure(yscrollcommand=scrollbar.set)
#scrollbar.configure(command=Test_TypeRes_Listbox.yview)
# Bind select
#Test_TypeRes_Listbox.bind('<<ListboxSelect>>')#, select_TypeRes)

# Populate data
#populate_list()

# Quit Button
exit_btn = Button(ImageLab, text="EXIT", width=8, command=ImageLab.quit)
exit_btn.place(relx = .90, rely = .90)

# Start program
ImageLab.mainloop()

