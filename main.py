from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def FileName():
    filename = askopenfilename()

    print(filename)


root = Tk()
root.title("DBC Converter")
root.geometry('250x100')
# Cria um Div
mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0)

# Config da Tela
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe,
          text="DBC Converter",
          font=("Helvetica 12")).grid(column=0, row=0)

ttk.Button(mainframe, command=FileName).grid(column=0, row=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
