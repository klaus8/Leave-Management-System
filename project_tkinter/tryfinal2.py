from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import tkinter as tk
global root2
import tkinter.messagebox as tmsg

global root3
def main3(y):
    root2 = tk.Tk()
    root2.geometry("1600x1000+0+0")
    root2.title("WELCOME TO ADMIN HOME PAGE")
    from tkinter import Text, Tk
    client_label = Label(text="WELCOME TO ADMIN PAGE", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
    root2.configure(bg="#117864")

    id1 = tk.StringVar()
    name = tk.StringVar()
    dob = tk.StringVar()
    address = tk.StringVar()
    join_date = tk.StringVar()
    salary = tk.StringVar()
    address1=tk.StringVar()
    e99=tk.StringVar()



    f0=Frame(root2, bg="#7F8C8D",pady=3)
    f0.pack(fill=X)

    def To_add_employee():
        root2.destroy()
        add_profile()

    def To_admin_profile(y):
        root2.destroy()
        admin_profile(y)
    def search_client(y):
        # root2.destroy()
        fetch_client(y)
    global entry42
    entry42=tk.StringVar
    def to_update_client_window(u,y):

        root2.destroy()
        update_client_profile(u,y)
    global e19
    e19=StringVar()

    def htao(y):
        root2.destroy()
        main3(y)
    def update_client_profile(u,y):
        print(u)
        root16 = tk.Tk()
        root16.title("CLIENT PROFILE")
        root16.geometry("1600x1000+0+0")
        root16.configure(bg="#3498DB")
        client_label = Label(text="WELCOME TO CLIENT PROFILE", font="Times 20 italic bold", bg="#154360").pack(side=TOP,
                                                                                                              fill=X)
        my_pic3 = Image.open("client_add.png")
        re3 = my_pic3.resize((300, 320), Image.ANTIALIAS)
        new_pic3 = ImageTk.PhotoImage(re3)
        l9 = Label(root16, image=new_pic3)
        l9.place(x=900, y=200)
        l1 = Label(root16, text="ID", width=15, font=("arial", 24)).place(x=40, y=200)
        l1 = Label(root16, text="NAME", width=15, font=("arial", 24)).place(x=40, y=250)
        l1 = Label(root16, text="D.O.B", width=15, font=("arial", 24)).place(x=40, y=300)
        l1 = Label(root16, text="BASE SALARY", width=15, font=("arial", 24)).place(x=40, y=350)
        l1 = Label(root16, text="MONTHLY WORK", width=15, font=("arial", 24)).place(x=40, y=400)

        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Shivam289#",
            database="LEAVE1"
        )
        # f = 16
        my_conn = my_connect.cursor()

        ####### end of connection ####
        querry1 = ("SELECT CLIENT_ID from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (u,))
        T = my_conn.fetchall()
        # if len(T)==0:
        #     tmsg.showwarning("INVALID","NO DATA")
        e1 = Label(root16, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=200)

        querry1 = ("SELECT CLIENT_NAME from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (u,))
        T = my_conn.fetchall()
        e1 = Label(root16, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=250)

        querry1 = ("SELECT CLIENT_DOB from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (u,))
        T = my_conn.fetchall()
        e1 = Label(root16, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=300)
        global j
        querry1 = ("SELECT SALARY from CLIENT WHERE CLIENT_ID=%s")
        my_conn.execute(querry1, (u,))
        T = my_conn.fetchall()

        e1 = Label(root16, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=350)


        # T = my_conn.fetchall()

        e19 = tk.Entry(root16, width=10, font=("arial", 24))
        e19.place(x=400, y=400)

        # querry1 = ("INSERT INTO SALARY1(WORK_HOUR) VALUES(Y) WHERE CLIENT_ID=%s")
        # my_conn.execute(querry1, (u,))

        def entery():
            Y=e19.get()
            print(Y)
            k=int(Y)
            querry3=("SELECT SALARY FROM CLIENT WHERE CLIENT_ID=%s")
            my_conn.execute(querry3,(u,))
            p=my_conn.fetchone()
            print(p)
            print(p[0])
            print(type(p[0]))
            i=p[0]
            if k>0:
                querry2=("UPDATE SALARY1 SET NEW_SALARY=((%s)+(%s)*100) WHERE CLIENT_ID=%s")
                my_conn.execute(querry2,(i,k,u,))
                my_connect.commit()
                querry6 = ("UPDATE SALARY1 SET SALARY_INC=(%s)*100 WHERE CLIENT_ID=%s")
                my_conn.execute(querry6, (k, u,))
                my_connect.commit()
                querry7 = ("UPDATE SALARY1 SET SALARY_DEC=0 WHERE CLIENT_ID=%s")
                my_conn.execute(querry7, (u,))
                my_connect.commit()
                tmsg.showinfo("INSERTED","MONTHLY WORK UPDATED")
                e19.delete(0,END)
            elif k<0:
                querry2 = ("UPDATE SALARY1 SET NEW_SALARY=((%s)+(%s)*100) WHERE CLIENT_ID=%s")
                my_conn.execute(querry2, (i, k, u,))
                my_connect.commit()
                querry4 = ("UPDATE SALARY1 SET SALARY_DEC=(%s)*100 WHERE CLIENT_ID=%s")
                my_conn.execute(querry4, ( k, u,))
                my_connect.commit()
                querry5 = ("UPDATE SALARY1 SET SALARY_INC=0 WHERE CLIENT_ID=%s")
                my_conn.execute(querry5, (u,))
                my_connect.commit()
                tmsg.showinfo("INSERTED", "MONTHLY WORK UPDATED")
                e19.delete(0,END)
            querry1 = ("UPDATE SALARY1 SET WORK_HOUR=%s WHERE CLIENT_ID=%s")
            my_conn.execute(querry1, (Y,u,))
            my_connect.commit()

        # z = int(T)
        # print(z)
        def lauto(y):
            root16.destroy()
            main3(y)
        bu=Button(root16,text="ENTER",fg="#B9770E",font=("arial",19),command=entery).place(x=500,y=450)
        b12 = Button(root16, text="<<BACK", font=("arial", 16), bg="#CA6F1E", command=lambda:lauto(y))
        b12.place(x=1200, y=100)

        root16.mainloop()
    def fetch_client(y):

        canvas23 = Canvas(root2, bg='#95A5A6', width=350, height=300)
        canvas23.place(x=850, y=90)
        l3 = Label(root2, text="Enter Client Id", fg="#34495E", bg="#95A5A6", font=("arial", 19))
        l3.place(x=1000, y=150)
        entry41 = tk.Entry(root2, textvar=address1, width=20, font=("arial", 15, "bold"), bd=5)
        entry41.place(x=960, y=200)

        def client_profile_update(y):
            u=entry41.get()
            my_connect = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Shivam289#",
                database="LEAVE1"
            )
            # f = 16
            my_conn = my_connect.cursor()

            ####### end of connection ####
            querry1 = ("SELECT CLIENT_ID from CLIENT WHERE CLIENT_ID=%s")
            my_conn.execute(querry1, (u,))
            T = my_conn.fetchall()
            if len(T)>0:
                to_update_client_window(u,y)
            else:
                tmsg.showwarning("INVALID","ENTER AGAIN")
                entry41.delete(0,END)


        b12 = Button(root2, text="Search", font=("arial", 16), bg="#CA6F1E", command=lambda :client_profile_update(y))
        b12.place(x=1030, y=250)
        b12 = Button(root2, text="<<BACK", font=("arial", 16), bg="#CA6F1E", command=lambda: htao(y))
        b12.place(x=900, y=250)


        # my_w.mainloop()

    def add_profile():



        root3 = Tk()
        root3.geometry("1600x1000+0+0")
        root3.title("Add Employee")
        root3.configure(bg="#A6ACAF")

        def submit_emp2():
            ID=int(entry1.get())
            print(ID)
            NAME = entry2.get()
            print(NAME)
            DOB1 = entry3.get()
            print(DOB1)
            ADDRESS = entry4.get()
            print(ADDRESS)
            JOIN_D = entry5.get()
            print(JOIN_D)
            SALARY = int(entry6.get())
            print(SALARY)

            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Shivam289#",
                                         db="LEAVE1")
            cursor = db.cursor()

            st=''
            st1=''
            for i in range(4):
                st=st+DOB1[i]
                st1=st1+JOIN_D[i]
            print(st)
            q=int(st)
            r=int(st1)
            flag2=0
            if r>=q+18 and ID>0:
                insert_stmt = (
                    "INSERT INTO CLIENT(CLIENT_ID, CLIENT_NAME,CLIENT_DOB,CLIENT_ADD,JOINING_DATE, SALARY)"
                    "VALUES (%s, %s, %s, %s,%s,%s)"
                )
                # if 2==int(id2):
                #     print("yes")
                data = (ID, NAME, DOB1, ADDRESS, JOIN_D, SALARY)
                cursor.execute(insert_stmt, data)
                db.commit()
                tmsg.showinfo("DATA","DATA INSERTED")
                entry1.delete(0,END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                entry6.delete(0, END)
                flag2=1
            elif r>=q+18 and ID=='':
                insert_stmt = (
                    "INSERT INTO CLIENT( CLIENT_NAME,CLIENT_DOB,CLIENT_ADD,JOINING_DATE, SALARY)"
                    "VALUES ( %s, %s, %s,%s,%s)"
                )
                # if 2==int(id2):
                #     print("yes")
                data = (NAME, DOB1, ADDRESS, JOIN_D, SALARY)
                cursor.execute(insert_stmt, data)
                db.commit()
                flag2 = 1
            else:
                tmsg.showwarning("WRONG DATES","INPUT VALID DATE")
            db1 = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Shivam289#",
                                         db="LEAVE1")
            cursor1 = db1.cursor()

            if flag2==1:
                insert_stmt1 = (
                    "INSERT INTO SALARY1(CLIENT_ID)"
                    "VALUES (%s)"
                )
                # if 2==int(id2):
                #     print("yes")
                data1 = (ID,)
                cursor1.execute(insert_stmt1, data1)
                db1.commit()
                print("working")



        label = Label(root3, text="EMPLOYEE ADD", font=("arial", 25), bg="#5DADE2")
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

        # =entry field

        entry6 = tk.Entry(root3, textvar=salary, width=20, font=("arial", 15, "bold"), bd=5)
        entry6.place(x=500, y=450)

        entry1 = tk.Entry(root3, bd=5, width=20, textvar=id1, font=("arial", 15))
        entry1.place(x=500, y=150)

        entry2 = tk.Entry(root3, bd=5, width=20, textvar=name, font=("arial", 15))
        entry2.place(x=500, y=210)

        # entry3 = Entry(root3, bd=5, width=20, textvar=dob, font=("arial", 15))
        # entry3.place(x=500, y=270)
        # cal = DateEntry(root3, selectmode='day')
        # cal.place(x=500, y=270)
        entry3 = tk.Entry(root3, textvar=dob, width=20, font=("arial", 15, "bold"), bd=5)
        entry3.place(x=500, y=270)
        entry4 = tk.Entry(root3, textvar=address, width=20, font=("arial", 15, "bold"), bd=5)
        entry4.place(x=500, y=330)

        def back56():
            root3.destroy()
            main3(y)

        entry5 = tk.Entry(root3, bd=5, width=20, textvar=join_date, font=("arial", 15))
        entry5.place(x=500, y=390)
        b1 = Button(root3, text="<<BACK", bg="#BA4A00", command=back56, font=("arial", 18)).place(x=1200, y=90)
        b1=Button(root3,text="SUBMIT",bg="#BA4A00",command=submit_emp2,font=("arial",18)).place(x=800,y=600)
        my_pic3 = Image.open("client_add.png")
        re3 = my_pic3.resize((300, 320), Image.ANTIALIAS)
        new_pic3 = ImageTk.PhotoImage(re3)
        l9 = Label(root3, image=new_pic3)
        l9.place(x=900, y=200)
        root3.mainloop()

    s=y


    def admin_profile(s):
        root6 = tk.Tk()
        root6.geometry("1600x1000+0+0")
        root6.title("WELCOME TO ADMIN PROFILE")

        client_label = Label(text="WELCOME TO ADMIN PROFILE", font="Times 20 italic bold", bg="#154360").pack(side=TOP,
                                                                                                            fill=X)
        root6.configure(bg="#1F618D")
        my_pic2 = Image.open("admin_profile.png")
        re2 = my_pic2.resize((300, 320), Image.ANTIALIAS)
        new_pic2 = ImageTk.PhotoImage(re2)
        l1 = Label(root6, image=new_pic2)
        l1.place(x=900, y=200)

        l1 = Label(root6, text="ID", width=15, font=("arial", 24)).place(x=40, y=200)
        l1 = Label(root6, text="NAME", width=15, font=("arial", 24)).place(x=40, y=250)
        l1 = Label(root6, text="D.O.B", width=15, font=("arial", 24)).place(x=40, y=300)
        l1 = Label(root6, text="COMPANY NAME", width=15, font=("arial", 24)).place(x=40, y=350)
        l1 = Label(root6, text="EXPERIENCE YEAR", width=15, font=("arial", 24)).place(x=40, y=400)


        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Shivam289#",
            database="LEAVE1"
        )
        # f = 16
        print(s)
        SUM=s
        my_conn = my_connect.cursor()

        ####### end of connection ####
        querry1 = ("SELECT ADMIN_ID from ADMIN WHERE ADMIN_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Label(root6, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=200)
        querry1 = ("SELECT ADMIN_NAME from ADMIN WHERE ADMIN_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Label(root6, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=250)
        querry1 = ("SELECT ADMIN_DOB from ADMIN WHERE ADMIN_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Label(root6, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=300)

        querry1 = ("SELECT COMPANY_NAME from ADMIN WHERE ADMIN_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Label(root6, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=350)

        querry1 = ("SELECT EXPR_YR from ADMIN WHERE ADMIN_ID=%s")
        my_conn.execute(querry1, (SUM,))
        T = my_conn.fetchall()
        e1 = Label(root6, text=T, width=10, font=("arial", 24))
        e1.place(x=400, y=400)

        def back69():
            root6.destroy()
            main3(y)


        b9 = Button(root6, text='<<BACK', bg='#154360', font=("arial", 20), command=back69).place(x=1200, y=50)
        root6.mainloop()



    f0=Frame(root2, bg="#7F8C8D",pady=3)
    f0.pack(fill=X)
    button1=Button(f0,text="Profile",bg="#F39C12",height=2,width=20,command=lambda:To_admin_profile(y))
    button1.pack(side=LEFT)
    button1=Button(f0,text="Add Employee",bg="#F39C12",height=2,width=20,command=To_add_employee)
    button1.pack(side=LEFT)




    def remove_employee(y):
        canvas23 = Canvas(root2, bg='#7F8C8D', width=350, height=300)
        canvas23.place(x=850,y=90)
        l3=Label(root2,text="Enter Id",fg="#34495E",bg="#7F8C8D",font=("arial",23,"bold"))
        l3.place(x=1000,y=150)
        entry40 = tk.Entry(root2, textvar=address1, width=20, font=("arial", 15, "bold"), bd=5)
        entry40.place(x=960, y=200)
        def delete_emp(y):
            print("working")
            global id34
            id34=int(entry40.get())
            print(id34)
            my_connect1 = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Shivam289#",
                database="LEAVE1"
            )
            # f = 16
            my_conn1 = my_connect1.cursor()

            ####### end of connection ####
            # msg1 = tmsg.askyesno("DELETE PROFILE",
            #                      " ARE YOU SURE")
            querry1 = ("SELECT * from CLIENT WHERE CLIENT_ID=%s")
            my_conn1.execute(querry1, (id34,))
            T = my_conn1.fetchall()

            if len(T)==0:
                tmsg.showwarning("INVLID DATA", "ENTER AGAIN")
                entry40.delete(0,END)

            elif len(T)>0:
                msg1 = tmsg.askyesno("DELETE PROFILE",
                                         " ARE YOU SURE")
                querry1 = ("SELECT * from CLIENT WHERE CLIENT_ID=%s")
                my_conn1.execute(querry1, (id34,))
                T = my_conn1.fetchall()
                for i in T:
                    print(i)
                e1 = Label(root2, text=T, font=("arial", 24))
                e1.place(x=10, y=200)


                if msg1 > 0:
                    e1.destroy()
                    ok(id34)


                else:
                    entry40.delete(0,END)
                    e1.destroy()


        def ok(id34):
            print(id34)
            id35=id34
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Shivam289#",
                                         db="LEAVE1")
            cursor = db.cursor()
            savequery = "DELETE FROM CLIENT WHERE CLIENT_ID=%s"
            cursor.execute(savequery, (id35,))
            db.commit()
            tmsg.showinfo("DELETED","YOUR DATA IS DELETED")
            entry40.delete(0, END)



        # b13 = Button(root2, text="OK", font=("arial", 16), bg="red", command=ok)
        # b13.place(x=900, y=250)
        b12=Button(root2,text="Search",font=("arial",16),bg="#CA6F1E",command=lambda :delete_emp(y))
        b12.place(x=1030,y=250)
        b12 = Button(root2, text="<<BACK", font=("arial", 16), bg="#CA6F1E", command=lambda: htao(y))
        b12.place(x=900, y=250)
    def client_profile2(y):

        search_client(y)
    def log_out(y):
        root2.destroy()
        from tryfinal1 import main
        main()
    def company(y):
        root11 = tk.Tk()
        root11.configure(bg="#82E0AA")
        root11.geometry("1600x1000")
        root11.title("STATUS OF LEAVE")

        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="Shivam289#",
                                     db="LEAVE1")
        cursor = db.cursor()
        savequery = '''select LEAVE_ID,LEAVE_STARTDATE,LEAVE_LASTDATE,LEAVE_MSG,LEAVE_STATUS,CLIENT_ID from LEAVE2 WHERE FLAG=0 '''
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        # savequery1='''select '''

        # Printing the result of the
        # query
        for x in myresult:
            print(x)
        i = 0
        e1=Label(root11,text="LEAVE ID",fg="#0E6655",bg="#82E0AA",font=("arial", 18),width=15)
        e1.grid(row=0,column=0)
        e1 = Label(root11, text="Leave Start Date",fg="#0E6655", bg="#82E0AA",font=("arial", 18),width=15)
        e1.grid(row=0, column=1)
        e1 = Label(root11, text="Leave End Date",fg="#0E6655", bg="#82E0AA", font=("arial", 18),width=15)
        e1.grid(row=0, column=2)
        e1 = Label(root11, text="Leave Msg",fg="#0E6655", bg="#82E0AA", font=("arial", 18),width=15)
        e1.grid(row=0, column=3)
        e1 = Label(root11, text="Leave Status",fg="#0E6655", bg="#82E0AA", font=("arial", 18),width=15)
        e1.grid(row=0, column=4)
        e1 = Label(root11, text="Client Id",fg="#0E6655", bg="#82E0AA", font=("arial", 18),width=15)
        e1.grid(row=0, column=5)
        for student in myresult:
            for j in range(len(student)):
                e = Label(root11,text=student[j], width=15, fg='#D35400', bg="#82E0AA", font=("arial", 18))
                # e.grid(row=i + 100, column=j + 100)
                e.grid(row=i+1 , column=j )
                # e.place(x=i*5+100,y=5*j+100)
                # e.insert(END, student[j])
            i = i + 1
        k=i
        o=200+25*k
        lab = Label(root11, text="STATUS", bg="#117A65",width=70, font=("arial", 26))
        lab.place(x=0,y=o)

        root11.mainloop()
    def company1(y):

        canvas25 = Canvas(root2, bg='#95A5A6', width=350, height=300)
        canvas25.place(x=850, y=90)

        l3 = Label(root2, text="Enter Leave id", fg="#34495E", bg="#95A5A6", font=("arial", 19))
        l3.place(x=1000, y=150)
        entry40 = tk.Entry(root2, textvar=address1, width=20, font=("arial", 15, "bold"), bd=5)
        entry40.place(x=960, y=200)



        def solve(y):
            tr = int(entry40.get())
            entry40.delete(0,END)
            print(tr)
            my_connect = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Shivam289#",
                database="LEAVE1"
            )

            my_conn = my_connect.cursor()
            querry1 = ("SELECT LEAVE_ID from CLIENT,LEAVE2 WHERE CLIENT.CLIENT_ID=LEAVE2.CLIENT_id AND LEAVE_ID=%s")
            my_conn.execute(querry1, (tr,))
            T = my_conn.fetchall()
            # tr leave id

            if len(T)>0:
             root2.destroy()
             solve_issue(tr,y)
            else:
                tmsg.showinfo("INVALID","ENTER AGAIN")
        b12 = Button(root2, text="Search", font=("arial", 16), bg="#CA6F1E", command=lambda :solve(y))
        b12.place(x=1030, y=250)
        b12 = Button(root2, text="<<BACK", font=("arial", 16), bg="#CA6F1E", command=lambda: htao(y))
        b12.place(x=900, y=250)
    global root10
    def back12():
        root10.destroy()
        main3(y)
    def solve_issue(tr,y):
        print(tr)
        print("jhgk")
        root10 = Tk()

        root10.configure(bg="#1ABC9C")
        root10.geometry("1600x1000+0+0")
        root10.title("STATUS")


        admin_label = Label(text="REPORT MAKING", font="Times 20 italic bold", bg="#154360").pack(side=TOP, fill=X)
        name = Label(root10, text="Name", width=20, height=2, bg="pink", fg="blue").place(x=100, y=200)
        name1 = Label(root10, text="Start-Date", width=20, height=2, bg="pink", fg="blue").place(x=100, y=250)
        name2 = Label(root10, text="End-Date", width=20, height=2, bg="pink", fg="blue").place(x=100, y=300)
        name3 = Label(root10, text="Reason", width=20, height=2, bg="pink", fg="blue").place(x=100, y=350)
        report = Label(root10, text="Status", width=20, height=2, bg="pink", fg="blue").place(x=100, y=400)
        msg = Label(root10, text="Message", width=20, height=2, bg="pink", fg="blue").place(x=100, y=450)

        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Shivam289#",
            database="LEAVE1"
        )

        my_conn = my_connect.cursor()




        querry1 = ("SELECT CLIENT_NAME from CLIENT,LEAVE2 WHERE CLIENT.CLIENT_ID=LEAVE2.CLIENT_id AND LEAVE_ID=%s")
        my_conn.execute(querry1, (tr,))
        T = my_conn.fetchall()
        e1 = Label(root10,text=T, width=20, font=("arial", 24))
        # e1.insert(END, T)
        e1.place(x=300, y=200)
        my_conn = my_connect.cursor()
        # querry1 = ("SELECT CLIENT_N from CLIENT WHERE CLIENT_ID=%s")
        # my_conn.execute(querry1, (SUM,))
        # T = my_conn.fetchall()
        querry1 = ("SELECT LEAVE_STARTDATE from CLIENT,LEAVE2 WHERE CLIENT.CLIENT_ID=LEAVE2.CLIENT_id AND LEAVE_ID=%s")
        my_conn.execute(querry1, (tr,))
        T = my_conn.fetchall()
        e1 = Label(root10, text=T, width=20, font=("arial", 24))
        # e1.insert(END, T)
        e1.place(x=300, y=250)
        querry1 = ("SELECT LEAVE_LASTDATE from CLIENT,LEAVE2 WHERE CLIENT.CLIENT_ID=LEAVE2.CLIENT_id AND LEAVE_ID=%s")
        my_conn.execute(querry1, (tr,))
        T = my_conn.fetchall()
        e1 = Label(root10, text=T, width=20, font=("arial", 24))
        # e1.insert(END, T)
        e1.place(x=300, y=300)
        querry1 = ("SELECT LEAVE_MSG from CLIENT,LEAVE2 WHERE CLIENT.CLIENT_ID=LEAVE2.CLIENT_id AND LEAVE_ID=%s")
        my_conn.execute(querry1, (tr,))
        T = my_conn.fetchall()
        e1 = Label(root10, text=T, width=20, font=("arial", 24))
        # e1.insert(END, T)
        e1.place(x=300, y=350)
        global msg1
        global e2
        # e2 = tk.StringVar()
        msg1 = tk.StringVar()


        e99 = tk.Entry(root10, bd=5, width=25, textvar=msg1, font=("arial", 15))
        e99.place(x=300, y=450)

        global radio
        radio = IntVar()

        def back12(y):
            root10.destroy()
            main3(y)

        def yes(tr):
            if radio.get() == 1:
                print("yes")
                # submit_report(tr,y)

            else:
                print("no")

        R1 = Radiobutton(root10, text="YES", variable=radio, value=1, command=lambda:yes(tr))
        R1.place(x=300, y=400)

        R2 = Radiobutton(root10, text="NO", variable=radio, value=2, command=lambda:yes(tr))
        R2.place(x=400, y=400)

        def submit_report(tr,y):
            l=radio.get()
            if l==1:
                k="YES"
            else:
                k="NO"
            print("ho gya")
            # print(k)
            print(tr)
            h=e99.get()
            print(h)
            # print(T(0))
            querry2 = '''UPDATE LEAVE2 SET LEAVE_STATUS=%s WHERE LEAVE_ID=%s'''
            my_conn.execute(querry2, (k,tr,))
            my_connect.commit()
            querry0 = '''UPDATE LEAVE2 SET FLAG=1 WHERE LEAVE_ID=%s'''
            my_conn.execute(querry0,(tr,))
            my_connect.commit()
            print(l,h,y,tr)
            querry9="SELECT CLIENT_ID FROM LEAVE2 WHERE LEAVE_ID=%s"
            my_conn.execute(querry9, (tr,))
            tr1=my_conn.fetchone()
            print(tr1)
            print(tr1[0])
            if len(tr1)>0:

                querry3= '''INSERT INTO REPORT(REPORT_STATUS,REPORT_MSG,ADMIN_ID,CLIENT_ID) VALUES(%s,%s,%s,%s)'''
                my_conn.execute(querry3, (k,h,y,tr1[0]))
                my_connect.commit()
                print("fjsdnkl")

            else:
                tmsg.showwarning("INVALID","INVALID INFO")

        b1 = Button(root10, text="SUBMIT", font="aerial,19", width=10, command=lambda:submit_report(tr,y), bg="#BA4A00").place(x=600,
                                                                                                                y=550)
        b1 = Button(root10, text="<<BACK", font="aerial,19", width=10, command=lambda :back12(y),
                    bg="#BA4A00").place(x=1200,
                                        y=80)
        root10.mainloop()

    button1=Button(f0,text="Remove Employee",bg="#F39C12",height=2,width=20,command=lambda :remove_employee(y))
    button1.pack(side=LEFT)
    button1=Button(f0,text="See Client Profile",bg="#F39C12",height=2,width=20,command=lambda :client_profile2(y))
    button1.pack(side=LEFT)
    button1=Button(f0,text="Extract Leave Request",bg="#F39C12",height=2,width=20,command=lambda :company(y))
    button1.pack(side=LEFT)
    button1=Button(f0,text="Report Making",bg="#F39C12",height=2,width=20,command=lambda :company1(y))
    button1.pack(side=LEFT)
    button1=Button(f0,text="Log out",bg="#F39C12",height=2,width=20,command=lambda :log_out(y))
    button1.pack(side=RIGHT)


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
    text_var="WELCOME TO <<ADMIN>> PAGE"
    text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',50,'bold'),fill='#F7DC6F',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width']=width
    canvas['height']=height
    fps=100   #Change the fps to make the animation faster/slower
    shift()

    root2.mainloop()
# main3(1)