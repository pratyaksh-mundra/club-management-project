from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import csv
import sys
import datetime
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import pandas as pd

con = sqlite3.connect("identifier.sqlite")
mycur = con.cursor()
a = pd.read_sql("""SELECT a.act_name, COUNT(*)*cost AS "Total Cost"
                      FROM attendance a, activities ac
                      WHERE a.a_no=ac.a_no
                      GROUP BY a.act_name;""", con)
print(a)
root= tk.Tk()
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()

a.plot(x="act_name",y="Total Cost",kind='bar', legend=True, ax=ax)
ax.set_title('The Title for your chart')
root.mainloop()
print(a)