from tkinter import *
from tkinter import ttk
from main import admitted


def validate_input_1(new_value):
    if admitted(new_value):
        return True
    else:
        entry.delete(0, END)
        print("Valore non valido")
        return False


def validate_input_2(new_value):
    if admitted(new_value):
        return True
    else:
        entry2.delete(0, END)
        print("Valore non valido")
        return False


def oscura():
    pass


def probabilities():
    card_1 = entry.get()


root = Tk()
root.title("BLACKJACK TABLE")
root.geometry("600x400")
icon = PhotoImage(file="images/utils/logo.png")
root.iconphoto(True, icon)

button = Button(root, command=oscura)
button.pack()

validate_cmd_1 = root.register(validate_input_1)
validate_cmd_2 = root.register(validate_input_2)

entry = Entry(root, validate="key", validatecommand=(validate_cmd_1, "%P"))
entry.pack(padx=10, pady=10)
validate_button = Button(root, text="Valida", command=lambda: validate_input_1(entry.get()))
validate_button.pack(pady=5)

entry2 = Entry(root, validate="key", validatecommand=(validate_cmd_2, "%P"))
entry2.pack(padx=10, pady=10)
validate_button2 = Button(root, text="Valida", command=lambda: validate_input_2(entry2.get()))
validate_button2.pack(pady=5)

root.mainloop()
