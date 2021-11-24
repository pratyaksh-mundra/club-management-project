from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
from tkinter import ttk
import tkinter as tk
import  os






manager = Tk()
con = sqlite3.connect("identifier.sqlite")
manager.configure()
manager.title("manager view")
manager.geometry("1600x900")
manager.tk.call("source", "azure.tcl")
manager.tk.call("set_theme", "dark")
def run_loginsetup():
    os.system('python login_setup.py')

# region write to csv functions
def write_to_csv_mem(records):
    with open('membership.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(records)


def write_to_csv_emp(records):
    with open('activities.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(records)


def write_to_csv_attend(records):
    with open('activities.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(records)


def write_to_csv_act(records):
    with open('activities.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(records)


def write_to_csv_mp(records):
    with open('activities.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerow(records)


# endregion

# region membership functions
def insert():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()

    mycur.execute("insert into membership values (:mem_no,:mem_type,:main_member,:exp_Date,:address)",
                  {
                      'mem_no': None,
                      'mem_type': mem_type_field.get(),
                      'main_member': main_member_field.get(),
                      'exp_Date': exp_Date_field.get(),
                      'address': address_field.get()
                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()

    mem_type_field.delete(0, END)
    main_member_field.delete(0, END)
    exp_Date_field.delete(0, END)
    address_field.delete(0, END)


def display_membership():
    display_mem = Toplevel(manager)
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
    export_btn = ttk.Button(display_mem, text="export to CSV", command=lambda: write_to_csv_mem(records))

    export_btn.grid(row=200, column=0)
    curr.close()


def delete_membership():
    mem_id = mem_no_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from membership where mem_no=" + str(mem_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

# region employee function
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
    export_btn = ttk.Button(display_emp, text="export to CSV", command=lambda: write_to_csv_emp(records))

    export_btn.grid(row=200, column=0)
    curr.close()


def delete_employee():
    emp_id = emp_id_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from employee where eid=" + str(emp_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()
    emp_id_field.delete(0, END)


# endregion

# region activities function
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
    display_act = Toplevel(manager)
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


def delete_activities():
    act_id = act_no_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from activities where a_no=" + str(act_id))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()
    emp_id_field.delete(0, END)


# endregion

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
    display_main = Toplevel(manager)
    display_main.title("display")
    lab = Label(display_main, text="pid|mem_no|pay_date|name|amount|employee id|manager id")
    lab.grid(row=0, column=0)
    con = sqlite3.connect("identifier.sqlite")
    curr = con.cursor()
    curr.execute("select * from main_payments")
    records = curr.fetchall()
    # print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(display_main, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)
    export_btn = ttk.Button(display_main, text="export to CSV", command=lambda: write_to_csv_mp(records))

    export_btn.grid(row=200, column=0)
    curr.close()


def delete_mp():
    pid1 = pid_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from main_payments where pid=" + str(pid1))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

# region family functions
def insert_fam():
    con = sqlite3.connect("identifier.sqlite")
    mycur = con.cursor()

    mycur.execute("insert into family values (:f_no,:mem_no,:name,:birthday,:anniversaries)",
                  {
                      'f_no': None,
                      'mem_no': mem_no_field.get(),
                      'name': name_field.get(),
                      'birthday': birthday_field.get(),
                      'anniversaries': anniversaries_field.get()

                  })
    con.commit()
    messagebox.showinfo("successful!, " "inserted")
    mycur.close()


    mem_no_field.delete(0, END)
    name_field.delete(0, END)
    birthday_field.delete(0, END)
    anniversaries_field.delete(0, END)



def display_fam():
    display_main = Toplevel(manager)
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


def delete_fam():
    fam = fam_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from family where mem_no=" + str(fam))
    con.commit()
    messagebox.showinfo("successful!,  deleted")
    cur2.close()


# endregion

def display_attendance():
    display_attend = Toplevel(manager)
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


# region membership table querying and buttons
top = Label(manager, text="NEW MEMBERS",  font="verdana 12 bold").grid(row=0, column=1)

mem_type = Label(manager, text="MEM TYPE:",)
main_member = Label(manager, text="NAME:",)
exp_Date = Label(manager, text="EXP DATE:",)
address = Label(manager, text="ADDRESS:",)

# grid formating

mem_type.grid(row=1, column=0)
main_member.grid(row=2, column=0)
exp_Date.grid(row=3, column=0)
address.grid(row=4, column=0)

mem_type_field = Entry(manager)
main_member_field = Entry(manager)
exp_Date_field = Entry(manager)
address_field = Entry(manager)

# grid formating

mem_type_field.grid(row=1, column=1, ipadx="100")
main_member_field.grid(row=2, column=1, ipadx="100")
exp_Date_field.grid(row=3, column=1, ipadx="100")
address_field.grid(row=4, column=1, ipadx="100")

b1 = ttk.Button(manager, text="INSERT",width="20", command=insert).grid(row=5,
                                                                                                          column=1)
b2 = ttk.Button(manager, text="DISPLAY",width="20", command=display_membership).grid(
    row=6, column=1)
# empty=Label(manager,bg="#EDDFEF").grid(row=7,column=0)
mem_no = Label(manager, text="ID:")
mem_no.grid(row=8, column=0)
mem_no_field = Entry(manager)
mem_no_field.grid(row=8, column=1, ipadx="100")

b3 = ttk.Button(manager, text="DELETE",width="20", command=delete_membership).grid(
    row=9, column=1)
empty = Label(manager).grid(row=11, column=0)
# endregion

# region employee part, querying and buttons


top1 = Label(manager, text="EMPLOYEE", font="verdana 12 bold").grid(row=12, column=1)
designation = Label(manager, text="DESIGNATION:")
salary = Label(manager, text="SALARY:")
mid = Label(manager, text="MID:")
name = Label(manager, text="NAME:")

# grid formating
designation.grid(row=13, column=0)
salary.grid(row=14, column=0)
mid.grid(row=15, column=0)
name.grid(row=16, column=0)

designation_field = Entry(manager)
salary_field = Entry(manager)
mid_field = Entry(manager)
name_field = Entry(manager)

# grid formating
designation_field.grid(row=13, column=1, ipadx="100")
salary_field.grid(row=14, column=1, ipadx="100")
mid_field.grid(row=15, column=1, ipadx="100")
name_field.grid(row=16, column=1, ipadx="100")

# buttons

b1 = ttk.Button(manager, text="INSERT",width="20", command=insert_employee).grid(
    row=17, column=1)
b2 = ttk.Button(manager, text="DISPLAY",width="20", command=display_employee).grid(
    row=18, column=1)
empty = Label(manager).grid(row=19, column=0)
# stuff for delete button since eid is auto increment
emp_id = Label(manager, text="DELETE EMPLOYEE:").grid(row=20, column=0)
emp_id_field = Entry(manager)
emp_id_field.grid(row=20, column=1, ipadx="100")
b3 = ttk.Button(manager, text="DELETE",width="20", command=delete_employee).grid(
    row=21, column=1)
# endregion

# region add or remove activities
top = Label(manager, text="ADD/REMOVE ACTIVITIES", font="verdana 12 bold").grid(row=0,
                                                                                                          column=6)
act_name = Label(manager, text="ACTIVITY NAME:")
cost = Label(manager, text="COST:")

# grid formating
act_name.grid(row=1, column=5)
cost.grid(row=2, column=5)

act_name_field = Entry(manager)
cost_field = Entry(manager)

# grid formating
act_name_field.grid(row=1, column=6, ipadx="100")
cost_field.grid(row=2, column=6, ipadx="100")

b1 = ttk.Button(manager, text="INSERT",width='20', command=insert_activities).grid(
    row=3, column=6,)
b2 = ttk.Button(manager, text="DISPLAY",width="20", command=display_activities).grid(
    row=4, column=6)

act_no = Label(manager, text="DELETE ACTIVITIES:").grid(row=5, column=5)
act_no_field = Entry(manager)
act_no_field.grid(row=5, column=6, ipadx="100")
b3 = ttk.Button(manager, text="DELETE",width="20", command=delete_activities).grid(
    row=6, column=6)
empty = Label(manager).grid(row=7, column=6)
empty = Label(manager).grid(row=7, column=6)
# endregion

# region add remove main_payments
top = Label(manager, text="PAYMENTS", font="verdana 12 bold").grid(row=8, column=6)
mem_no = Label(manager, text="MEMBER NO.: ")
pay_date = Label(manager, text="PAYMENT DATE: ")
name = Label(manager, text="NAME:")
amount = Label(manager, text="AMOUNT:")
eid = Label(manager, text="EMPLOYEE ID:")
mid = Label(manager, text="MANAGER_ID:")

# grid formating
mem_no.grid(row=9, column=5)
pay_date.grid(row=10, column=5)
name.grid(row=11, column=5)
amount.grid(row=12, column=5)
eid.grid(row=13, column=5)
mid.grid(row=14, column=5)

mem_no_field = Entry(manager)
pay_date_field = Entry(manager)
name_field = Entry(manager)
amount_field = Entry(manager)
eid_field = Entry(manager)
mid_field = Entry(manager)

# grid formating
mem_no_field.grid(row=9, column=6, ipadx="100")
pay_date_field.grid(row=10, column=6, ipadx="100")
name_field.grid(row=11, column=6, ipadx="100")
amount_field.grid(row=12, column=6, ipadx="100")
eid_field.grid(row=13, column=6, ipadx="100")
mid_field.grid(row=14, column=6, ipadx="100")

b1 = ttk.Button(manager, text="INSERT",width="20", command=insert_mp).grid(row=16,
                                                                                                             column=6)
b2 = ttk.Button(manager, text="DISPLAY",width="20", command=display_mp).grid(row=17,
                                                                                                               column=6)

pid = Label(manager, text="DELETE PAYMENTS:").grid(row=18, column=5)
pid_field = Entry(manager)
pid_field.grid(row=18, column=6, ipadx="100")
b3 = ttk.Button(manager, text="DELETE",width="20", command=delete_mp).grid(row=19,
                                                                                                             column=6)
empty = Label(manager).grid(row=20, column=6)

# endregion

# region attendance section
top = Label(manager, text="ATTENDANCE", font="verdana 12 bold").grid(row=0, column=8)
date1 = Label(manager, text="ENTER DATE:").grid(row=1, column=7)
date1_field = Entry(manager)
date1_field.grid(row=1, column=8, ipadx="50")
b3 = ttk.Button(manager, text="DISPLAY",width="20", command=display_attendance).grid(
    row=2, column=8)
# endregion

# region family part
top = Label(manager, text="FAMILY", font="verdana 12 bold").grid(row=4, column=8)
mem_no = Label(manager, text="MEM NUMBER: ")
name = Label(manager, text="NAME: ")
birthday = Label(manager, text="BIRTHDAY:")
anniversaries = Label(manager, text="ANNIVERSARIES:")

# grid formating
mem_no.grid(row=5, column=7)
name.grid(row=6, column=7)
birthday.grid(row=7, column=7)
anniversaries.grid(row=8, column=7)

mem_no_field = Entry(manager)
name_field = Entry(manager)
birthday_field = Entry(manager)
anniversaries_field = Entry(manager)


# grid formating
mem_no_field.grid(row=5, column=8, ipadx="100")
name_field.grid(row=6, column=8, ipadx="100")
birthday_field.grid(row=7, column=8, ipadx="100")
anniversaries_field.grid(row=8, column=8, ipadx="100")


b1 = ttk.Button(manager, text="INSERT", width="20", command=insert_fam).grid(row=9,column=8)
mem_no_dis = Label(manager, text="ENTER MEM NO :")
mem_no_dis.grid(row=10, column=7 )
mem_no_dis_field = Entry(manager)
mem_no_dis_field.grid(row=10, column=8, ipadx="50")

b2 = ttk.Button(manager, text="DISPLAY", width="20", command=display_fam).grid(row=11,column=8)

fam = Label(manager, text="DELETE FAMILY(MEM NO):").grid(row=12, column=7)
fam_field = Entry(manager)
fam_field.grid(row=12, column=8, ipadx="50")
b3 = ttk.Button(manager, text="DELETE", width="20", command=delete_fam).grid(row=13,column=8)
empty = Label(manager).grid(row=20, column=8)
# endregion

b3 = ttk.Button(manager, text="login setup", width="20", command=run_loginsetup).grid(row=30,column=8)





# Set the initial theme


def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if manager.tk.call("ttk::style", "theme", "use") == "azure-light":
        # Set light theme
        manager.tk.call("set_theme", "dark")
    else:
        # Set dark theme
        manager.tk.call("set_theme", "light")

# Remember, you have to use ttk widgets
button = ttk.Button(manager, text="Change theme!", command=change_theme)
button.grid(row=31,column=8)


manager.mainloop()
