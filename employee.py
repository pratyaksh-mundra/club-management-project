# region import files
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
import sys
import datetime
from tkinter import ttk
import tkinter as tk
# endregion

employee = Tk()
con = sqlite3.connect("identifier.sqlite")
employee.configure(bg='#293241')
employee.title("employee view")
employee.geometry("1600x900")
def write_to_csv_attend(records):
    with open('activities.csv','a') as f:
        w=csv.writer(f, dialect='excel')
        w.writerow(records)
def insert_attendance():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    mycur.execute("insert into membership values (:mem_no,:mem_type,:main_member,:exp_Date,:address)",
                  {
                      'date': now.strftime('%Y-%m-%d %H:%M:%S'),
                      'mem_no': date_field.get(),
                      'act_name': act_name_field.get(),
                      'name': name_field.get(),
                      'f_no': f_no_field.get(),
                      'a_no': a_no_field.get(),
                      'eid': eid_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()

    date_field.delete(0, END)
    act_name_field.delete(0, END)
    name_field.delete(0, END)
    f_no_field.delete(0, END)
    a_no_field.delete(0, END)
    eid_field.delete(0, END)

top = Label(employee, text="ATTENDANCE", fg="#E0FBFC",bg="#EE6C4D", font="verdana 24 bold").grid(row=0, column=1)
date = Label(employee, text="DATE:", fg="#EE6C4D", bg="#98c1d9")
mem_no = Label(employee, text="MEM_NO:" , fg="#EE6C4D", bg="#98c1d9")
act_name = Label(employee, text="ACTIVITY NAME:" , fg="#EE6C4D", bg="#98c1d9")
name = Label(employee, text="NAME:", fg="#EE6C4D", bg="#98c1d9")
f_no = Label(employee, text="F_NO.:", fg="#EE6C4D", bg="#98c1d9")
a_no = Label(employee, text="ACTIVITY NO:", fg="#EE6C4D", bg="#98c1d9")
eid = Label(employee, text="EMPLOYEE ID:", fg="#EE6C4D", bg="#98c1d9")


date.grid(row=1, column=0)
mem_no.grid(row=2, column=0)
act_name.grid(row=3, column=0)
name.grid(row=4, column=0)
f_no.grid(row=5, column=0)
a_no.grid(row=6, column=0)
eid.grid(row=7, column=0)


date_field = Entry(employee,bg="#e0fbfc")
mem_no_field = Entry(employee,bg="#e0fbfc")
act_name_field = Entry(employee,bg="#e0fbfc")
name_field = Entry(employee,bg="#e0fbfc")
f_no_field = Entry(employee,bg="#e0fbfc")
a_no_field = Entry(employee,bg="#e0fbfc")
eid_field = Entry(employee,bg="#e0fbfc")

date_field.grid(row=1, column=1, ipadx="100",)
mem_no_field.grid(row=2, column=1, ipadx="100")
act_name_field.grid(row=3, column=1, ipadx="100")
name_field.grid(row=4, column=1, ipadx="100")
f_no_field.grid(row=5, column=1, ipadx="100")
a_no_field.grid(row=6, column=1, ipadx="100")
eid_field.grid(row=7, column=1, ipadx="100")



employee.mainloop()