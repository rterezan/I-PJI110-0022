import PySimpleGUI as sg
class TelaPython:
    def _init_(self):
        #layout
        layout = [
            [sg.Text('Nome'),sg.InputText()],
            [sg.Text('Idade'),sg.InputText()],
            [sg.Button('Enviar Dados')]
        ]
# Janela
        janel = sg.Window('Dados do Usuário').layout(layout)
# e extrair dados
        self.button, self.values = janel.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar
