from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
import os
from tkinter import ttk
import tkinter as tk

def run_member():
    os.system('python memberLogin.py')

def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      #open database
      conn = sqlite3.connect('identifier.sqlite')
      #select query
      cursor = conn.execute('SELECT * from member_login where mem_username="%s" and mem_password="%s"'%(uname,pwd))
      #fetch data
      if cursor.fetchone():
       message.set("Login success")
       run_member()
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.tk.call("source", "azure.tcl")
    login_screen.tk.call("set_theme", "dark")
    #Setting title of screen
    login_screen.title("MEMBER LOGIN")
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen.configure()
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="MEMBER LOGIN FORM").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=120)
    #Login button
    ttk.Button(login_screen, text="Login",  command=login).place(x=125,y=170)
    login_screen.mainloop()
Loginform()