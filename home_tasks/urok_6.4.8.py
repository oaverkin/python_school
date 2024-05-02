from tkinter import *


def label_click(event):
    if event.widget == label1:
        label1['fg'] = 'yellow'
        label1['bg'] = 'blue'
        label2['bg'] = 'yellow'
        label2['fg'] = 'blue'
        label1['width'] = label1['width']
        label2['width'] = label2['width']

    elif event.widget == label2:
        label1['fg'] = 'blue'
        label1['bg'] = 'yellow'
        label2['bg'] = 'blue'
        label2['fg'] = 'yellow'
        label1['width'] = label1['width']
        label2['width'] = label2['width']


root = Tk()
root.title("Україна")
root.geometry("180x140")

label1 = Label(text="Моя країна", font=("Arial", 12, "bold"), width=25, height=4)
label1.pack()
label1.bind("<1>", label_click)

label2 = Label(text="Україна", font=("Arial", 12, "bold"), width=25, height=4)
label2.pack()
label2.bind("<1>", label_click)

root.mainloop()


