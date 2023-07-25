from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import tkinter as tk
import tkinter.messagebox as tmsg
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
        # last_date.delete(0,END)
        if (SD == '' or LD == '' or MS == ''):
            tmsg.showwarning("FILL", "FILLING ALL IS MANDATORY")
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Shivam289#",
            database="LEAVE1"
        )

        my_conn = my_connect.cursor()

        querry7 = ("SELECT JOINING_DATE from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry7, (SUM,))
        T1 = my_conn.fetchone()
        print(T1[0])
        j=str(T1[0])
        print(j)
        print(type(j))
        print(T1)

        k = ''
        o = ''
        f = ''
        s=''
        t=''
        g = ''
        d = ''
        for i in range(4):
            k = k + j[i]
            o = o + SD[i]
            f = f + LD[i]
            d = d + LD[i]
        print(k)
        r=''
        h=''
        w=''
        x=''

        for i in range(8,10):
            w=w+j[i]
            x=x+j[i-3]
            s=s+SD[i]
            t=t+LD[i]
            r=r+SD[i-3]
            h=h+LD[i-3]
        l = int(k)
        # k=0
        l5=int(w)
        l6=int(r)
        l7=int(s)
        l8=int(x)
        l1 = int(o)
        l2 = int(f)
        l3 = int(s)
        l4= int(t)
        print(l1,l2,l3,l4,l5,l6,l7,l8)
        if (l2>=l1 and l6>=l8 and l4>=l3 and h>=r):
            querry1 = ('''INSERT INTO LEAVE2(LEAVE_STARTDATE,LEAVE_LASTDATE,LEAVE_MSG,LEAVE_STATUS,CLIENT_ID,FLAG) VALUES(%s,%s,%s,"NO",%s,0)''')
            my_conn.execute(querry1, (SD,LD,MS,io))
            my_connect.commit()
            tmsg.showinfo("LEAVE REQUEST","DATA SENT INTO ADMIN")




            print("work")

        else:
            tmsg.showwarning("WRONG DATES", "INPUT VALID DATE")
    def back69(ru):
        root6.destroy()
        # import client2
        from tryfinal3 import client
        client(ru)
    b9=Button(root6,text='SUBMIT',bg='#154360',font=("arial",20),command=lambda :submit_client(io)).place(x=700,y=550)
    b9 = Button(root6, text='<<BACK', bg='#154360', font=("arial", 20), command=lambda:back69(io)).place(x=1200, y=50)
    root6.mainloop()
# leave(15)
