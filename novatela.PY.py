import tkinter as tk
from tkinter import messagebox

class Telona:

    def __init__(self, master):
        self.nossatelona = master
        self.nossatelona.title(" UNESP - NAE")

        #self.coisa = tk.Label(self.nossatelona, text = "Fala ") #,background="white")
        #self.coisa["font"] = ("Verdana","18")
        #self.coisa.pack(pady =0, side = tk.LEFT, fill =tk.Y)

        #self.coisa = tk.Label(self.nossatelona, text = "Título") #,background="white")
        #self.coisa["font"] = ("Verdana","15")
        #self.coisa.pack(ipadx =25, ipady = 10, side=tk.RIGHT)

        self.fr = tk.Frame(self.nossatelona)
        self.fr2 = tk.Frame(self.nossatelona)

        self.fr.pack()
        self.fr2.pack(side=tk.BOTTOM)

        self.coisa = tk.Label(self.fr, text="Frame 1", font=("Arial","16"))
        self.coisa.place(relx=0.1, y=0.5)

        self.coisa = tk.Label(self.nossatelona, text = "NAE - Núcleo de Apoio ao Estudade") #,background="white")
        self.coisa["font"] = ("Verdana","15")
        self.coisa.pack(fill = tk.X)

        self.coisa2 = tk.Label(self.fr2, text="Frame 2", font=("Arial","16"), relief="raised")
        self.coisa2.pack()

        self.coisa = tk.Label(self.nossatelona, text="Cadastro", font=("Verdana","16"), relief="raised")
        self.coisa.pack(pady=15)
        self.coisa.bind("<Button-1>", self.posta)

        self.coisa = tk.Label(self.nossatelona, text="Consulta", font=("Verdana","16"), relief="raised")
        self.coisa.pack(pady=20)
        self.coisa.bind("<Button-1>", self.posta)

        self.btn =tk.Button(self.nossatelona, text="Clique", font=("Verdana","16"), command=self.respostabtn)

    def respostabtn(self):
        messagebox.showinfo("Caixa de Mensagem", "Você clicou")

    def posta(self, event):
        print(event.x, event.y)
        messagebox.showinfo("Caixa de Mensagem", "Você clicou")

janelaRaiz = tk.Tk()
janelaRaiz.geometry("900x800")

Telona(janelaRaiz)
janelaRaiz.mainloop()


