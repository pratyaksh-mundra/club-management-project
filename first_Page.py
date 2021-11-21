import sys
import os
from tkinter import *

window = Tk()
window.configure(bg="#E9C46A")

window.title("CLUB MANAGEMENT")
window.geometry('550x200')


def run_manager():
    os.system('python manager.py')
def run_employee():
    os.system('python employee.py')
def run_member():
    os.system('python member.py')


# region misc
btn1 = Button(window, text="MANAGER VIEW", bg="#264653", fg="#2A9D8F", command=run_manager)
btn2 = Button(window, text="EMPLOYEE VIEW", bg="#264653", fg="#2A9D8F", command=run_employee)
btn3 = Button(window, text="MEMBER VIEW", bg="#264653", fg="#2A9D8F", command=run_member)
btn1.grid(column=0, row=0,ipadx="100")
empty=Label(window, bg="#E9C46A").grid(row=1, column=0,ipadx="100")
btn2.grid(column=0, row=2,ipadx="100")
empty=Label(window, bg="#E9C46A").grid(row=3, column=6)
btn3.grid(column=0, row=4,ipadx="100")
# endregion

window.mainloop()
