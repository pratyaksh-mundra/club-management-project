# region import files
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
from tkinter import ttk
import tkinter as tk
# endregion

manager = Tk()
con = sqlite3.connect("identifier.sqlite")
manager.configure(bg='#EDDFEF')
manager.title("manager view")
manager.geometry("1600x900")

def write_to_csv(records):
    with open('membership.csv','a') as f:
        w=csv.writer(f, dialect='excel')
        w.writerow(records)

def insert()
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
    mem_no_field.delete(0, END)
    mem_type_field.delete(0, END)
    main_member_field.delete(0, END)
    exp_Date_field.delete(0, END)
    address_field.delete(0, END)

def insert_employee():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()


    mycur.execute("insert into employee values (:eid,:designation,:salary,:mid,:name)",
                      {
                          'eid': None,
                          'designation': designation_field.get(),
                          'salary': salary_field.get(),
                          'mid': mid_field.get(),
                          'name': name_field.get()
                      })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()
    designation_field.delete(0, END)
    salary_field.delete(0, END)
    mid_field.delete(0, END)
    name_field.delete(0, END)

def display_membership():

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
    export_btn=Button(display_mem, text="export to CSV",command=lambda: write_to_csv(records))
    export_btn.grid(row=200,column=0)
    curr.close()

def delete_membership():
    mem_id=mem_no_field.get()
    cur2=con.cursor()
    cur2.execute("delete from membership where mem_no="+str(mem_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()

def display_employee():
    display_emp = Toplevel(manager)
    display_emp.title("display")
    lab = Label(display_emp, text="eid|designation|salary|mid|name")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from employee")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_emp, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)
    curr.close()

def delete_employee():
    emp_id = emp_id_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from employee where eid=" + str(emp_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()
    emp_id_field.delete(0, END)

def insert_activities():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()

    mycur.execute("insert into membership values (:a_no,:act_name,:cost)",
                  {
                      'a_no': None,
                      'act_name': act_name_field.get(),
                      'cost': cost_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()
    act_name_field.delete(0, END)
    cost_field.delete(0, END)
def display_activities():
def delete_activities():


# region membership table querying and buttons
top = Label(manager, text="NEW MEMBERS", fg="white",bg="#94958B", font="verdana 30 bold").grid(row=0, column=1)
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


b1 = Button(manager, text="INSERT", font="30", fg="white", bg="#464655", width="20", command=insert).grid(row=9, column=1)
b2=Button(manager,text="DISPLAY",font="30",fg="white", bg="#464655",width="20",command=display_membership).grid(row=10,column=1)
b3=Button(manager,text="DELETE",font="30",fg="white", bg="#464655",width="20", command=delete_membership).grid(row=11,column=1)
empty=Label(manager,bg="#EDDFEF").grid(row=12,column=0)
# endregion

# region employee part, querying and buttons



top1 = Label(manager, text="EMPLOYEE",fg="white", bg="#94958B", font="verdana 30 bold").grid(row=13, column=1)
designation = Label(manager, text="DESIGNATION:")
salary = Label(manager, text="SALARY:")
mid = Label(manager, text="MID:")
name = Label(manager, text="NAME:")


#grid formating
designation.grid(row=14, column=0)
salary.grid(row=15, column=0)
mid.grid(row=16, column=0)
name.grid(row=17, column=0)



designation_field = Entry(manager)
salary_field = Entry(manager)
mid_field = Entry(manager)
name_field = Entry(manager)


#grid formating
designation_field.grid(row=14, column=1, ipadx="100")
salary_field.grid(row=15, column=1, ipadx="100")
mid_field.grid(row=16, column=1, ipadx="100")
name_field.grid(row=17, column=1,ipadx="100" )

#buttons

b1 = Button(manager, text="INSERT", font="30", fg="white", bg="#464655", width="20", command=insert_employee).grid(row=18, column=1)
b2=Button(manager,text="DISPLAY",font="30",fg="white", bg="#464655",width="20",command=display_employee).grid(row=19,column=1)
empty=Label(manager,bg="#EDDFEF").grid(row=20,column=0)
#stuff for delete button since eid is auto increment
emp_id = Label(manager, text="DELETE EMPLOYEE:").grid(row=21, column=0)
emp_id_field = Entry(manager)
emp_id_field.grid(row=22,column=1,ipadx="100")
b3 = Button(manager, text="DELETE", font="30", fg="white", bg="#464655",width="20", command=delete_employee).grid(row=23,column=1)
# endregion

# region add or remove activities
top = Label(manager, text="ADD/REMOVE ACTIVITIES", fg="white",bg="#94958B", font="verdana 30 bold").grid(row=0, column=6)
act_name = Label(manager, text="ACTIVITY NAME:")
cost = Label(manager, text="COST:")


#grid formating
act_name.grid(row=1, column=5)
cost.grid(row=2, column=5)



act_name_field = Entry(manager)
cost_field = Entry(manager)


#grid formating
act_name_field.grid(row=1, column=6, ipadx="100")
cost_field.grid(row=2, column=6, ipadx="100")



b1 = Button(manager, text="INSERT", font="30", fg="white", bg="#464655", width="20", command=insert_activities).grid(row=3, column=6)
b2=Button(manager,text="DISPLAY",font="30",fg="white", bg="#464655",width="20",command=display_activities).grid(row=4,column=6)
b3=Button(manager,text="DELETE",font="30",fg="white", bg="#464655",width="20", command=delete_activities).grid(row=5,column=6)
empty=Label(manager,bg="#EDDFEF").grid(row=12,column=6)
# endregion




manager.mainloop()
