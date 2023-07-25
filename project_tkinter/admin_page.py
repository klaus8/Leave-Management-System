from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
root2=Tk()
root2.geometry("1600x1000+0+0")
root2.title("WELCOME TO ADMIN HOME PAGE")
from tkinter import Text, Tk

def buttons():
    applic()
def company():
    print("google")
admin_label = Label(text="WELCOME TO ADMIN PAGE", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
f0=Frame(root2, bg="#7F8C8D",pady=3)
f0.pack(fill=X)
button1=Button(f0,text="Profile",bg="#F39C12",height=2,width=20,command=company)
button1.pack(side=LEFT)
button1=Button(f0,text="Add Employee",bg="#F39C12",height=2,width=20,command=buttons)
button1.pack(side=LEFT)
# menu= StringVar()
# menu.set("Application")

#Create a dropdown Menu
# drop= OptionMenu(f0, menu,"Add employee", "Remove employee","Leave request","Solve issue","See profile")
# drop.pack(side=LEFT)
button1=Button(f0,text="Remove Employee",bg="#F39C12",height=2,width=20,command=company)
button1.pack(side=LEFT)
button1=Button(f0,text="See Client Profile",bg="#F39C12",height=2,width=20,command=company)
button1.pack(side=LEFT)
button1=Button(f0,text="Extract Issue",bg="#F39C12",height=2,width=20,command=company)
button1.pack(side=LEFT)
button1=Button(f0,text="Solve Issue",bg="#F39C12",height=2,width=20,command=company)
button1.pack(side=LEFT)
button1=Button(f0,text="Log out",bg="#F39C12",height=2,width=20,command=company)
button1.pack(side=RIGHT)

#
# my_pic = Image.open("admin1.png")
# # re = my_pic.resize((220, 150), Image.ANTIALIAS)
# # new_pic = ImageTk.PhotoImage(re)
# # my_img = root2.create_image(740, 0, anchor=NW, image=new_pic)
def ex_issue():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="Shivam289#",
                                 db="LEAVE1")
    cursor = db.cursor()
    savequery = "select ADMIN_ID,ADMIN_DOB FROM ADMIN"
    cursor.execute(savequery)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
def add_employee():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="Shivam289#",
                                 db="LEAVE1")
    cursor = db.cursor()
    savequery = "INSERT INTO CLIENT VALUES(1,'shivam','2002-08-26','abc','2010-05-05',2000000)"
    cursor.execute(savequery)
    db.commit()
    print("working")
def del_employee():

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="Shivam289#",
                                 db="LEAVE1")
    cursor = db.cursor()
    savequery = "DELETE FROM CLIENT WHERE CLIENT_ID=1"
    cursor.execute(savequery)
    db.commit()
    print("working")





canvas = Canvas(root2, bg='yellow',width = 1000, height = 800)
canvas.pack()
canvas99 = Canvas(canvas, bg='blue',width = 600, height = 410)
canvas99.place(x=400,y=0)
canvas100 = Canvas(canvas, bg='blue',width = 1000, height = 195)
canvas100.place(x=0,y=410)
def applic():
    button1 = Button(root2, text="Add employee", bg="green", height=3, width=30, command=add_employee)
    button1.place(x=730,y=120)
    button1 = Button(root2, text="Remove employee", bg="green", height=3, width=30, command=del_employee)
    button1.place(x=730, y=170)
    button1 = Button(root2, text="See profile", bg="green", height=3, width=30, command=company)
    button1.place(x=730, y=220)
    button1 = Button(root2, text="Extract issue", bg="green", height=3, width=30, command=ex_issue)
    button1.place(x=730, y=270)
    button1 = Button(root2, text="Solve issue", bg="green", height=3, width=30, command=company)
    button1.place(x=730, y=320)
    button1 = Button(root2, text="<<BACK", bg="green", height=3, width=30, command=company)
    button1.place(x=850, y=400)

my_pic = Image.open("admin1.png")
re = my_pic.resize((400, 410), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(re)
my_img = canvas.create_image(0, 0, anchor=NW, image=new_pic)
# img = PhotoImage(file="admin1.png")
# canvas.create_image(20,20, anchor=NW, image=img)


root2.mainloop()


