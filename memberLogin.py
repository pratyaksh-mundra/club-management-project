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
    login_screen.title("member login")
    login_screen.geometry("350x250")
    login_screen.configure(bg='#293241')
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    Label(login_screen,width="300", text="Login From", fg="#E0FBFC", bg="#EE6C4D",font=("Arial",12,"bold")).pack()
    Label(login_screen, text="Username * ",fg="#EE6C4D", bg="#98c1d9",font=("Arial",12,"bold")).place(x=20,y=40)
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    Label(login_screen, text="Password * ",fg="#EE6C4D", bg="#98c1d9",font=("Arial",12,"bold")).place(x=20,y=80)
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    Label(login_screen, text="",textvariable=message,bg="#293241",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    Button(login_screen, text="Login", width=10, height=1, command=login, fg="#EE6C4D", bg="#98c1d9",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()
Loginform()