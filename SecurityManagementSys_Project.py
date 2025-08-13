import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import pymysql
import time
import pandas as pd
import re


import tkinter as tk
from tkinter import messagebox

def ID_exception_dialog():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create an exception dialog box
    messagebox.showerror("ID Exception", "Invalid ID. Please enter a valid numeric ID.")


def validate_id(input_id):
    # Check if the input ID is numeric
    if input_id.isdigit():
        return True
    else:
        return False








# import tkinter as tk
# from tkinter import messagebox

def Email_exception_dialog():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create an exception dialog box
    messagebox.showerror("Email Exception", "Invalid email address. Please enter a valid email.")

# Example usage
#Email_exception_dialog()


import re

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
    
    
    
#import re

def validate_mobile_number(mobile_number):
    """
    Validates a mobile number.

    Parameters:
        mobile_number (str): The mobile number to be validated.

    Returns:
        bool: True if the mobile number is valid, False otherwise.
    """
    # Regular expression for a typical 10-digit mobile number
    pattern = r'^[6-9]\d{9}$'
    
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Check if the mobile number matches the pattern
    if re.match(regex, mobile_number):
        return True
    else:
        return False


    
    
def Mobile_exception_dialog():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create an exception dialog box
    messagebox.showerror("Moble Number Exception", "Invalid mobile number. Please enter a valid 10-digit mobile number starting with 6, 7, 8, or 9.")
     
    
    
    
    
    
    
    
    
    
    
    
    
    

# Example usage
#email = input("Enter your email address: ")

####################################################################

