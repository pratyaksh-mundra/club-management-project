from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
home = Tk()




def manager():
    manager = Toplevel()
    manager_edit= Button(manager, text="edit").grid(row=1, column=1)
    manager_view = Button(manager, text="view").grid(row=2, column=1)



def employee():
    employee = Toplevel()



def customer():
    customer = Toplevel()


manager_view_button = Button(home, text="manager", command=manager).grid(row=2, column=1)
employee_view_button = Button(home, text="employee", command=employee).grid(row=3, column=1)
customer_view_button = Button(home, text="customer", command=customer).grid(row=4, column=1)
mainloop()
