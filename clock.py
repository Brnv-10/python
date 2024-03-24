from tkinter import *
from time import *


def update():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%B %D, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)
window= Tk()


time_label=Label(window, font=("forte",50),fg="black",bg="white")
time_label.pack()

day_label=Label(window, font=("arial",30),fg="black",bg="white")
day_label.pack()

date_label=Label(window, font=("arial",30),fg="red",bg="white")
date_label.pack()

update()

window.mainloop()