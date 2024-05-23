from tkinter import *

def click():
    a = float(entry1.get)
    b = float(entry2.get)
    result = (3 * a - b) * (a + 2 * b)
    label['text'] = str(result)


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


