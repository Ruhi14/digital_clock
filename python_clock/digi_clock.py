from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Digital Clock")

def present_time():
    display_time = time.strftime('%H:%M:%S %p')
    digi_clock.config(text=display_time)
    digi_clock.after(200, present_time)

digi_clock = Label(root, font=('calibri', 40, 'bold'), bg='black', fg='white')
digi_clock.pack()

present_time()
root.mainloop()