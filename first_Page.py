import sys
import os
from tkinter import *

window = Tk()

window.title("Running Python Script")
window.geometry('550x200')

def run():
    os.system('python manager.py')

btn = Button(window, text="MANAGER VIEW", bg="black", fg="white",command=run)
btn = Button(window, text="EMPLOYEE VIEW", bg="black", fg="white",command=run)
btn = Button(window, text="CUSTOMER VIEW", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)

window.mainloop()