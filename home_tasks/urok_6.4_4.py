from tkinter import *
from tkinter.messagebox import *

def click(event):
    entry['bg'] = 'yellow'
    entry['fg'] = 'red'
    entry['font'] = 12
    label['text'] = entry.get()
    showinfo('Поле', entry.get())


root = Tk()
root.geometry("300x250")

entry = Entry()
entry.bind('<1>', click)
entry.pack(pady=20)
entry.focus_set()

label = Label()
label.pack()

root.mainloop()


