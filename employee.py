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
    export_btn = Button(display_attend, text="export to CSV", command=lambda: write_to_csv_attend(records))

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
    export_btn = Button(display_act, text="export to CSV", command=lambda: write_to_csv_act(records))
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
    export_btn = Button(display_main, text="export to CSV",command=lambda: write_to_csv_mp(records))


    export_btn.grid(row=200,column=0)
    curr.close()
def delete_mp():
    pid1 = pid_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from main_payments where pid="+str(pid1))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()
# endregion

# region attendance portion
top = Label(employee, text="ATTENDANCE", fg="#E0FBFC",bg="#EE6C4D", font="verdana 24 bold").grid(row=0, column=1)
#date = Label(employee, text="DATE:", fg="#EE6C4D", bg="#98c1d9")
mem_no = Label(employee, text="MEM_NO:" , fg="#EE6C4D", bg="#98c1d9")
act_name = Label(employee, text="ACTIVITY NAME:" , fg="#EE6C4D", bg="#98c1d9")
name = Label(employee, text="NAME:", fg="#EE6C4D", bg="#98c1d9")
f_no = Label(employee, text="F_NO.:", fg="#EE6C4D", bg="#98c1d9")
a_no = Label(employee, text="ACTIVITY NO:", fg="#EE6C4D", bg="#98c1d9")
eid = Label(employee, text="EMPLOYEE ID:", fg="#EE6C4D", bg="#98c1d9")


#date.grid(row=1, column=0)
mem_no.grid(row=2, column=0)
act_name.grid(row=3, column=0)
name.grid(row=4, column=0)
f_no.grid(row=5, column=0)
a_no.grid(row=6, column=0)
eid.grid(row=7, column=0)


#date_field = Entry(employee,bg="#e0fbfc")
mem_no_field = Entry(employee,bg="#e0fbfc")
act_name_field = Entry(employee,bg="#e0fbfc")
name_field = Entry(employee,bg="#e0fbfc")
f_no_field = Entry(employee,bg="#e0fbfc")
a_no_field = Entry(employee,bg="#e0fbfc")
eid_field = Entry(employee,bg="#e0fbfc")

#date_field.grid(row=1, column=1, ipadx="100",)
mem_no_field.grid(row=2, column=1, ipadx="100")
act_name_field.grid(row=3, column=1, ipadx="100")
name_field.grid(row=4, column=1, ipadx="100")
f_no_field.grid(row=5, column=1, ipadx="100")
a_no_field.grid(row=6, column=1, ipadx="100")
eid_field.grid(row=7, column=1, ipadx="100")

b1 = Button(employee, text="INSERT", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=insert_attendance).grid(row=8, column=1)
# endregion



# region attendance section search
top = Label(employee, text="attendance", fg="#E0FBFC",bg="#EE6C4D", font="verdana 12 bold").grid(row=9, column=1)
date1 = Label(employee, text="ENTER DATE:",fg="#EE6C4D", bg="#98c1d9").grid(row=10, column=0)
date1_field = Entry(employee,bg="#e0fbfc")
date1_field.grid(row=10,column=1,ipadx="100")
b3 = Button(employee, text="DISPLAY", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=display_attendance).grid(row=11,column=1)
empty=Label(employee,text="",bg='#293241').grid(row=12,column=1)
# endregion

# region display activities
top = Label(employee, text="VIEW ACTIVITIES", fg="#E0FBFC", bg="#EE6C4D", font="verdana 12 bold").grid(row=13, column=1)
b2=Button(employee,text="DISPLAY",font="30", fg="#EE6C4D", bg="#98c1d9",width="20",command=display_activities).grid(row=14,column=1)
empty=Label(employee,text="",bg='#293241').grid(row=15,column=1)



# endregion

# region add remove main_payments
top = Label(employee, text="PAYMENTS", fg="#E0FBFC", bg="#EE6C4D", font="verdana 12 bold").grid(row=16, column=1)
mem_no = Label(employee, text="MEMBER NO.: ",fg="#EE6C4D", bg="#98c1d9")
pay_date = Label(employee, text="PAYMENT DATE: ",fg="#EE6C4D", bg="#98c1d9")
name = Label(employee, text="NAME:",fg="#EE6C4D", bg="#98c1d9")
amount = Label(employee, text="AMOUNT:",fg="#EE6C4D", bg="#98c1d9")
eid = Label(employee, text="EMPLOYEE ID:",fg="#EE6C4D", bg="#98c1d9")
mid = Label(employee, text="MANAGER_ID:",fg="#EE6C4D", bg="#98c1d9")


#grid formating
mem_no.grid(row=17, column=0)
pay_date.grid(row=18, column=0)
name.grid(row=19, column=0)
amount.grid(row=20, column=0)
eid.grid(row=21, column=0)
mid.grid(row=22, column=0)



mem_no_field = Entry(employee,bg="#e0fbfc")
pay_date_field = Entry(employee,bg="#e0fbfc")
name_field = Entry(employee,bg="#e0fbfc")
amount_field = Entry(employee,bg="#e0fbfc")
eid_field = Entry(employee,bg="#e0fbfc")
mid_field = Entry(employee,bg="#e0fbfc")


#grid formating
mem_no_field.grid(row=17, column=1, ipadx="100")
pay_date_field.grid(row=18, column=1, ipadx="100")
name_field.grid(row=19, column=1, ipadx="100")
amount_field.grid(row=20, column=1, ipadx="100")
eid_field.grid(row=21, column=1, ipadx="100")
mid_field.grid(row=22, column=1, ipadx="100")




b1 = Button(employee, text="INSERT", font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=insert_mp).grid(row=23, column=1)
b2=Button(employee,text="DISPLAY",font="30", fg="#EE6C4D", bg="#98c1d9",width="20",command=display_mp).grid(row=24,column=1)
empty=Label(employee,text="",bg='#293241').grid(row=25,column=1)

pid = Label(employee, text="DELETE PAYMENTS:",fg="#EE6C4D", bg="#98c1d9").grid(row=26, column=0)
pid_field = Entry(employee,bg="#e0fbfc")
pid_field.grid(row=26,column=1,ipadx="100")
b3 = Button(employee, text="DELETE",font="30", fg="#EE6C4D", bg="#98c1d9",width="20", command=delete_mp).grid(row=27,column=1)
empty=Label(employee, bg='#293241').grid(row=28, column=1)

# endregion



employee.mainloop()