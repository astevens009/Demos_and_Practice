import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

options ={
    'fill' : 'both',
    'padx' : 10,
    'pady' : 10,
    'ipadx' : 5
}

root = tk.Tk()
root.title('Demo Messagebox')
root.resizable(False, False)
root.geometry('350x150')

ttk.Button(
    root,
    text='Show an error message',
    command=lambda: showerror(
        title='Error',
        message='This is an error message')
).pack(**options)

ttk.Button(
    root,
    text='Show an error message',
    command=lambda: showinfo(
        title='Information',
        message='This is an information message')
).pack(**options)

ttk.Button(
    root,
    text='Show a warning message',
    command=lambda: showwarning(
        title='Warning',
        message='This is an error message')
).pack(**options)


root.mainloop()
