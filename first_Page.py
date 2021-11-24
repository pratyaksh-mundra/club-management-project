import sys
import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
from tkinter import ttk
import tkinter as tk
import  os


window = Tk()
window.configure()

window.title("CLUB MANAGEMENT")
window.geometry('550x200')

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

def run_manager():
    os.system('python managerLogin.py')
def run_employee():
    os.system('python employeeLogin.py')
def run_member():
    os.system('python memberLogin.py')


# region misc
btn1 = ttk.Button(window, text="MANAGER VIEW" , command=run_manager)
btn2 = ttk.Button(window, text="EMPLOYEE VIEW", command=run_employee)
btn3 = ttk.Button(window, text="MEMBER VIEW",  command=run_member)
btn1.place(relx='0.350',rely='0.298',height='30',relwidth='0.35')
empty=Label(window, ).grid(row=1, column=0,ipadx="100")
btn2.place(relx='0.350',rely='0.498',height='30',relwidth='0.35')
empty=Label(window, ).grid(row=3, column=6)
btn3.place(relx='0.350',rely='0.698',height='30',relwidth='0.35')
# endregion

window.mainloop()
