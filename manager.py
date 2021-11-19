from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

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


manager.mainloop()
