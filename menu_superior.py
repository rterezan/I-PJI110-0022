from doctest import master
from tkinter import *
from turtle import left
import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar
# Module Import
import mariadb
import sys
import maria_banco
import pymysql
import verifica_db
import webbrowser as wb
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)
from PIL import Image
from datetime import date


# import imprime
# import cadastro_funcao

def selfgrava(cur, nov_matric, nov_nome, nov_cpf, nov_endereco):
    pass


class superiormenu:

    def __init__(self, master=None):
        self.jane=master
        self.jane.title ( " UNESP - NAE - Núcleo de Apoio ao Estudante - FCLAr" )

        self.barra_menu=tk.Menu ( self.jane )
        self.jane.config ( menu=self.barra_menu )

        self.submenu=tk.Menu ( self.barra_menu, tearoff=0 )
        self.submenu.add_command ( label="Cadastrar", command=self.cadastro )
        self.submenu.add_separator ( )
        self.submenu.add_command ( label="Consultar" )
        self.submenu.add_separator ( )
        self.submenu.add_command ( label="Alterar" )
        self.submenu.add_separator ( )
        self.submenu.add_command ( label="Apagar" )
        self.submenu.add_separator ( )
        # self.submenu.add_command(label="Listar", command = self.imprime)

        self.menub=tk.Menu ( self.barra_menu, tearoff=0 )
        self.menub.add_command ( label="Enviar documentos", command=self.lerArquivo )
        self.menub.add_command ( label="Enviar sua fotografia", command=self.subirfoto )

        self.edital=tk.Menu ( self.barra_menu, tearoff=0 )
        self.edital.add_command ( label="Processo Seletivo - Ingressantes", command=self.nevagador )
        self.edital.add_command ( label="Processo Seletivo - Veteranos", command=self.navegador )

        self.barra_menu.add_cascade ( label="Cadastramento", menu=self.submenu )
        self.barra_menu.add_cascade ( label="Anexar Documentos", menu=self.menub )
        self.barra_menu.add_cascade ( label="Consultar Editais", menu=self.edital )
        self.barra_menu.add_command ( label="Atendimento online",)

    def grava(cur, nov_matric, nov_nome, nov_cpf, nov_endereco, endereco):
        cur.execute ( "INSERT INTO mysql.teste_db(matricula, nome, cpf, endereco) VALUES (?, ?, ?, ?)",
                      (nov_matric, nov_nome, nov_cpf, nov_endereco) )
        # cur.execute("INSERT INTO mysql.teste_db(matricula, nome, cpf, endereco) VALUES (?, ?, ?, ?)",('nov_matric', 'nov_nome', 'nov_cpf', 'nov_endereco'))
        print ( "Eba" )
        print ( nov_nome )

    def cadastro(self):

        titulo_mensa=Label ( self.jane, text=" <= Digite seu Registro de Aluno (somente números)", font=('Arial 12') )
        titulo_mensa.place ( x=360, y=118 )

        titulo_nae2=Label ( self.jane, text="RA do Aluno", font=('Century 12 bold') )
        titulo_nae2.place ( x=100, y=120 )

        reg_aluno=Entry ( self.jane, font='Century 12', width=10 )
        reg_aluno.place ( x=250, y=120 )

        nae3=Label ( self.jane, text="Nome do Aluno", font=('Century 12 bold') )
        nae3.place ( x=100, y=150 )

        entra=Entry ( self.jane, font='Century 12', width=50 )
        entra.place ( x=250, y=150 )

        entra_cpf=Label ( self.jane, text="CPF", font=('Century 12 bold') )
        entra_cpf.place ( x=100, y=180 )

        mostra_cpf=Entry ( self.jane, font='Century 12', width=14 )
        mostra_cpf.place ( x=250, y=180 )

        idad_aluno=Label ( self.jane, text="Nascimento", font=('Century 12 bold') )
        idad_aluno.place ( x=100, y=210 )

        data_atual=date.today ( )
        print ( data_atual )

        # eidade = data_atual.strftime("%d/%m/%Y")
        # print(f, eidade)

        eidade=Entry ( self.jane, font='Century 12', width=10 )
        eidade.place ( x=250, y=210 )

        ender=Label ( self.jane, text="Endereço", font=('Century 12 bold') )
        ender.place ( x=100, y=240 )

        tender=Entry ( self.jane, font='Century 12', width=50 )
        tender.place ( x=250, y=240 )

        cidad=Label ( self.jane, text="Cidade", font=('Century 12 bold') )
        cidad.place ( x=100, y=270 )

        tcidad=Entry ( self.jane, font='Century 12', width=40 )
        tcidad.place ( x=250, y=270 )

        # print(tcidad)

        estat=Label ( self.jane, text="Estado", font=('Century 12 bold') )
        estat.place ( x=100, y=300 )

        comboestat=ttk.Combobox ( self.jane, font=('Arial 11'),
                                  values=[
                                      'Acre',
                                      'Alagoas',
                                      'Amapá',
                                      'Amazonas',
                                      'Bahia',
                                      'Ceará',
                                      'Distrito Federal',
                                      'Espírito Santo',
                                      'Goiás',
                                      'Maranhão',
                                      'Mato Grosso',
                                      'Mato Grosso do Sul',
                                      'Minas Gerais',
                                      'Pará',
                                      'Paraíba',
                                      'Paraná',
                                      'Pernambuco',
                                      'Piauí',
                                      'Rio de Janeiro',
                                      'Rio Grande do Norte',
                                      'Rio Grande do Sul',
                                      'Rondônia',
                                      'Roraima',
                                      'Santa Catarina',
                                      'São Paulo',
                                      'Sergipe',
                                      'Tocantins'] )

        # print(dict(comboestat))
        comboestat.place ( x=250, y=300 )
        comboestat.current ( 1 )

        # testat = Entry(self.jane, font='Century 12', width=2)
        # testat.place(x=250, y=200)

        alu_email=Label ( self.jane, text="E-mail", font=('Century 12 bold') )
        alu_email.place ( x=100, y=330 )

        t_alu_email=Entry ( self.jane, font='Century 12', width=40 )
        t_alu_email.place ( x=250, y=330 )

        alu_tele=Label ( self.jane, text="(DDD) Telefone", font=('Century 12 bold') )
        alu_tele.place ( x=100, y=360 )

        t_alu_tele=Entry ( self.jane, font='Century 12', width=15 )
        t_alu_tele.place ( x=250, y=360 )

        alu_curso=Label ( self.jane, text="Curso", font=('Century 12 bold') )
        alu_curso.place ( x=100, y=390 )

        combocurso=ttk.Combobox ( self.jane, font=('Arial 11'),
                                  values=[
                                      "Administração Pública",
                                      "Ciências Econômicas",
                                      "Ciências Sociais",
                                      "Letras",
                                      "Pedagogia"] )
        # print(dict(combocurso))
        combocurso.place ( x=250, y=390 )
        combocurso.current ( 1 )

        # t_alu_curso = Entry(self.jane, font='Century 12', width=15)
        # t_alu_curso.place(x=250, y=290)

        labelTop=Label ( self.jane, text="Período", font=('Century 12 bold') )
        labelTop.place ( x=100, y=420 )

        comboperiodo=ttk.Combobox ( self.jane, font=('Arial 11'),
                                    values=[
                                        "Diurno",
                                        "Matutino",
                                        "Noturno",
                                        "Integral"] )
        # print(dict(comboperiodo))
        comboperiodo.place ( x=250, y=420 )
        comboperiodo.current ( 1 )

        alu_renda=Label ( self.jane, text="Renda Familiar", font=('Century 12 bold') )
        alu_renda.place ( x=100, y=470 )

        t_alu_renda=Entry ( self.jane, font='Century 12', width=10 )
        t_alu_renda.place ( x=250, y=470 )

        alu_familia=Label ( self.jane, text="No. famíliares", font=('Century 12 bold') )
        alu_familia.place ( x=100, y=500 )

        t_alu_familia=Entry ( self.jane, font='Century 12', width=2 )
        t_alu_familia.place ( x=250, y=500 )

        valor_selec=tk.BooleanVar ( )
        valor_selec.set ( False )

        alu_auximora=Label ( self.jane, text="Quais auxílios solicita ? (até 2):", font=('Century 12 bold') )
        alu_auximora.place ( x=100, y=540 )

        caixa_morada=Checkbutton ( self.jane, text='Moradia', font=('Arial 11'), var=valor_selec )
        caixa_morada.place ( x=340, y=540 )

        valor_selec2=tk.BooleanVar ( )
        valor_selec2.set ( False )

        caixa_alimenta=Checkbutton ( self.jane, text='Alimentação', font=('Arial 11'), var=valor_selec2 )
        caixa_alimenta.place ( x=450, y=540 )

        valor_selec3=tk.BooleanVar ( )
        valor_selec3.set ( False )

        caixa_aluguel=Checkbutton ( self.jane, text='Aluguel', font=('Arial 11'), var=valor_selec3 )
        caixa_aluguel.place ( x=590, y=540 )

        valor_selec4=tk.BooleanVar ( )
        valor_selec4.set ( False )

        caixa_transporte=Checkbutton ( self.jane, text='Transporte', font=('Arial 11'), var=valor_selec4 )
        caixa_transporte.place ( x=700, y=540 )

        self.botao=tk.Button ( self.jane, text="Confirma Dados ?", font=("Arial", "13") )
        self.botao.place ( x=250, y=630, anchor=tk.SW )

        self.brasao ( )

        try:
            conn=mariadb.connect (
                user="root",
                password="Javeio2023*",
                host="localhost",
                port=3306,
                autocommit=True )
            print ( "oba" )

            # Instanciar Cursor
            cur=conn.cursor ( )
            nov_matric=reg_aluno.get ( )
            nov_nome=entra.get ( )
            nov_cpf=mostra_cpf.get ( )
            nov_endereco=tender.get ( )

            self.grava ( cur,
                         nov_matric,
                         nov_nome,
                         nov_cpf,
                         nov_endereco )

            conn.close ( )

        except mariadb.Error as e:
            print ( f"Erro de conexão com o db ou DMLL : {e}" )
            sys.exit ( 1 )

    def lerArquivo(self):
        self.arquivo=filedialog.askopenfile ( mode="r",
                                              title="Anexe uma imagem (.JPG ou .PNG) ou documento (.TXT OU .PDF)",
                                              filetypes=(("Arquivos JPG", "*.jpg"), ("Arquivos PDF", "*.png")) )
        # self.conteudo = self.arquivo.read()
        self.im2=Image.open ( 'Prova BD.jpg' )
        self.imagem_selo=self.im2.resize ( (170, 130) )
        self.im2.show ( )
        titulo_salvo=Label ( self.jane, text=" <= Documento anexado                                                                   ", font=('Arial 12') )
        titulo_salvo.place ( x=360, y=118 )
        self.lisdoc = Label(self.jane, Text = "Documentos enviados:")
        self.lisdoc.place(x=800, y=100)
        self.imagem_foto=ImageTk.PhotoImage (self.imagem_selo)
        self.alu_doc=Label(self.jane, image=self.imagem_foto )
        self.alu_doc.place ( x=800, y = 130 )

    def subirfoto(self):
        self.arquivo=filedialog.askopenfile ( mode="r", title="Anexe sua fotografia (.JPG ou .PNG)",
                                              filetypes=(("Arquivos JPG", "*.jpg"), ("Arquivos png", "*.png")) )
        # self.conteudo = self.arquivo.read()
        self.im=Image.open ( 'natali.jpeg' )
        self.im.show ( )
        self.imaselo=self.im.resize ( (120, 100) )
        self.imafoto=ImageTk.PhotoImage ( self.imaselo )
        self.alu_foto=Label( self.jane, image=self.imafoto )  # .pack( side=BOTTOM )
        self.alu_foto.place ( x=100, y=2 )

        # tela_cv()

    def navegador(self):
        wb.open_new_tab (
            'https://www.fclar.unesp.br/#!/instituicao/administracao/diretoria/nucleo-de-apoio-ao-estudante/processo-seletivo/processo-seletivo-2021---ingressantes/' )

    def nevagador(self):
        wb.open_new_tab ('https://www.fclar.unesp.br/Home/Instituicao/Administracao/Diretoria/nucleodeapoioaoestudante/edital---permanencia1.pdf')

    def calendario(self):
        cal=Calendar ( root, selectmode='day',
                       year=2020, month=5,
                       day=22 )

        cal.pack ( pady=20 )

    def execute(self, param, param1):
        pass

    def brasao(self):
        self.im3=Image.open ( 'selofcl.png' )
        # im3.show()
        self.selo=self.im3.resize ( (144, 100) )
        self.selofoto=ImageTk.PhotoImage ( self.selo )
        self.caraca=Label ( self.jane, image=self.selofoto )  # .pack( side=TOP )
        self.caraca.place ( x=500, y=2 )


Raiz=tk.Tk ( )
Raiz.geometry ( "1200x900" )

superiormenu ( Raiz )
Raiz.mainloop ( )
