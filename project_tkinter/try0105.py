from tkinter import *
from tkcalendar import *
import tkinter as tk
import mysql.connector
from datetime import datetime
root3 = Tk()
root3.geometry("1600x1000+0+0")
root3.title("WELCOME TO ADMIN HOME PAGE")
# def change_date_format(d):
#     if d[6]

label = Label(root3, text="EMPLOYEE ADD", font=("arial", 25), bg="violetred1")
label.pack(side=TOP, fill=X)

label1 = Label(root3, text="ID:", font=("arial", 17))
label1.place(x=300, y=150)

label2 = Label(root3, text="NAME:", font=("arial", 17))
label2.place(x=300, y=210)

label3 = Label(root3, text="DOB:", font=("arial", 17))
label3.place(x=300, y=270)

label3 = Label(root3, text="ADD:", font=("arial", 17))
label3.place(x=300, y=330)

label4 = Label(root3, text="JOIN-DATE", font=("arial", 17))
label4.place(x=300, y=390)

label4 = Label(root3, text="SALARY", font=("arial", 17))
label4.place(x=300, y=450)

# VARIABLE
name= tk.StringVar()
salary = tk.StringVar()
id1 = tk.StringVar()
add = tk.StringVar()


# =entry field

entry6 = Entry(root3, textvar=salary, width=20, font=("arial", 15, "bold"), bd=5)
entry6.place(x=500, y=450)

entry1 = Entry(root3, bd=5, width=20, textvar=id1, font=("arial", 15))
entry1.place(x=500, y=150)

entry2 = Entry(root3, bd=5, width=20, textvar=name, font=("arial", 15))
entry2.place(x=500, y=210)

# entry3 = Entry(root3, bd=5, width=20, textvar=dob, font=("arial", 15))
# entry3.place(x=500, y=270)
# cal = DateEntry(root3, selectmode='day',date_format="y-mm-dd")
# cal.place(x=500, y=270)
# dt=cal.get()
# str1=dt.strftime("%Y-%m-%d")
# print(str1)
# print(type(dt))


entry4 = Entry(root3, bd=5, width=20, textvar=add, font=("arial", 15))
entry4.place(x=500, y=330)

# cal1 = DateEntry(root3, selectmode='day',date_format="y-mm-dd")
# cal1.place(x=500, y=390)

def mainF():
    global cal
    def getDate(cal):
        date=cal.get_date()
        print(date)
    # cal.place(x=900,y=100)
    # butt=Button(root3,text="Date Getter", bg="cyan",command=getDate).place(x=500,y=420)
cal1=DateEntry(root3,selectmode="day",date_pattern="y-mm-dd").place(x=500,y=390)

# print(type(cal1))
# but=Button(root3,text="Pick Date",command=mainF).place(x=500,y=390)
# but1=Button(root3,text="Pick Date",command=mainF).place(x=500,y=270)



# d2=cal.get()
# print(d2)
# year=year, month=month, day=day,
# cal1 = DateEntry(root3, width=8,
# # background='darkblue', foreground='white', borderwidth=2, locale = 'en_us', date_patern ='dd.mm.yyyy')
# # cal1.place(x=500, y=330)
# # d3=cal1.get()
# # print(d3+"sh")

def insert():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="Shivam289#",
                                 db="LEAVE1")
    cursor = db.cursor()
    # savequery = "INSERT INTO CLIENT VALUES(18,'shivam','2002-08-26','abc','2010-05-05',2000000)"
    # cursor.execute(savequery)
    # db.commit()

    # Creating a cursor object using the cursor() method
    # cursor = conn.cursor()
    # Preparing SQL query to INSERT a record into the database.
    insert_stmt = (
        "INSERT INTO CLIENT(CLIENT_ID, CLIENT_NAME,CLIENT_ADD, SALARY)"
        "VALUES (%s, %s, %s, %s)"
    )
    # if 2==int(id2):
    #     print("yes")
    data = (id3,name2,add2,salary1)
    try:
        # executing the sql command
        cursor.execute(insert_stmt, data)
        # commit changes in database
        db.commit()
    except:
        db.rollback()
        print("Stored successfully")


    # print(IntVar(id2))
    # print(IntVar(id2))
    # print(IntVar(id2))

def insert_table():
    global name2
    global id3
    global add2
    global salary1
    name1=name.get()
    add1=add.get()
    sal1=salary.get()
    id2=id1.get()
    salary1 = int(sal1)
    id3 = int(id2)
    name2 = str(name1)
    add2 = str(add1)
    print(name1,sal1,add1,id2)
    print(cal.get())
    print(cal1.get())
    insert()

button2 = Button(root3, text="SUBMIT FORM", width=14, font=("arial", 10), bg="indianred1", command=insert_table)
button2.place(x=660, y=630)
root3.mainloop()