from tkinter import *

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


class Application:
    def __init__(self, master=None):
      pass

janela = Tk()
janela.geometry ("800x600")
janela.title("UNESP - NAE - Núcleo de Apoio ao Esrtudante ")

titulo_nae = Label(janela, text="Atendimento ao Aluno")
titulo_nae.grid(column=0, row=0, padx=300, pady=100)
titulo_nae2= Label(janela, text="Escolha sua opção")
titulo_nae2.grid(column=0, row=4, padx=300, pady=100)

botao = Button(janela, text="Cadastrar seus dados", command=pegar_cotacoes)
botao.grid(column = 0, row = 2)

texto_aviso = Label(janela, text="")
texto_aviso.grid(column=0, row=3)

Application(janela)
janela.mainloop()

