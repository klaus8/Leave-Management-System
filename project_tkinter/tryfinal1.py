from tkinter import *
from tkinter import ttk
# import sqlite3
import time
from tkinter import Text, Tk
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image
import mysql.connector
global user3


def main():
    global root1
    root1 = Tk()
    global passw
    passw = StringVar()
    global passw2
    passw2 = StringVar()
    global userid
    userid = StringVar()
    global userid1
    userid1 = StringVar()
    global var
    var = IntVar()
    global sum
    sum = IntVar()

    root1.geometry("1366x768+0+0")
    root1.title("WELCOME TO CMRIT HOME PAGE")
    cmrit_label = Label(text="welcome to cmrit", font="Times 20 italic bold", bg="#154360" ).pack(side=TOP,  fill=X)

    def admin1():
        root1.destroy()
        root2=Tk()
        root2.geometry("1600x1000+0+0")
        root2.title("WELCOME TO ADMIN HOME PAGE")
        admin_label = Label(text="WELCOME TO ADMIN PAGE", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
        main_label=Label(bg="green").pack(x=100,fill=X)
        root2.mainloop()

    def choose_admin():

        user = userid.get()
        passw1 = passw.get()

        print(f"The name entered by you is {user} {passw1}")
        db = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="Shivam289#",
                                             db="LEAVE1")
        cursor = db.cursor()
        savequery = "select ADMIN_ID,ADMIN_DOB FROM ADMIN"
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        flag=0

        for x in myresult:
            if (str(user) == str(x[0]) and str(passw1) == str(x[1])):
                flag=1
        if flag==1:
            root1.destroy()
            # import admin_page2
            from tryfinal2 import main3
            main3(user)
        else:

            msg = tmsg.askyesno("WRONG PASSW",
                                                    " TRY AGAIN ")
            if msg>0:
                userid.delete(0, END)
                passw.delete(0, END)
                # user.delete(0, END)
                # passw1.delete(0, END)

            else:
                d0()





    def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))


    c1=Canvas(root1,width=400,height=1600,bg="#5499C7",relief='ridge')
    c1.pack(side=TOP,anchor="nw")
    c2=Canvas(root1,width=1200,height=1600,bg="#A9CCE3",relief='ridge')
    c2.place(x=400,y=37)
    login_label = Label(c1,text="Log In", font="Times 20 bold", bg="#117A65",pady=3,padx=30).place(x=120, y=330)
    t1=True

    def new_user():
        print("working1")
    def existing():
        print("working2")

    def admin_entry():
        msg = tmsg.askyesno("CONFIRMNATION",
                            " ADMIN: click yes for office use ")
        if msg > 0:
            client_button.destroy()
            text.destroy()
            l2 = Label(text="ENTER USER ID", bg="#48C9B0", padx=5, pady=5, font="arial 15 bold").place(x=630, y=100)
            user = Entry(width=20, show="*", bd=5, font=("arial", 20), textvar=userid, bg="#7DCEA0")
            user.place(x=600, y=150)
            l1 = Label(text="ENTER PASSWORD", bg="#48C9B0", padx=5, pady=5, font="arial 15 bold").place(x=630, y=200)
            user = Entry(width=20, show="*", bd=5, font=("arial", 20), textvar=passw, bg="#7DCEA0")
            user.place(x=600, y=250)
            admin_submit = Button(root1, text="SUBMIT", bg="#C39BD3", height=2, font="Times 12 bold",
                        command=choose_admin, padx=5).place(x=850, y=300)

            my_pic = Image.open("admin.png")
            re = my_pic.resize((220, 150), Image.ANTIALIAS)
            new_pic = ImageTk.PhotoImage(re)
            my_img = c2.create_image(740, 0, anchor=NW, image=new_pic)


            b2 = Button(c2, text="<<BACK", bg="#C39BD3", height=2, font="Times 13 bold", padx=7, command=d0).place(
                x=200, y=250)
            while (t1):
                for x in range(0, 40):
                    c2.move(my_img, 0, 5)
                    root1.update()
                    time.sleep(0.05)


                for x in range(0, 40):
                    c2.move(my_img, 0, -5)
                    root1.update()
                    time.sleep(0.05)


    def d0():
        t1=False
        root1.destroy()
        main()

    def choose():
        admin_button.destroy()


        def choose_user():
            user3 = userid1.get()
            passw3 = passw2.get()

            print(f"The name entered by you is {user3} {passw3}")
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Shivam289#",
                                         db="LEAVE1")
            cursor = db.cursor()
            savequery = "select CLIENT_ID,CLIENT_DOB FROM CLIENT"
            cursor.execute(savequery)
            myresult = cursor.fetchall()
            flag1 = 0

            for x in myresult:
                print(x[0],x[1])
                if (str(user3) == str(x[0]) and str(passw3) == str(x[1])):
                    flag1 = 1
                    print(int(x[0]))
                    d=int(x[0])
                    # fu=int(x[0])

            if flag1 == 1:
                root1.destroy()
                # flag=0
                # import client2
                from tryfinal3 import client
                client(user3)
            else:
                msg = tmsg.askyesno("WRONG PASSW",
                                    " TRY AGAIN ")
                if msg > 0:
                    userid1.delete(0, END)
                    passw2.delete(0, END)

                else:
                    d0()



        l2 = Label(text="ENTER USER ID", bg="#48C9B0", padx=5, pady=5, font="arial 15 bold").place(x=630, y=100)
        user = Entry(width=20, show="*", bd=5, font=("arial", 20), textvar=userid1, bg="#7DCEA0")
        user.place(x=600, y=150)
        l1 = Label(text="ENTER PASSWORD", bg="#48C9B0", padx=5, pady=5, font="arial 15 bold").place(x=630, y=200)
        user = Entry(width=20, show="*", bd=5, font=("arial", 20), textvar=passw2, bg="#7DCEA0")
        user.place(x=600, y=250)

        clientb = Button(root1, text="SUBMIT", bg="#C39BD3", height=2, font="Times 12 bold",
                    command=choose_user, padx=5).place(x=850, y=300)

        my_pic = Image.open("client.png")
        re = my_pic.resize((220, 150), Image.ANTIALIAS)
        new_pic = ImageTk.PhotoImage(re)
        my_img = c2.create_image(740, 0, anchor=NW, image=new_pic)
        b2 = Button(c2, text="<<BACK", bg="#C39BD3", height=2, font="Times 13 bold", padx=7, command=d0).place(
            x=200, y=250)
        while (t1):
            for x in range(0, 40):
                c2.move(my_img, 0, 5)
                root1.update()
                time.sleep(0.05)


            for x in range(0, 40):
                c2.move(my_img, 0, -5)
                root1.update()
                time.sleep(0.05)

    admin_button = Button(c1,
                            text="FOR ADMIN",
                            bg="#117864", height=1, width=20, font="Times 20 bold", command=admin_entry)
    admin_button.place(x=30, y=400)

    text = Text(c1)
    text = Text(c1, height=2, width=30, bg="#5499C7",fg="#1F618D")
    text.insert(INSERT,
                '''NOTE-Click "for admin:     (To see  details)''')

    text.insert(END, "!")
    text.place(x=40, y=550)

    client_button = Button(c1,
                            text="FOR client",
                            bg="#117864", height=1, width=20, font="Times 20 bold", command=choose)
    client_button.place(x=30, y=470)

    changeOnHover(client_button, "#3498DB", "#117864")
    changeOnHover(admin_button, "#B03A2E", "#117864")

    my_pic = Image.open("cmrit.png")
    re = my_pic.resize((300, 300), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(re)
    my_img = c1.create_image(0, 0, anchor=NW, image=new_pic)
    my_pic1 = Image.open("clg.png")
    re1 = my_pic1.resize((960, 320), Image.ANTIALIAS)
    new_pic1 = ImageTk.PhotoImage(re1)
    my_img1 = c2.create_image(0, 350, anchor=NW, image=new_pic1)
    l2=Label(c2,text="LEAVE MANAGEMENT SYSTEM",font="Times 25 bold",bg="#16A085",padx=15).place(x=150,y=5)


    root1.mainloop()
# main()