def adddetails():
    def submitadd():
        flag = True
        global con,mycursor
        id = idval.get()
        if validate_id(id):
            print("Enter valid ID")
        else:
            flag = False
            ID_exception_dialog()
        name = nameval.get()
        mobile = mobileval.get()
        if validate_mobile_number(mobile):
            print("Valid mobile number!")
        else:
            flag = False
            Mobile_exception_dialog()
        email = emailval.get()
        if validate_email(email):
            print("Valid email address!")
        else:
            flag = False
            #print("Invalid email address. Please enter a valid email.")
            Email_exception_dialog()
        address = addressval.get()
        gender = genderval.get()
        role = roleval.get()
        """date = dateval.get()
        time = timeval.get()"""
        added_date = time.strftime("%d/%m/%Y")
        added_time = time.strftime("%H:%M:%S")
        host = "localhost"
        user = "root"
        password = "root"
        database = "securitymanagementsystem1"
        if flag:
            try:
                        strr = "insert into detailstable values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        con = pymysql.connect(host=host,user=user,password=password,database=database)
                        mycursor = con.cursor()
                        mycursor.execute(strr,(id,name,mobile,email,address,gender,role,added_date,added_time))
                        con.commit()
                        res = messagebox.askyesnocancel("Notification","ID {} Name {} Added Successfully... Do you want to clean the form".format(id,name),parent=addroot)
                        if(res==True):
                                idval.set('')
                                nameval.set('')
                                mobileval.set('')
                                emailval.set('')
                                addressval.set('')
                                genderval.set('')
                                roleval.set('')
                                dateval.set('')
                                timeval.set('')
                
            except:
                messagebox.showerror("Notifications","Please enter correct details",parent=addroot)
        strr ="select * from detailstable" 
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        detailstable.delete(*detailstable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            detailstable.insert("",END,values=vv)
            
        

            
            
    #print("Details Added")
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry("470x470+220+200")
    addroot.title("Security Management System")
    addroot.config(bg="seashell4")
    #addroot.iconbitmap("logo.png.ico")
    addroot.resizable(False,False)
    
#-----------------------------------------------------------Add Student Labels
    idlabel = Label(addroot,text="Enter ID: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    idlabel.place(x=10,y=10)
    
    namelabel = Label(addroot,text="Enter Name: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    namelabel.place(x=10,y=70)
    
    mobilelabel = Label(addroot,text="Enter Mobile: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(addroot,text="Enter Email: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    emaillabel.place(x=10,y=190)
    
    addresslabel = Label(addroot,text="Enter Address: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    addresslabel.place(x=10,y=250)
    
    genderlabel = Label(addroot,text="Enter Gender: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    genderlabel.place(x=10,y=310)
    
    rolelabel = Label(addroot,text="Enter Role: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    rolelabel.place(x=10,y=370)
    
    """datelabel = Label(addroot,text="Enter Date: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    datelabel.place(x=10,y=430)
    
    timelabel = Label(addroot,text="Enter Time: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    timelabel.place(x=10,y=490)"""
    
    
    #########-----------------------------------------------------------------------add button
    submitbtn = Button(addroot,text="SUBMIT",font=("Constantia",17,"bold"),width=10,bd=5,activebackground="darkslategrey",activeforeground="gainsboro",command=submitadd)
    
    submitbtn.place(x=150,y=420)
    ##------------------------------------------------------------------------------------------Add Person entry
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    roleval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    
    
    identry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    roleentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=roleval)
    roleentry.place(x=250,y=370)
    
    """dateentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    timeeentry = Entry(addroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=timeval)
    timeeentry.place(x=250,y=490)
    """
    
    
    
    addroot.mainloop()
 ##################################################################################################################   
"""def searchdetails():
    print("Details Searched")"""
    
def searchdetails():
    def search():
        global con,mycursor
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        role = roleval.get()
        """date = dateval.get()
        time = timeval.get()"""
        #added_date = time.strftime("%d/%m/%Y")
        added_date = dateval.get()
        
        host = "localhost"
        user = "root"
        password = "root"
        database = "securitymanagementsystem1"
        
        con = pymysql.connect(host=host,user=user,password=password,database=database)
        mycursor = con.cursor()
        
        if(id != ""):
            strr = "select * from detailstable where id=%s"

            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)
            
            
        elif(name != ""):
            strr = "select * from detailstable where name=%s"
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                 vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                 detailstable.insert("",END,values=vv)
            
        
        elif(mobile != ""):
            strr = "select * from detailstable where mobile=%s"
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)
            
            
         
        elif(email != ""):
            strr = "select * from detailstable where email=%s"
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)

               
         
        elif(address != ""):
            strr = "select * from detailstable where address=%s"
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)
            
            
         
        elif(gender != ""):
            strr = "select * from detailstable where gender=%s"
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)
            
            
            
        elif(role != ""):
            strr = "select * from detailstable where role=%s"
            mycursor.execute(strr,(role))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)
            
            
            
        elif(added_date != ""):
            strr = "select * from detailstable where date=%s"
            print(added_date)
            mycursor.execute(strr,(added_date))
            datas = mycursor.fetchall()
            detailstable.delete(*detailstable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                detailstable.insert("",END,values=vv)
               
            
    #print("Details Added")
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry("470x540+220+200")
    searchroot.title("Security Management System")
    searchroot.config(bg="seashell4")
    #searchroot.iconbitmap("logo.png.ico")
    searchroot.resizable(False,False)
    
#-----------------------------------------------------------Add Student Labels
    idlabel = Label(searchroot,text="Enter ID: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    idlabel.place(x=10,y=10)
    
    namelabel = Label(searchroot,text="Enter Name: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    namelabel.place(x=10,y=70)
    
    mobilelabel = Label(searchroot,text="Enter Mobile: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(searchroot,text="Enter Email: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    emaillabel.place(x=10,y=190)
    
    addresslabel = Label(searchroot,text="Enter Address: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    addresslabel.place(x=10,y=250)
    
    genderlabel = Label(searchroot,text="Enter Gender: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    genderlabel.place(x=10,y=310)
    
    rolelabel = Label(searchroot,text="Enter Role: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    rolelabel.place(x=10,y=370)
    
    datelabel = Label(searchroot,text="Enter Date: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    datelabel.place(x=10,y=430)
    
    """timelabel = Label(searchroot,text="Enter Time: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    timelabel.place(x=10,y=490)"""
    
    ###########################################################33
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    roleval = StringVar()
    dateval = StringVar()
    """timeval = StringVar()"""
    
    
    identry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    roleentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=roleval)
    roleentry.place(x=250,y=370)
    
    
    dateentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    """timeeentry = Entry(searchroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=timeval)
    timeeentry.place(x=250,y=490)"""
    
    #########-----------------------------------------------------------------------add button
    submitbtn = Button(searchroot,text="SUBMIT",font=("Constantia",17,"bold"),width=10,bd=5,activebackground="darkslategrey",activeforeground="gainsboro",command=search)
    
    submitbtn.place(x=150,y=480)
    
    searchroot.mainloop()
  
 ########################################################################################################################################################33   

    
    
    
    
    
    
    
    
    
    
    
    ###################################################################################################################################################
def updatedetails():
    def update():

        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        role = roleval.get()
        date = dateval.get()
        time = timeval.get()
        """added_time = time.strftime("%H:%M:%S")
        added_date = time.strftime("%d/%m/%Y")"""
        
        strr = "update detailstable set name=%s,mobile=%s,email=%s,address=%s,gender=%s,role=%s,date=%s,time=%s where id=%s"
        mycursor.execute(strr,(name,mobile,email,address,gender,role,date,time,id)) 
        con.commit()
        messagebox.showinfo("Notifications","Id {} updated successfully...".format(id),parent=updateroot)
        strr ="select * from detailstable" 
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        detailstable.delete(*detailstable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            detailstable.insert("",END,values=vv)
         
             
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry("470x585+220+160")
    updateroot.title("Security Management System")
    updateroot.config(bg="seashell4")
    #updateroot.iconbitmap("logo.png.ico")
    updateroot.resizable(False,False)


#-----------------------------------------------------------Add Student Labels
    idlabel = Label(updateroot,text="Enter ID: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    idlabel.place(x=10,y=10)
    
    namelabel = Label(updateroot,text="Enter Name: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    namelabel.place(x=10,y=70)
    
    mobilelabel = Label(updateroot,text="Enter Mobile: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    mobilelabel.place(x=10,y=130)
    
    emaillabel = Label(updateroot,text="Enter Email: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    emaillabel.place(x=10,y=190)
    
    addresslabel = Label(updateroot,text="Enter Address: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    addresslabel.place(x=10,y=250)
    
    genderlabel = Label(updateroot,text="Enter Gender: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    genderlabel.place(x=10,y=310)
    
    rolelabel = Label(updateroot,text="Enter Role: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    rolelabel.place(x=10,y=370)
    
    datelabel = Label(updateroot,text="Enter Date: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    datelabel.place(x=10,y=430)
    
    timelabel = Label(updateroot,text="Enter Time: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    timelabel.place(x=10,y=490)
    
    ###########################################################33
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    roleval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    
    identry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    roleentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=roleval)
    roleentry.place(x=250,y=370)
    
    dateentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    timeeentry = Entry(updateroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=timeval)
    timeeentry.place(x=250,y=490)
    
    #########-----------------------------------------------------------------------add button
    submitbtn = Button(updateroot,text="SUBMIT",font=("Constantia",17,"bold"),width=10,bd=5,activebackground="darkslategrey",activeforeground="gainsboro",command=update)

    submitbtn.place(x=150,y=540)
    
    cc = detailstable.focus()
    content = detailstable.item(cc)
    pp = content["values"]
    if(len(pp) != 0):
         idval.set(pp[0])
         nameval.set(pp[1])
         mobileval.set(pp[2])
         emailval.set(pp[3])
         addressval.set(pp[4])
         genderval.set(pp[5])
         roleval.set(pp[6])
         dateval.set(pp[7])
         timeval.set(pp[8])
    
    
    
    
    
    
    updateroot.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    #######################################################################    
    
    
    
    
    
def deletedetails():
    cc = detailstable.focus()
    content = detailstable.item(cc)

    pp = content["values"][0]
    strr = "delete from detailstable where id =%s"
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo("Notifications","Id {} deleted successfully...".format(pp))
    strr ="select * from detailstable" 
    mycursor.execute(strr) 
    datas = mycursor.fetchall()
    detailstable.delete(*detailstable.get_children())
    for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            detailstable.insert("",END,values=vv)


   
    

def showdetails():
        global con,mycursor
        host = "localhost"
        user = "root"
        password = "root"
        database = "securitymanagementsystem1"
        strr ="select * from detailstable" 
        con = pymysql.connect(host=host,user=user,password=password,database=database)
        mycursor = con.cursor()


        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        detailstable.delete(*detailstable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            detailstable.insert("",END,values=vv)

"""def exportdetails():
    import pandas as pd
    from tkinter import filedialog, messagebox

    ff = filedialog.asksaveasfile()
    gg = detailstable.get_children()
    id,name,mobile,email,address,gender,role,added_date,added_time=[],[],[],[],[],[],[],[],[]
    for i in gg:
       content = detailstable.item(i) 
       pp = content["values"]
       id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),role.append(pp[6]),added_date.append(pp[7]),added_time.append(pp[8])
       dd = ["Id","Name","Mobile","Email","Address","Gender","Role","Added_date","Added_time"]
       df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,role,added_date,added_time)),columns=dd)
       paths = r"{}.csv".format(ff)
       df.to_csv(paths,index=False)
       messagebox.showinfo("Notifications","Details are saved {}".format(paths))"""
       
import pandas as pd
from tkinter import filedialog, messagebox

def exportdetails():
    ff = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if ff:
        gg = detailstable.get_children()
        data = []
        for i in gg:
            content = detailstable.item(i)
            pp = content["values"]
            data.append(pp)
        
        columns = ["Id", "Name", "Mobile", "Email", "Address", "Gender", "Role", "Added_date", "Added_time"]
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(ff, index=False)
        messagebox.showinfo("Notifications", "Details are saved to {}".format(ff))
    
    
    
"""import pandas as pd
from tkinter import filedialog, messagebox

def exportdetails(detailstable):
    ff = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if ff:
        gg = detailstable.get_children()
        data = []
        for i in gg:
            content = detailstable.item(i)
            pp = content["values"]
            data.append(pp)
        
        columns = ["Id", "Name", "Mobile", "Email", "Address", "Gender", "Role", "Added_date", "Added_time"]
        df = pd.DataFrame(data, columns=columns)
        
        # Save data to CSV
        df.to_csv(ff, index=False)
        
        # Show info message
        messagebox.showinfo("Notifications", "Details are saved to {}".format(ff))
        
        # Display the stored data in the table (if detailstable supports it)
        if hasattr(detailstable, 'insert_data_from_df'):
            detailstable.insert_data_from_df(df)
        else:
            messagebox.showwarning("Warning", "Unable to display stored data in the table.")

# Example usage
# Assuming detailstable is some kind of table widget
# exportdetails(detailstable)"""




       
    
def exit():
    #print("Exit")  
    res = messagebox.askyesnocancel("Notification","Do you want to Exit?")
    if(res == True):
        root.destroy()
     
######################################################Connection of Database


def Connectdb():
    def submitdb():
        global con,mycursor
        #host = hostval.get()
        #user = userval.get()
        #password = passwordval.get()
        host = "localhost"
        user = "root"
        password = "root"
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror("Notifications","Data is incorrect please try again")
            return
        try:
            strr = "create database securitymanagementsystem1"
            mycursor.execute(strr)
            strr = "use securitymanagementsystem1"
            mycursor.execute(strr)
            strr = "create table detailstable1(id int,name varchar(20),mobile varchar(20),email varchar(30),address varchar(100),gender varchar(50),role varchar(50),date varchar(50),time varchar(50))"
            mycursor.execute(strr)
            strr = "alter table detailstable1 modify column id int not null"
            mycursor.execute(strr)
            strr = "alter table detailstable1 modify column id int primary key"
            mycursor.execute(strr)
            messagebox.showinfo("Notofications","You are now logged into the system.",parent=dbroot)

            

            
        except:
            strr = " use securitymanagementsystem1"
            mycursor.execute(strr)
            messagebox.showinfo("Notofications","You are now logged into the system.",parent=dbroot)
        dbroot.destroy()
            

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x250+800+230") 
    #dbroot.iconbitmap("logo.png.ico")
    dbroot.resizable(False,False)
    dbroot.config(bg="seashell4")
    #--------------------------------------------------------------------Connectdb Labels
    hostLabel = Label(dbroot,text="Enter Host: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    hostLabel.place(x=10,y=10)
    
    userLabel = Label(dbroot,text="Enter User: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    userLabel.place(x=10,y=70)
    
    passwordLabel = Label(dbroot,text="Enter Password: ",bg="seashell3",font=("Constantia",18,"bold"),relief=GROOVE,borderwidth=3,width=12)
    passwordLabel.place(x=10,y=130)
    
    #----------------------------------------------------------------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    
    hostentry = Entry(dbroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=hostval)
    hostentry.place(x=250,y=10)
    
    userentry = Entry(dbroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwordentry = Entry(dbroot,font=("Constantia",15,"bold"),bd=5,bg="seashell3",textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    
    #-----------------------------------------------------------------------------Connectdb button
    submitbutton = Button(dbroot,text="SUBMIT",font=("Constantia",17,"bold"),width=20,bd=5,
                          activebackground="darkslategrey",activeforeground="gainsboro",command=submitdb)
    submitbutton.place(x=150,y=190)
                    
    dbroot.mainloop()
    



###################################################################################Connection of Database
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    #print(time_string,date_string)
    clock.config(text="Date :" +date_string+"\n"+"Time :" +time_string)
    clock.after(200,tick)
################################################################################### INTRO SLIDER
import random
colors = ["cornsilk2","cornsilk"] 
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20,IntroLabelColorTick)
    
    
def IntroLabelTick():
   global count,text
   if(count>=len(ss)):
       count = 0
       text = ""
       SliderLabel.config(text=text)
   else:
       text = text+ss[count]
       SliderLabel.config(text=text)
       count += 1
   SliderLabel.after(100,IntroLabelTick)  


#################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk() 
root.title(" Security Management System ")
root.config(bg="black")
root.geometry("1174x700+200+50")
#root.iconbitmap("logo.png.ico")
root.resizable(False,False)
##############################################################  Frames
###-------------------------------------------------------Data Entry Frame

DataEntryFrame = Frame(root,bg="grey",relief=GROOVE,borderwidth=3)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
#Data Entry Frame Intro
frontlabel = Label(DataEntryFrame,text="WELCOME",width=30,font=("Lucida Console",20," italic bold"),bg="grey")
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text=" 1.  Add Details",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=adddetails)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text=" 2.  Search Details",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=searchdetails)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text=" 3.  Delete Details",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=deletedetails)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text=" 4.  Update Details",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=updatedetails)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text=" 5.  Show All Details",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=showdetails)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text=" 6.  Export Data",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=exportdetails)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text=" 7.  Exit",width=25,font=("Constantia",20,"bold"),bd=6,bg="darkgrey",fg="gray1",
                activebackground="lightcyan4",activeforeground="lightgoldenrodyellow",relief=RIDGE,command=exit)
exitbtn.pack(side=TOP,expand=True)







##------------------------------------------------------------------------Show Data Frame

ShowDataFrame = Frame(root,bg="grey",relief=GROOVE,borderwidth=3)
ShowDataFrame.place(x=550,y=80,width=620,height=600)


#------------------------------------------------------------------------------Show Data Frames
style = ttk.Style()
style.configure("Treeview.Heading",font=("Constantia",20,"bold"),foreground="midnightblue")
style.configure("Treeview",font=("Times",15,"bold"),foreground="black",background="floralwhite")


scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)


detailstable = Treeview(ShowDataFrame,columns=("ID","Name","Mobile No.","Email","Address","Gender","Role","Added Date","Added Time")
                   ,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=detailstable.xview)
scroll_y.config(command=detailstable.yview)

detailstable.heading("ID",text="ID")
detailstable.heading("Name",text="Name")
detailstable.heading("Mobile No.",text="Mobile No.")
detailstable.heading("Email",text="Email")
detailstable.heading("Address",text="Address")
detailstable.heading("Gender",text="Gender")
detailstable.heading("Role",text="Role")
detailstable.heading("Added Date",text="Added Date")
detailstable.heading("Added Time",text="Added Time")
detailstable.column("ID",width=200)
detailstable.column("Name",width=200)
detailstable.column("Mobile No.",width=200)
detailstable.column("Email",width=300)
detailstable.column("Address",width=300)
detailstable.column("Gender",width=200)
detailstable.column("Role",width=200)
detailstable.column("Added Date",width=200)
detailstable.column("Added Time",width=200)


detailstable["show"] = "headings"
detailstable.pack(fill=BOTH,expand=1)

















###################################################################### Sliders
ss = " Security Management System  "
count = 0
text = ""
####################################################################################
SliderLabel = Label(root,text=ss,font=("fantasy",30,"italic bold"),bg="grey",relief=RIDGE,borderwidth=5,width=25)
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
############################################################################33 clock
clock = Label(root,text=ss,font=("fantasy",14," bold"),bg="gainsboro",relief=RIDGE,borderwidth=5,width=20,
              activebackground="darkslategrey",activeforeground="gainsboro")
clock.place(x=0,y=0)
tick()
################################################################# CONNECT TO DATABASE BUTTON
connectbutton = Button(root,text="Click Here To Login",width=20,font=("Pacifico",19,"bold"),bg="gainsboro",relief=RIDGE,borderwidth=5,
                       activebackground="darkslategrey",activeforeground="gainsboro",command=Connectdb)
SliderLabel.place(x=260,y=0)
connectbutton.place(x=877,y=0)

root.mainloop()





