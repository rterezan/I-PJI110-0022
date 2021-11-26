from tkinter import *
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)
from PIL import Image

def mostra2 # creating a object
im = Image.open('natali.jpeg')
im2 = Image.open('Prova BD.jpg')

im.show()
im2.show()

#window = tk.Tk()
#window.geometry("500x500") # (optional)
#imagefile = {natali.jpg}
#img = ImageTk.PhotoImage(Image.open(imagefile))
#lbl = tk.Label(window, image = img).pack()
#window.mainloop()
