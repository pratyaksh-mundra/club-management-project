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
    lab = Label(display_mem, text="mem_no|mem_type|main_member|exp_date|address")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from membership")
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
    cur2.execute("delete from membership where mem_no=" + str(mem_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

# region membership functions
def insert_employee():
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


def display_employee():
    display_mem = Toplevel(login_setup)
    display_mem.title("display")
    lab = Label(display_mem, text="mem_no|mem_type|main_member|exp_date|address")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from membership")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_mem, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)

    curr.close()


def delete_employee():
    mem_id = mcred_id_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from membership where mem_no=" + str(mem_id))
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

# region MANAGER CREDS
top = Label(login_setup, text="EMPLOYEE LOGIN", fg="#E0FBFC", bg="#EE6C4D", font="verdana 16 bold").grid(row=8, column=1)

e_username = Label(login_setup, text="USERNAME:",fg="#EE6C4D", bg="#98c1d9")
e_password = Label(login_setup, text="PASSWORD:",fg="#EE6C4D", bg="#98c1d9")


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

login_setup.mainloop()