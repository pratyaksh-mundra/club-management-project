from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
import os
from tkinter import ttk
import tkinter as tk

def run_employee():
    os.system('python employeeLogin.py')

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
      cursor = conn.execute('SELECT * from manager where e_username="%s" and e_password="%s"'%(uname,pwd))
      #fetch data
      if cursor.fetchone():
       message.set("Login success")
       run_employee()
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("employee login")
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen.configure(bg='#293241')
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Login From", fg="#E0FBFC", bg="#EE6C4D",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Username * ",fg="#EE6C4D", bg="#98c1d9",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    #Password Label
    Label(login_screen, text="Password * ",fg="#EE6C4D", bg="#98c1d9",font=("Arial",12,"bold")).place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg="#293241",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, command=login, fg="#EE6C4D", bg="#98c1d9",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()

Loginform()