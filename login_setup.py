from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
from tkinter import ttk
import tkinter as tk
import  os

login_setup = Tk()
con = sqlite3.connect("identifier.sqlite")
login_setup.configure(bg='#293241')
login_setup.title("login setup")
login_setup.geometry("1600x900")


# region membership functions
def insert():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()

    mycur.execute("insert into manager_login values (:mcred_id,:m_username,:m_password)",
                  {
                      'mcred_id': None,
                      'm_username': username_field.get(),
                      'm_password': password_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()

    username_field.delete(0, END)
    password_field.delete(0, END)


def display_manager():
    display_mem = Toplevel(login_setup)
    display_mem.title("display")
    lab = Label(display_mem, text="mcred_id|username|password")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from manager_login")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_mem, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)

    curr.close()


def delete_manager():
    mem_id = mcred_id_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from manager_login where mcred_id=" + str(mem_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

# region employee functions
def insert_employee():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()

    mycur.execute("insert into employee_login values (:ecred_id,:e_username,:e_password)",
                  {
                      'ecred_id': None,
                      'e_username': username_field.get(),
                      'e_password': password_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()

    username_field.delete(0, END)
    password_field.delete(0, END)


def display_employee():
    display_mem = Toplevel(login_setup)
    display_mem.title("display")
    lab = Label(display_mem, text="ecred_id|e_username|e_password")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from employee_login")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_mem, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)

    curr.close()


def delete_employee():
    ecred_id_s = ecred_id_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from employee_login where ecred_id=" + str(ecred_id_s))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

# region member functions
def insert_member():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()

    mycur.execute("insert into member_login values (:memcred_id,mem_username,:mem_password)",
                  {
                      'memcred_id': None,
                      'mem_username': mem_username_field.get(),
                      'mem_password': mem_password_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()

    username_field.delete(0, END)
    password_field.delete(0, END)


def display_member():
    display_mem = Toplevel(login_setup)
    display_mem.title("display")
    lab = Label(display_mem, text="memcred_id|mem_username|mem_password")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from member_login")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_mem, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)

    curr.close()


def delete_member():
    mem_cred_id_s = memcred_id_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from member_login where memcred_id=" + str(mem_cred_id_s))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

# region MANAGER CREDS
top = Label(login_setup, text="MANAGER LOGIN", fg="#E0FBFC", bg="#EE6C4D", font="verdana 16 bold").grid(row=0, column=1)

username = Label(login_setup, text="USERNAME:",fg="#EE6C4D", bg="#98c1d9")
password = Label(login_setup, text="PASSWORD:",fg="#EE6C4D", bg="#98c1d9")


# grid formating

username.grid(row=1, column=0)
password.grid(row=2, column=0)

username_field = Entry(login_setup)
password_field = Entry(login_setup)


# grid formating

username_field.grid(row=1, column=1, ipadx="100")
password_field.grid(row=2, column=1, ipadx="100")


b1 = Button(login_setup, text="INSERT CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=insert).grid(row=3,
                                                                                                          column=1)
b2 = Button(login_setup, text="DISPLAY CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=display_manager).grid(
    row=4, column=1)
# empty=Label(manager,bg="#EDDFEF").grid(row=7,column=0)
mcred_id = Label(login_setup, text="ID:")
mcred_id.grid(row=5, column=0)
mcred_id_field = Entry(login_setup)
mcred_id_field.grid(row=5, column=1, ipadx="100")

b3 = Button(login_setup, text="DELETE CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=delete_manager).grid(
    row=6, column=1)
empty = Label(login_setup, bg="#293241").grid(row=7, column=0)
# endregion

# region EMPLOYEE CREDS
top = Label(login_setup, text="EMPLOYEE LOGIN", fg="#E0FBFC", bg="#EE6C4D", font="verdana 16 bold").grid(row=8, column=1)

e_username = Label(login_setup, text="USERNAME:",fg="#EE6C4D", bg="#98c1d9")
e_password = Label(login_setup, text="PASSWORD:",fg="#EE6C4D", bg="#98c1d9")


# grid formating

e_username.grid(row=9, column=0)
e_password.grid(row=10, column=0)

e_username_field = Entry(login_setup)
e_password_field = Entry(login_setup)


# grid formating

e_username_field.grid(row=9, column=1, ipadx="100")
e_password_field.grid(row=10, column=1, ipadx="100")


b1 = Button(login_setup, text="INSERT CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=insert_employee).grid(row=11,
                                                                                                          column=1)
b2 = Button(login_setup, text="DISPLAY CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=display_employee).grid(
    row=12, column=1)
# empty=Label(manager,bg="#EDDFEF").grid(row=7,column=0)
ecred_id = Label(login_setup, text="ID:")
ecred_id.grid(row=13, column=0)
ecred_id_field = Entry(login_setup)
ecred_id_field.grid(row=13, column=1, ipadx="100")

b3 = Button(login_setup, text="DELETE CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=delete_employee).grid(
    row=14, column=1)
empty = Label(login_setup, bg="#293241").grid(row=15, column=0)
# endregion

# region member CREDS
top = Label(login_setup, text="MEMBER LOGIN", fg="#E0FBFC", bg="#EE6C4D", font="verdana 16 bold").grid(row=16, column=1)

mem_username = Label(login_setup, text="USERNAME:",fg="#EE6C4D", bg="#98c1d9")
mem_password = Label(login_setup, text="PASSWORD:",fg="#EE6C4D", bg="#98c1d9")


# grid formating

mem_username.grid(row=17, column=0)
mem_password.grid(row=18, column=0)

mem_username_field = Entry(login_setup)
mem_password_field = Entry(login_setup)


# grid formating

mem_username_field.grid(row=17, column=1, ipadx="100")
mem_password_field.grid(row=18, column=1, ipadx="100")


b1 = Button(login_setup, text="INSERT CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=insert_member).grid(row=19,
                                                                                                          column=1)
b2 = Button(login_setup, text="DISPLAY CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=display_member).grid(
    row=20, column=1)
# empty=Label(manager,bg="#EDDFEF").grid(row=7,column=0)
memcred_id = Label(login_setup, text="ID:")
memcred_id.grid(row=21, column=0)
memcred_id_field = Entry(login_setup)
memcred_id_field.grid(row=21, column=1, ipadx="100")

b3 = Button(login_setup, text="DELETE CREDENTIALS", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=delete_member).grid(
    row=22, column=1)
empty = Label(login_setup, bg="#293241").grid(row=23, column=0)
# endregion

login_setup.mainloop()