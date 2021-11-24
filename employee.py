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
employee.configure
employee.title("employee view")
employee.geometry("1600x900")
employee.tk.call("source", "azure.tcl")
employee.tk.call("set_theme", "dark")
def time_so():
    a = datetime.datetime.now()
    return a

def write_to_csv_attend(records):
    with open('activities.csv','a') as f:
        w=csv.writer(f, dialect='excel')
        w.writerow(records)
def write_to_csv_mp(records):
    with open('activities.csv','a') as f:
        w=csv.writer(f, dialect='excel')
        w.writerow(records)
def write_to_csv_act(records):
    with open('activities.csv','a') as f:
        w=csv.writer(f, dialect='excel')
        w.writerow(records)
def insert_attendance():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()
    time_now=time_so()
    mycur.execute("insert into attendance values (:date,:mem_no,:act_name,:name,:f_no,:a_no,:eid)",
                  {
                      'date': time_now,
                      'mem_no': mem_no_field.get(),
                      'act_name': act_name_field.get(),
                      'name': name_field.get(),
                      'f_no': f_no_field.get(),
                      'a_no': a_no_field.get(),
                      'eid': eid_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()


    act_name_field.delete(0, END)
    name_field.delete(0, END)
    f_no_field.delete(0, END)
    a_no_field.delete(0, END)
    eid_field.delete(0, END)
def display_attendance():
    display_attend = Toplevel(employee)
    display_attend.title("display")
    date1 = date1_field.get()
    lab = Label(display_attend, text="date|mem_no|act_name|name|f_no|a_no|eid")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from attendance where date=" + str(date1))
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_attend, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)
    export_btn = ttk.Button(display_attend, text="export to CSV", command=lambda: write_to_csv_attend(records))

    export_btn.grid(row=200, column=0)
    curr.close()

def display_activities():
    display_act = Toplevel(employee)
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
    export_btn = ttk.Button(display_act, text="export to CSV", command=lambda: write_to_csv_act(records))
    export_btn.grid(row=200, column=0)
    curr.close()
# region main_payments functions
def insert_mp():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()


    mycur.execute("insert into main_payments values (:pid,:mem_no,:pay_date,:name,:amount,:eid,:mid)",
                      {
                          'pid': None,
                          'mem_no': mem_no_field.get(),
                          'pay_date': pay_date_field.get(),
                          'name': name_field.get(),
                          'amount': amount_field.get(),
                          'eid': eid_field.get(),
                          'mid': mid_field.get()
                      })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()

    mem_no_field.delete(0, END)
    pay_date_field.delete(0, END)
    name_field.delete(0, END)
    amount_field.delete(0, END)
    eid_field.delete(0, END)
    mid_field.delete(0, END)
def display_mp():

    display_main=Toplevel(employee)
    display_main.title("display")
    lab = Label(display_main, text="pid|mem_no|pay_date|name|amount|employee id|manager id")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from main_payments")
    records= curr.fetchall()
    #print(records)
    print_records = ''
    for record in records:
        print_records += str(record)+ "\n"
    query_label = Label(display_main,text=print_records)
    query_label.grid(row=1,column=0,columnspan=2)
    export_btn = ttk.Button(display_main, text="export to CSV",command=lambda: write_to_csv_mp(records))


    export_btn.grid(row=200,column=0)
    curr.close()
def delete_mp():
    con = sqlite3.connect("identifier.sqlite")
    pid1 = pid_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from main_payments where pid="+str(pid1))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()
def display_mp_pid():
    display_main = Toplevel(employee)
    display_main.title("display")
    lab = Label(display_main, text="pid|mem_no|pay_date|name|amount|employee id|manager id")
    lab.grid(row=0, column=0)
    pid1 = pid_field.get()
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from main_payments where pid=" + str(pid1))
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
        query_label = Label(display_main, text=print_records)
        query_label.grid(row=1, column=0, columnspan=2)
    curr.close()
# endregion

# region attendance portion
top = Label(employee, text="ATTENDANCE").grid(row=0, column=1)
#date = Label(employee, text="DATE:",)
mem_no = Label(employee, text="MEM_NO:" ,)
act_name = Label(employee, text="ACTIVITY NAME:" ,)
name = Label(employee, text="NAME:",)
f_no = Label(employee, text="F_NO.:",)
a_no = Label(employee, text="ACTIVITY NO:",)
eid = Label(employee, text="EMPLOYEE ID:",)


#date.grid(row=1, column=0)
mem_no.grid(row=2, column=0)
act_name.grid(row=3, column=0)
name.grid(row=4, column=0)
f_no.grid(row=5, column=0)
a_no.grid(row=6, column=0)
eid.grid(row=7, column=0)


#date_field = Entry(employee)
mem_no_field = Entry(employee)
act_name_field = Entry(employee)
name_field = Entry(employee)
f_no_field = Entry(employee)
a_no_field = Entry(employee)
eid_field = Entry(employee)

#date_field.grid(row=1, column=1, ipadx="100",)
mem_no_field.grid(row=2, column=1, ipadx="100")
act_name_field.grid(row=3, column=1, ipadx="100")
name_field.grid(row=4, column=1, ipadx="100")
f_no_field.grid(row=5, column=1, ipadx="100")
a_no_field.grid(row=6, column=1, ipadx="100")
eid_field.grid(row=7, column=1, ipadx="100")

b1 = ttk.Button(employee, text="INSERT",  command=insert_attendance).grid(row=8, column=1)
# endregion



# region attendance section search
top = Label(employee, text="attendance").grid(row=9, column=1)
date1 = Label(employee, text="ENTER DATE:").grid(row=10, column=0)
date1_field = Entry(employee)
date1_field.grid(row=10,column=1,ipadx="100")
b3 = ttk.Button(employee, text="DISPLAY",  command=display_attendance).grid(row=11,column=1)
empty=Label(employee,text="").grid(row=12,column=1)
# endregion

# region display activities
top = Label(employee, text="VIEW ACTIVITIES").grid(row=13, column=1)
b2=ttk.Button(employee,text="DISPLAY",command=display_activities).grid(row=14,column=1)
empty=Label(employee,text="").grid(row=15,column=1)



# endregion

# region add remove main_payments
top = Label(employee, text="PAYMENTS").grid(row=16, column=1)
mem_no = Label(employee, text="MEMBER NO.: ")
pay_date = Label(employee, text="PAYMENT DATE: ")
name = Label(employee, text="NAME:")
amount = Label(employee, text="AMOUNT:")
eid = Label(employee, text="EMPLOYEE ID:")
mid = Label(employee, text="MANAGER_ID:")


#grid formating
mem_no.grid(row=17, column=0)
pay_date.grid(row=18, column=0)
name.grid(row=19, column=0)
amount.grid(row=20, column=0)
eid.grid(row=21, column=0)
mid.grid(row=22, column=0)



mem_no_field = Entry(employee)
pay_date_field = Entry(employee)
name_field = Entry(employee)
amount_field = Entry(employee)
eid_field = Entry(employee)
mid_field = Entry(employee)


#grid formating
mem_no_field.grid(row=17, column=1, ipadx="100")
pay_date_field.grid(row=18, column=1, ipadx="100")
name_field.grid(row=19, column=1, ipadx="100")
amount_field.grid(row=20, column=1, ipadx="100")
eid_field.grid(row=21, column=1, ipadx="100")
mid_field.grid(row=22, column=1, ipadx="100")




b1 = ttk.Button(employee, text="INSERT",  command=insert_mp).grid(row=23, column=1)
b2=ttk.Button(employee,text="DISPLAY ALL",command=display_mp).grid(row=24,column=1)
empty=Label(employee,text="").grid(row=25,column=1)

pid = Label(employee, text="DELETE PAYMENTS:").grid(row=26, column=0)
pid_field = Entry(employee)
pid_field.grid(row=26,column=1,ipadx="100")
b3 = ttk.Button(employee, text="DELETE", command=delete_mp).grid(row=27,column=1)

pid = Label(employee, text="PLEASE ENTER PID: ")
pid.grid(row=30, column=0)
pid_field = Entry(employee)
pid_field.grid(row=30, column=1, ipadx="100")

b4=ttk.Button(employee,text="DISPLAY",command=display_mp_pid).grid(row=31,column=1)
empty=Label(employee,text="").grid(row=32,column=1)
# endregion



employee.mainloop()