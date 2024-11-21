from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk

def upload():
    pass

window = Tk()
window.title("Файл в облако")

ttk.Button(text="Загрузить файл", command=upload).pack()

entry = Entry()
entry.pack()

window.mainloop()
