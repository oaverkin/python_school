from tkinter import *

def label_click(event):
    label['text'] = 'Меня зовут Олег'
    label['height'] = 5


root = Tk()
root.geometry("500x400")
label = Label(root, text="Это описание")
label.pack(pady=20)
label.bind('<Double-Button-1>', label_click)
root.mainloop()


