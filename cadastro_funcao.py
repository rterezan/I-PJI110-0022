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
import Gravar.py


def cadast(self):
    self.jane = master
    titulo_nae2 = Label( self.jane, text="RA do Aluno", font=('Century 12 bold') )
    titulo_nae2.place( x=100, y=50 )

    reg_aluno = Entry( self.jane, font='Century 12', width=10 )
    reg_aluno.place( x=250, y=50 )

    nae3 = Label( self.jane, text="Nome do Aluno", font=('Century 12 bold') )
    nae3.place( x=100, y=80 )

    entra = Entry( self.jane, font='Century 12', width=40 )
    entra.place( x=250, y=80 )

    idad_aluno = Label( self.jane, text="Idade", font=('Century 12 bold') )
    idad_aluno.place( x=100, y=110 )

    eidade = Entry( self.jane, font='Century 12', width=3 )
    eidade.place( x=250, y=110 )

    ender = Label( self.jane, text="Endereço", font=('Century 12 bold') )
    ender.place( x=100, y=140 )

    tender = Entry( self.jane, font='Century 12', width=50 )
    tender.place( x=250, y=140 )

    self.botao = tk.Button( self.jane, text="Confirma Dados", font=("Arial", "15") )
    self.botao.place( x=300, y=210, anchor=tk.SW )

    e_text = entra.get()
    novaidade = eidade.get()
    aluno = reg_aluno.get()
    self.append( (aluno, e_text, novaidade) )

    def execute(self, cur):
        pass
