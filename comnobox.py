import tkinter as tk
from tkinter import ttk
from tkinter import *


app = tk.Tk()
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app,
                            values=[
                                    "January",
                                    "February",
                                    "March",
                                    "April"])
#print(dict(comboExample))
#comboExample.grid(column=0, row=1)
#comboExample.current(1)

entry = Entry(app)
print(entry.get()) # Would print entry data in CL
#ent is the name of the Entry
s = entry.get()

print(comboExample.current(), comboExample.get())

app.mainloop()
