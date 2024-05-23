from tkinter import *

def click():
    x = float(entry1.get)
    y = float(entry2.get)
    z = x + y
    label['text'] = str(z)


root = Tk()
root.geometry("300x250")

entry1 = Entry()
entry1.pack(pady=10)
entry2 = Entry()
entry2.pack(pady=10)

label = Label('_____')
label.pack(pady=10)

button = Button(text='Сумма', command=click)
button.pack(pady=10)


root.mainloop()


