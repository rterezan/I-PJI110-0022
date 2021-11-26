from tkinter import *
from turtle import left

import requests


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_aviso["text"] = texto


def get_value():

    titulo_nae2 = Label(janela, text="RA do Aluno", font=('Century 15 bold'))
    titulo_nae2.grid(column=1, row=2, padx=0, pady=0)

    reg_aluno = Entry(janela, font='Century 12', width=10)
    reg_aluno.grid(column=2, row=2, padx=0, pady=0)

    nae3 = Label(janela, text="Nome do Aluno")
    nae3.grid(column=1, row=3, padx=0, pady=0)

    entra = Entry(janela, font='Century 15', width=40)
    entra.grid(column=2, row=3, pady=0)

    idad_aluno  = Label(janela, text="Idade")
    idad_aluno.grid(column=1, row=4, padx=0, pady=0)

    eidade = Entry(janela, font='Century 15', width=3)
    eidade.grid(column=2, row=4, pady=0)

    e_text = entra.get()
    novaidade = eidade.get()
    aluno = reg_aluno.get()
    pessoas.append((aluno, e_text, novaidade))

def cadastrar():
    identificador = input('Id? ')
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    pessoas.append((aluno, e_text, novaidade))


def listar():
    cabeca = Label(janela, text = "Listagem de alunos", font=('Century 15 bold'))
    cabeca.place(x=100, y=100)
    for pessoa in pessoas:
        aluno, e_text, novaidade = pessoa
        #centra =  entra.get()
        #print(f'Nome: {entra}, idade: {eidade}, id: {reg_aluno}')
        losna = Label(janela, text = 'Registro de Aluno:' + aluno + ' - ' + 'Nome: ' + e_text + ' - ' + 'Idade:' + novaidade, font=('Century 12 bold'))
        losna.place(x=100, y=110)

def buscar():
    #id = input('RA buscado? ')
    titulo = Label(janela, text="RA do Aluno")
    titulo.grid(column=1, row=1, padx=0, pady=0)
    reg_aluno = Entry(janela, text="RA do aluno", font='Century 12', width=10)
    reg_aluno.grid(column=2, row=1, pady=0)
    for pessoa in pessoas:
        aluno = reg_aluno.get()
        reg_aluno, entra, eidade = pessoa
        if reg_aluno == aluno:
            print(f'Nome: {entra}, idade: {eidade}, id: {reg_aluno}')
            break
    else:
        print(f'Pessoa com id {reg_aluno} não encontrada')


pessoas = []


class Application:
    def __init__(self, master=None):
              pass


janela = Tk()
janela.geometry("900x800")
janela.title("UNESP - NAE - Núcleo de Apoio ao Esrtudante ")

titulo_nae = Label(janela, text="Atendimento ao Aluno")
titulo_nae.grid(column=1, row=0, padx=10, pady=10)

button = Button(janela, text="Cadastrar", command=get_value)
button.grid(column=3, row=1, padx=10, pady=10)

cuton = Button(janela, text="Listar", command=listar)
cuton.grid(column=4, row=1, padx=10, pady=10)

dauton = Button(janela, text="Consultar", command=buscar)
dauton.grid(column=5, row=1, padx=10, pady=10)

#botao = Button(janela, text="Cadastrar seus dados", command=cadastrar)
#botao.grid(column=0, row=2)

# botao = Button(janela, text="Consulta dados", command=pegar_cotacoes)
# botao.grid(column = 0, row = 2)


Application(janela)
janela.mainloop()
