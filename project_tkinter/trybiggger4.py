from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import tkinter as tk
def leave(io):
    root6 = tk.Tk()
    root6.geometry("1600x1000+0+0")
    root6.title("WELCOME TO ADMIN HOME PAGE")
    from tkinter import Text, Tk
    global start_date
    start_date=StringVar()
    global last_date
    last_date=StringVar()
    global msg1
    msg1=StringVar()
    client_label = Label(text="WELCOME TO CLIENT PAGE", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
    root6.configure(bg="#1F618D")
    my_pic2 = Image.open("leave_logo.png")
    re2 = my_pic2.resize((300, 320), Image.ANTIALIAS)
    new_pic2 = ImageTk.PhotoImage(re2)
    l1 = Label(root6, image=new_pic2)
    l1.place(x=900, y=200)

    l1 = Label(root6, text="ID", width=15, font=("arial", 24)).place(x=40, y=200)
    l1 = Label(root6, text="NAME", width=15, font=("arial", 24)).place(x=40, y=250)
    l1 = Label(root6, text="START DATE", width=15, font=("arial", 24)).place(x=40, y=300)
    l1 = Label(root6, text="LAST DATE", width=15, font=("arial", 24)).place(x=40, y=350)
    l1 = Label(root6, text="MESSAGE", width=15, font=("arial", 24)).place(x=40, y=400)

    # SUM = 15
    SUM=io
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Shivam289#",
        database="LEAVE1"
    )
    # f=16
    my_conn = my_connect.cursor()

    ####### end of connection ####
    querry1 = ("SELECT CLIENT_ID from CLIENT WHERE CLIENT_ID=%s")
    my_conn.execute(querry1, (SUM,))
    T = my_conn.fetchall()
    # e1 = Entry(root6, width=10, font=("arial", 24))
    # e1.insert(END, T)
    # e1.place(x=400, y=200)
    e1 = Label(root6, text=T,width=10, font=("arial", 24))
    # e1.insert(END, T)
    e1.place(x=400, y=200)


    querry1 = ("SELECT CLIENT_NAME from CLIENT WHERE CLIENT_ID=%s")
    my_conn.execute(querry1, (SUM,))
    T = my_conn.fetchall()
    e1 = Label(root6, text=T,width=10, font=("arial", 24))
    # e1.insert(END, T)
    e1.place(x=400, y=250)


    e1=Entry(root6,width=10,font=("arial", 24),textvariable=start_date)
    e1.place(x=400,y=300)
    e1=Entry(root6,width=10,font=("arial", 24),textvariable=last_date)
    e1.place(x=400,y=350)
    e1=Entry(root6,width=25,font=("arial", 24),textvariable=msg1)
    e1.place(x=400,y=400)
    def submit_client(io):
        print(io)

        print(start_date.get())
        print(last_date.get())
        print(msg1.get())
        SD=start_date.get()
        LD=last_date.get()
        MS=msg1.get()
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Shivam289#",
            database="LEAVE1"
        )

        my_conn = my_connect.cursor()

        ####### end of connection ####
        querry1 = ('''INSERT INTO LEAVE2(LEAVE_STARTDATE,LEAVE_LASTDATE,LEAVE_MSG,LEAVE_STATUS,CLIENT_ID) VALUES(%s,%s,%s,"NO",%s)''')
        my_conn.execute(querry1, (SD,LD,MS,io))
        my_connect.commit()




        print("work")
    def back69(ru):
        root6.destroy()
        # import client2
        from trybigger3 import client
        client(ru)
    b9=Button(root6,text='SUBMIT',bg='#154360',font=("arial",20),command=lambda :submit_client(io)).place(x=700,y=550)
    b9 = Button(root6, text='<<BACK', bg='#154360', font=("arial", 20), command=lambda:back69(io)).place(x=1200, y=50)
    root6.mainloop()
# leave(15)
