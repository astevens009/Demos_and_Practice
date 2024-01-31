from tkinter import *
from tkinter import messagebox
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot



top = Tk()
top.geometry('100x100')

def greetings():
    messagebox.showinfo('Welcome to The Matrix!\nCheck your reality at the door...', 'Matrix Greeting')

button1 = Button(top, text = 'Matrix Greeting', command = greetings)
button1.place(x=35, y=50)

top.mainloop()