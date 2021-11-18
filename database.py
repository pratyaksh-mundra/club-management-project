from tkinter import *
import sqlite3
import mysql
import cx_Oracle
from PIL import ImageTk, Image
root = Tk()
conn=sqlite3.connect("identifier.sqlite")

c=conn.cursor()
c.execute("select * from membership")
r=c.fetchall()




mylable=Label(root, text=r)
mylable.grid(row=0, column=1)
root.mainloop()
