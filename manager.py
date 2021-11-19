from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
from tkinter import ttk

import tkinter as tk

manager = Tk()
con = sqlite3.connect("identifier.sqlite")
manager.configure(bg='yellow')
manager.title("manager view")
manager.geometry("1600x900")


def insert():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()


    mycur.execute("insert into membership values (:mem_no,:mem_type,:main_member,:exp_Date,:address)",
                      {
                          'mem_no': mem_no_field.get(),
                          'mem_type': mem_type_field.get(),
                          'main_member': main_member_field.get(),
                          'exp_Date': exp_Date_field.get(),
                          'address': address_field.get()
                      })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()
    mem_no.delete(0, END)
    mem_type.delete(0, END)
    main_member.delete(0, END)
    exp_Date.delete(0, END)
    address.delete(0, END)
def insert_employee():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()


    mycur.execute("insert into employee values (:designation,:salary,:mid,:name)",
                      {

                          'designation': exp_Date_field.get(),
                          'salary': address_field.get(),
                          'mid': address_field.get(),
                          'name': address_field.get()
                      })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()
    designation.delete(0, END)
    salary.delete(0, END)
    mid.delete(0, END)
def display():

    display_mem=Toplevel(manager)
    display_mem.title("display")
    lab = Label(display_mem, text="mem_no|mem_type|main_member|exp_date|address")
    lab.grid(row=0,column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from membership")
    records= curr.fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records += str(record)+ "\n"
    query_label=Label(display_mem,text=print_records)
    query_label.grid(row=1,column=0,columnspan=2)
    curr.close()


top = Label(manager, text="NEW MEMBERS", bg="red", font="verdana 30 bold").grid(row=0, column=1)
mem_no = Label(manager, text="ID:")
mem_type = Label(manager, text="MEM TYPE:")
main_member = Label(manager, text="NAME:")
exp_Date = Label(manager, text="EXP DATE:")
address = Label(manager, text="ADDRESS:")

#grid formating
mem_no.grid(row=1, column=0)
mem_type.grid(row=2, column=0)
main_member.grid(row=3, column=0)
exp_Date.grid(row=4, column=0)
address.grid(row=5, column=0)


mem_no_field = Entry(manager)
mem_type_field = Entry(manager)
main_member_field = Entry(manager)
exp_Date_field = Entry(manager)
address_field = Entry(manager)

#grid formating
mem_no_field.grid(row=1, column=1, ipadx="100")
mem_type_field.grid(row=2, column=1, ipadx="100")
main_member_field.grid(row=3, column=1, ipadx="100")
exp_Date_field.grid(row=4, column=1, ipadx="100")
address_field.grid(row=5, column=1, ipadx="100")


b1 = Button(manager, text="INSERT", font="30", fg="red", bg="blue", width="20", command=insert).grid(row=9, column=1)
b2=Button(manager,text="DISPLAY",font="30",fg="red",bg="blue",width="20",command=display).grid(row=10,column=1)
#b3=Button(manager,text="DELETE",font="30",fg="red",bg="blue",command=delete).grid(row=11,column=2)

#employee

top1 = Label(manager, text="EMPLOYEE", bg="red", font="verdana 30 bold").grid(row=11, column=1)
designation = Label(manager, text="DESIGNATION:")
salary = Label(manager, text="SALARY:")
mid = Label(manager, text="MID:")
name = Label(manager, text="NAME:")


#grid formating
designation.grid(row=12, column=0)
salary.grid(row=13, column=0)
mid.grid(row=14, column=0)
name.grid(row=15, column=0)



designation_field = Entry(manager)
salary_field = Entry(manager)
mid_field = Entry(manager)
name_field = Entry(manager)


#grid formating
designation_field.grid(row=12, column=1, ipadx="100")
salary_field.grid(row=13, column=1, ipadx="100")
mid_field.grid(row=14, column=1, ipadx="100")
name_field.grid(row=15, column=1, ipadx="100")


manager.mainloop()
