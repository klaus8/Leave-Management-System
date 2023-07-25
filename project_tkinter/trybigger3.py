from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import tkinter as tk
# import client_profile

global root2
global root6
global SUM
# from try0801 import *


def client(ru):
    global root2
    root2 = tk.Tk()
    root2.geometry("1600x1000+0+0")
    root2.title("WELCOME TO CLIENT HOME PAGE")
    from tkinter import Text, Tk
    client_label = Label(text="WELCOME TO CLIENT PAGE", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
    root2.configure(bg="#1ABC9C")


    def shift():
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000//fps,shift)
    ############# Main program ###############

    canvas=Canvas(root2,bg='#1ABC9C')
    # canvas.pack(fill=X)
    canvas.place(x=200,y=400)
    text_var="WELCOME TO CLIENT PAGE"
    text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',50,'bold'),fill='#F7DC6F',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width']=width
    canvas['height']=height
    fps=100   #Change the fps to make the animation faster/slower
    shift()
    def back67(ru):
        root5.destroy()
        client(ru)

    def prof(ru):
        root2.destroy()
        pro(ru)

    def pro(ru):

        global root5
        root5 = Tk()
        root5.geometry("1600x1000+0+0")
        root5.title("WELCOME TO ADMIN HOME PAGE")


        client_label = Label(text="WELCOME TO CLIENT PAGE", font="Times 20 italic bold", bg="#A2D9CE").pack(side=TOP,
                                                                                                            fill=X)
        root5.configure(bg="#5DADE2")

        # my_pic2 = Image.open("clinet_profile.png")
        # re2 = my_pic2.resize((250, 180), Image.ANTIALIAS)
        # new_pic2 = ImageTk.PhotoImage(re2)
        # l1 = Label(root5, image=new_pic2)
        # l1.place(x=50, y=100)
        my_pic2 = Image.open("clinet_profile.png")
        re2 = my_pic2.resize((300, 320), Image.ANTIALIAS)
        new_pic2 = ImageTk.PhotoImage(re2)
        l1 = Label(root5, image=new_pic2)
        l1.place(x=50, y=100)
        # SUM=15
        SUM=ru
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Shivam289#",
            database="LEAVE1"
        )

        my_conn = my_connect.cursor()

        ####### end of connection ####
        querry1 = ("SELECT CLIENT_ID from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=200)
        querry1 = ("SELECT CLIENT_NAME from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=250)
        print(T)
        querry1 = ("SELECT CLIENT_ADD from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=300)

        querry1 = ("SELECT JOINING_DATE from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=350)

        querry1 = ("SELECT CLIENT_DOB from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=400)

        querry1 = ("SELECT SALARY from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=450)

        querry1 = ("SELECT SALARY_INC from SALARY1 WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=500)

        querry1 = ("SELECT SALARY_DEC from SALARY1 WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Label(root5, text=T,width=10, font=("arial", 24))
        # e1.insert(END, T)
        e1.place(x=800, y=550)

        querry1 = ("SELECT WORK_HOUR from SALARY1 WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Entry(root5, width=10, font=("arial", 24))
        e1.insert(END, T)
        e1.place(x=800, y=600)

        l1 = Label(root5, text="ID", width=20, font=("arial", 24)).place(x=400, y=200)
        l1 = Label(root5, text="NAME", width=20, font=("arial", 24)).place(x=400, y=250)
        l1 = Label(root5, text="ADDRESS", width=20, font=("arial", 24)).place(x=400, y=300)
        l1 = Label(root5, text="JOIN DATE", width=20, font=("arial", 24)).place(x=400, y=350)
        l1 = Label(root5, text="DOB", width=20, font=("arial", 24)).place(x=400, y=400)
        l1 = Label(root5, text="SALARY", width=20, font=("arial", 24)).place(x=400, y=450)
        l1 = Label(root5, text="INCREMENT", width=20, font=("arial", 24)).place(x=400, y=500)
        l1 = Label(root5, text="DECREMENT", width=20, font=("arial", 24)).place(x=400, y=550)
        l1 = Label(root5, text="WORK HRS", width=20, font=("arial", 24)).place(x=400, y=600)

        b34=Button(root5,text="<<BACK",width=10,font=("arial",18),command=lambda :back67(ru)).place(x=1200,y=40)
        print(T)



        root5.mainloop()

    # def back68():
    #     # root2.destroy()
    #     rqst()


    def rqst(ru):

        # back68()

        # root6 = tk.Tk()
        # root6.geometry("1600x1000+0+0")
        # root6.title("WELCOME TO ADMIN HOME PAGE")
        # from tkinter import Text, Tk
        # global start_date
        # start_date = StringVar()
        # global last_date
        # last_date = StringVar()
        # global msg1
        # msg1 = StringVar()
        # client_label = Label(text="WELCOME TO CLIENT PAGE", font="Times 20 italic bold", bg="#154360").pack(side=TOP,
        #                                                                                                     fill=X)
        # root6.configure(bg="#1F618D")
        # my_pic2 = Image.open("leave_logo.png")
        # re2 = my_pic2.resize((300, 320), Image.ANTIALIAS)
        # new_pic2 = ImageTk.PhotoImage(re2)
        # l1 = Label(root6, image=new_pic2)
        # l1.place(x=900, y=200)
        #
        # l1 = Label(root6, text="ID", width=15, font=("arial", 24)).place(x=40, y=200)
        # l1 = Label(root6, text="NAME", width=15, font=("arial", 24)).place(x=40, y=250)
        # l1 = Label(root6, text="START DATE", width=15, font=("arial", 24)).place(x=40, y=300)
        # l1 = Label(root6, text="LAST DATE", width=15, font=("arial", 24)).place(x=40, y=350)
        # l1 = Label(root6, text="MESSAGE", width=15, font=("arial", 24)).place(x=40, y=400)
        #
        # SUM = 15
        # my_connect = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     passwd="Shivam289#",
        #     database="LEAVE1"
        # )
        # f = 23
        # my_conn = my_connect.cursor()
        #
        # ####### end of connection ####
        # querry1 = ("SELECT CLIENT_ID from CLIENT WHERE CLIENT_ID=%s")
        # my_conn.execute(querry1, (SUM,))
        # T = my_conn.fetchall()
        # e1 = Entry(root6, width=10, font=("arial", 24))
        # e1.insert(END, T)
        # e1.place(x=400, y=200)
        #
        # querry1 = ("SELECT CLIENT_NAME from CLIENT WHERE CLIENT_ID=%s")
        # my_conn.execute(querry1, (SUM,))
        # T = my_conn.fetchall()
        # e1 = Entry(root6, width=10, font=("arial", 24))
        # e1.insert(END, T)
        # e1.place(x=400, y=250)
        #
        # e1 = Entry(root6, width=10, font=("arial", 24), textvariable=start_date)
        # e1.place(x=400, y=300)
        # e1 = Entry(root6, width=10, font=("arial", 24), textvariable=last_date)
        # e1.place(x=400, y=350)
        # e1 = Entry(root6, width=25, font=("arial", 24), textvariable=msg1)
        # e1.place(x=400, y=400)

        # def submit_client():
        #     print(start_date.get())
        #     print(last_date.get())
        #     print(msg1.get())
        #     SD = start_date.get()
        #     LD = last_date.get()
        #     MS = msg1.get()
        #     my_connect = mysql.connector.connect(
        #         host="localhost",
        #         user="root",
        #         passwd="Shivam289#",
        #         database="LEAVE1"
        #     )
        #
        #     my_conn = my_connect.cursor()
        #
        #     ####### end of connection ####
        #     querry1 = (
        #         '''INSERT INTO LEAVE2(LEAVE_STARTDATE,LEAVE_LASTDATE,LEAVE_MSG,LEAVE_STATUS,CLIENT_ID) VALUES(%s,%s,%s,"NO",%s)''')
        #     my_conn.execute(querry1, (SD, LD, MS, f))
        #     T = my_connect.commit()
        #
        # b9 = Button(root6, text='SUBMIT', bg='#154360', font=("arial", 20), command=submit_client).place(x=700, y=550)
        # root6.mainloop()

        root2.destroy()
        # import leave_request
        from trybiggger4 import leave
        leave(ru)

    f0=Frame(root2, bg="#1ABC9C",pady=3)
    f0.pack(fill=X)
    button1=Button(f0,text="Profile",bg="#566573",height=2,width=20,command=lambda :prof(ru))
    button1.pack(side=LEFT)
    button1=Button(f0,text="Leave request",bg="#D4AC0D",height=2,width=20,command=lambda :rqst(ru))
    button1.pack(side=LEFT)
    # menu= StringVar()
    # menu.set("Application")
    def h1(ru):
        root2.destroy()
        from trybigger1 import main
        main()
    #Create a dropdown Menu
    # drop= OptionMenu(f0, menu,"Add employee", "Remove employee","Leave request","Solve issue","See profile")
    # drop.pack(side=
    print(ru)
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="Shivam289#",
                                 db="LEAVE1")
    cursor = db.cursor()
    # savequery = "DELETE FROM CLIENT WHERE CLIENT_ID=%s"
    # cursor.execute(savequery, (id35,))
    save = "SELECT * FROM REPORT where CLIENT_ID=%s"
    cursor.execute((save), (ru,))
    t = cursor.fetchall()
    print(t)
    print("dsf")
    # for i in t:
    #     if ru in
    global l
    print(len(t))
    k = "green"
    if len(t) > 0:

            print("fsd")
            l = "red"
    else:
        l = "#566573"
        print(l)
    k = l
    global root89
    def h2(ru):
        # root2.destroy()
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="Shivam289#",
                                     db="LEAVE1")
        cursor = db.cursor()
        # savequery = "DELETE FROM CLIENT WHERE CLIENT_ID=%s"
        # cursor.execute(savequery, (id35,))
        # save="SELECT * FROM REPORT where CLIENT_ID=%s"
        # cursor.execute((save),(ru,))
        # t=cursor.fetchall()
        # for i in t:
        #     print(i)
        root89=tk.Tk()
        root89.title("REPORT")
        root89.geometry("1366x768")
        # c1 = Canvas(root89, width=1366, height=768, bg="#76D7C4")
        # c1.pack()
        # my_pic = Image.open("Advance-Reporting.png")
        # re = my_pic.resize((1366, 768), Image.ANTIALIAS)
        # new_pic = ImageTk.PhotoImage(re)
        # my_img = c1.create_image(0, 0, anchor=NW, image=new_pic)
        # print(root89.winfo_screenwidth())
        # print(root89.winfo_screenheight())
        # # lab1=Label(root89,text="ID",font=("arial",18,"bold"))
        # # lab1.place(x=100,y=100)
        # c1.create_text(250,200,text="id",fill="#2E4053",font=("arial",23,"bold"))
        # c1.create_text(250, 300, text="ADMIN NAME", fill="#2E4053", font=("arial", 23, "bold"))
        #
        # c1.create_text(250, 400, text="STATUS", fill="#2E4053", font=("arial", 23, "bold"))
        # c1.create_text(250, 500, text="MESSAGE", fill="#2E4053", font=("arial", 23, "bold"))
        # c1.create_text(550,200,text=ru,fill="#2E4053",font=("arial",23,"bold"))
        # save1 = "SELECT ADMIN_ID FROM REPORT where CLIENT_ID=%s"
        # cursor.execute((save1), (ru,))
        # t = cursor.fetchall()
        # # l=t[0][3]
        # # print(l)
        # #
        # # save2="SELECT ADMIN_NAME FROM ADMIN WHERE ADMiN_ID=%s"
        # # cursor.execute((save2), (l,))
        # # t1= cursor.fetchall()
        # # print(t1)
        # c1.create_text(550, 300, text=t[0], fill="#2E4053", font=("arial", 23, "bold"))
        #
        # save1 = "SELECT REPORT_STATUS FROM REPORT where CLIENT_ID=%s"
        # cursor.execute((save1), (ru,))
        # t = cursor.fetchall()
        # # if t[0]==1:
        # #     q="YES"
        # # else:
        # #     q="NO"
        # c1.create_text(550, 400, text=t[0], fill="#2E4053", font=("arial", 23, "bold"))
        #
        # save1 = "SELECT REPORT_MSG FROM REPORT where CLIENT_ID=%s"
        # cursor.execute((save1), (ru,))
        # t = cursor.fetchall()
        # c1.create_text(550, 500, text=t[0], fill="#2E4053", font=("arial", 23, "bold"))

        lab = Label(root89, text="REPORT", bg="yellow", font=("arial", 18), height=20).place(x=1250, y=50)
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="Shivam289#",
                                     db="LEAVE1")
        cursor = db.cursor()
        savequery = '''select * from REPORT WHERE CLIENT_ID=%s'''
        cursor.execute((savequery),(ru,))
        myresult = cursor.fetchall()

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        i = 0
        for student in myresult:
            for j in range(len(student)):
                e = Entry(root89, width=15, fg='#D35400', bg="#839192", font=("arial", 18))
                e.grid(row=i + 100, column=j + 100)
                # e.place(x=i*5+100,y=5*j+100)
                e.insert(END, student[j])
            i = i + 1
        # def go1():
        #     root89.destroy()
        #     client(ru)


        def del1(ru,k):
            db1 = mysql.connector.connect(host="localhost",
                                          user="root",
                                          password="Shivam289#",
                                          db="LEAVE1")
            cursor1 = db1.cursor()

            save1 = "DELETE FROM REPORT where CLIENT_ID=%s"
            cursor1.execute((save1), (ru,))
            db1.commit()
            root89.destroy()
            # k="green"
            # go1()
            root2.destroy()
            client(ru)
        b2=Button(root89,text="DELETE ALL",font=("arial",23,"bold"),bg="red",command=lambda :del1(ru,k))
        b2.place(x=800,y=600)
        # b2 = Button(root89, text="DELETE ALL", font=("arial", 23, "bold"), bg="red", command=lambda: del1(ru))
        # b2.place(x=800, y=600)

        root89.mainloop()

        # db.commit()

    button1 = Button(f0, text="REPORT", bg=k, height=2, width=20, command=lambda :h2(ru))
    button1.pack(side=LEFT)
    button1=Button(f0,text="Log out",bg="#566573",height=2,width=20,command=lambda:h1(ru))
    button1.pack(side=RIGHT)

    root2.mainloop()
# client(15)