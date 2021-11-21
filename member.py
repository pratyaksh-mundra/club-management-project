from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
import sys
import datetime
from tkinter import ttk
import tkinter as tk

member = Tk()
con = sqlite3.connect("identifier.sqlite")
member.configure(bg='#293241')
member.title("member view")
member.geometry("1600x900")

def display_activities():
    display_act = Toplevel(member)
    display_act.title("display")
    lab = Label(display_act, text="a_no|name|cost")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from activities")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_act, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)
    curr.close()

def display_mp():

    display_main=Toplevel(member)
    display_main.title("display")
    lab = Label(display_main, text="pid|mem_no|pay_date|name|amount|employee id|manager id")
    lab.grid(row=0, column=0)
    pid1 = pid_field.get()
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from main_payments where pid="+str(pid1))
    records= curr.fetchall()
    #print(records)
    print_records = ''
    for record in records:
        print_records += str(record)+ "\n"
    query_label = Label(display_main,text=print_records)
    query_label.grid(row=1,column=0,columnspan=2)
    curr.close()

def display_fam():
    display_main = Toplevel(member)
    display_main.title("display")
    mem=mem_no_dis_field.get()
    lab = Label(display_main, text="f_no|mem_no|name|birthday|anniversaries")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from family where mem_no="+str(mem))
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
        query_label = Label(display_main, text=print_records)
        query_label.grid(row=1, column=0, columnspan=2)
    curr.close()

# region activities
top = Label(member, text="VIEW ACTIVITIES", fg="#E0FBFC", bg="#EE6C4D", font="verdana 12 bold").grid(row=13, column=1)
b2=Button(member,text="DISPLAY",font="30", fg="#EE6C4D", bg="#98c1d9",width="20",command=display_activities).grid(row=14,column=1)
empty=Label(member,text="",bg='#293241').grid(row=15,column=1)
# endregion



# region PAYMENTS
top = Label(member, text="PAYMENTS", fg="#E0FBFC", bg="#EE6C4D", font="verdana 12 bold").grid(row=16, column=1)
pid = Label(member, text="PLEASE ENTER PID: ",fg="#EE6C4D", bg="#98c1d9")
pid.grid(row=17, column=0)
pid_field = Entry(member,bg="#e0fbfc")
pid_field.grid(row=17, column=1, ipadx="100")

b2=Button(member,text="DISPLAY",font="30", fg="#EE6C4D", bg="#98c1d9",width="20",command=display_mp).grid(row=24,column=1)
empty=Label(member,text="",bg='#293241').grid(row=25,column=1)
# endregion

top = Label(member, text="FAMILY", fg="#E0FBFC", bg="#EE6C4D", font="verdana 12 bold").grid(row=26, column=1)
mem_no_dis = Label(member, text="ENTER MEM NO :",fg="#EE6C4D", bg="#98c1d9")
mem_no_dis.grid(row=27, column=0 )
mem_no_dis_field = Entry(member,bg="#e0fbfc")
mem_no_dis_field.grid(row=27, column=1, ipadx="100")

b2 = Button(member, text="DISPLAY", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=display_fam).grid(row=28,column=1)
member.mainloop()