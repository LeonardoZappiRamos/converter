from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import pandas as pd
import os
from pysus.utilities.readdbc import read_dbc


def FileName():
    filetypes = (
        ('dbc files', '*.dbc'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(title= "Escolha o arquivo", initialdir="C:\\", filetypes=filetypes)
    Convert(filename)

def Convert(file):
    #df = read_dbc(file, encoding='iso-8859-1')
    #dataFrame = pd.DataFrame(df)

    SAVING_PATH = fd.asksaveasfile(mode='w', defaultextension=".csv")
    #dataFrame.to_csv(SAVING_PATH,index=False, header=False, mode='a')

    SAVING_PATH.close()




root = Tk()
root.title("DBC Converter")
root.geometry('250x100')

# Cria um Frame
mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0)

# Config da Tela
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# TITLE
ttk.Label(mainframe, text="DBC Converter", font=("Helvetica 12")).grid(column=0, row=0)

# INPUT FILE
btn = ttk.Button(mainframe,text="Escolha um arquivo" ,command=FileName).grid(column=0, row=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
