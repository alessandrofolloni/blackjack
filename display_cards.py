from tkinter import *
from tkinter import ttk

def oscura():
    pass


root = Tk()
root.title("BLACKJACK TABLE")
root.geometry("600x400")
icon = PhotoImage(file="images/utils/logo.png")
root.iconphoto(True, icon)

button = Button(command=oscura)
button.pack()

root.mainloop()
