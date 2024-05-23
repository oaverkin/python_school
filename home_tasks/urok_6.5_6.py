from tkinter import *

def click():
    a = float(entry1.get)
    b = float(entry2.get)
    c = float(entry3.get)
    result = (2 * a + b) * (a + c)
    label['text'] = str(result)


root = Tk()
root.geometry("300x250")

entry1 = Entry()
entry1.pack(pady=10)
entry2 = Entry()
entry2.pack(pady=10)
entry3 = Entry()
entry3.pack(pady=10)

label = Label('_____')
label.pack(pady=10)

button = Button(text='Сумма', command=click)
button.pack(pady=10)


root.mainloop()


