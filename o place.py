from doctest import master
from tkinter import *
from turtle import left
import tkinter as tk
import requests
from tkinter import messagebox
from tkinter import filedialog
# Module Import
import mariadb
import sys
import maria_banco
import pymysql

class Telona:

    def __init__(self, master = None):
        self.jane = master
        self.jane.title(" UNESP - NAE - Núcleo de Apoio ao Estudante - FCLAr")

        self.barra_menu = tk.Menu(self.jane)
        self.jane.config(menu = self.barra_menu)#

        self.submenu = tk.Menu(self.barra_menu, tearoff=0)
        self.submenu.add_command(label="Cadastrar", command = self.cadastro)
        self.submenu.add_separator()
        self.submenu.add_command(label="Consultar")
        self.submenu.add_separator()
        self.submenu.add_command(label="Alterar")
        self.submenu.add_separator()
        self.submenu.add_command(label="Apagar")
        self.submenu.add_separator()
        #self.submenu.add_command(label="Listar", command = self.tentativa)#

        self.menub = tk.Menu(self.barra_menu, tearoff=0)
        self.menub.add_command(label="Ler arquivo", command = self.lerArquivo)
        self.menub.add_command(label="Abrir diretorio")
        self.barra_menu.add_cascade(label="Cadastramento", menu=self.submenu)
        self.barra_menu.add_cascade(label="Anexar Documentos", menu=self.menub)
        self.barra_menu.add_command(label="Consultar Editais")
        self.barra_menu.add_command(label="Atendimento online")

        #self.botao = tk.Button(self.jane, text="Botão", font=("Arial", "15"))
        #self.botao.place(x =50, y =50, anchor = tk.SW)

    def lerArquivo(self):
        self.arquivo = filedialog.askopenfile(mode="r", title = "Selecione um arquivo",
                                              filetypes = (("Arquivos PDF" , "*.jpg"),("Arquivos Python" , "*.py")))
        self.conteudo = self.arquivo.read()

        #print(self.conteudo)

        #def abredir(self):
    #    self.arquivo2 = filedialog.askopenfilename(title="Selecione um arquivo",
    #                                             filetypes = ((Arquivos de texto","*.txt), ("Arquivos Python","*.py)"))

    def cadastro(self):
        titulo_nae2 = Label(self.jane, text="RA do Aluno", font=('Century 12 bold'))
        titulo_nae2.place(x=100, y =50)

        reg_aluno = Entry(self.jane, font='Century 12', width=10)
        reg_aluno.place(x=250, y =50)

        nae3 = Label(self.jane, text="Nome do Aluno", font=('Century 12 bold'))
        nae3.place(x=100, y =80)

        entra = Entry(self.jane, font='Century 12', width=40)
        entra.place(x=250, y =80)

        idad_aluno  = Label(self.jane, text="Idade",  font=('Century 12 bold'))
        idad_aluno.place(x=100, y=110)

        eidade = Entry(self.jane, font='Century 12', width=3)
        eidade.place(x=250, y=110)

        ender  = Label(self.jane, text="Endereço",  font=('Century 12 bold'))
        ender.place(x=100, y=140)

        tender = Entry(self.jane, font='Century 12', width=50)
        tender.place(x=250, y=140)

        self.botao = tk.Button(self.jane, text="Confirma Dados", font=("Arial", "15"))
        self.botao.place(x =300, y =210, anchor = tk.SW)

        e_text = entra.get()
        novaidade = eidade.get()
        aluno = reg_aluno.get()
        self.append((aluno, e_text, novaidade))






janelaRaiz = tk.Tk()
janelaRaiz.geometry("900x600")

Telona(janelaRaiz)
janelaRaiz.mainloop()
