import sys
import os
from tkinter import *

window = Tk()
window.configure(bg="#293241")

window.title("CLUB MANAGEMENT")
window.geometry('550x200')


def run_manager():
    os.system('python managerLogin.py')
def run_employee():
    os.system('python employeeLogin.py')
def run_member():
    os.system('python memberLogin.py')


# region misc
btn1 = Button(window, text="MANAGER VIEW", fg="#EE6C4D", bg="#98c1d9", command=run_manager)
btn2 = Button(window, text="EMPLOYEE VIEW", fg="#EE6C4D", bg="#98c1d9", command=run_employee)
btn3 = Button(window, text="MEMBER VIEW", fg="#EE6C4D", bg="#98c1d9", command=run_member)
btn1.grid(column=0, row=0,ipadx="100")
empty=Label(window, bg="#293241").grid(row=1, column=0,ipadx="100")
btn2.grid(column=0, row=2,ipadx="100")
empty=Label(window, bg="#293241").grid(row=3, column=6)
btn3.grid(column=0, row=4,ipadx="100")
# endregion

window.mainloop()
