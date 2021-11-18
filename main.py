# This is a sample Python script.
from tkinter import *
import sqlite3
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import database
con = sqlite3.connect("data/identifier.sqlite")
c=con.cursor()
c.execute("select * from membership")
