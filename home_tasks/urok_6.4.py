from tkinter import *

def label_click(event):
    label['text'] = 'Я учусь в 9 классе'
    label['font'] = 14
    label['fg'] = 'red'
    label['bg'] = 'yellow'


root = Tk()
root.geometry("500x400")

label = Label(root, text="Это описание")
label.pack(pady=20)
label.bind('<1>', label_click)
root.mainloop()


