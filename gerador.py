import random
import site
import PySimpleGUI as sg
import os
from playsound import playsound

class PassGen:
    def __init__(self):
        #layout
        sg.theme('Black')
        playsound('NEFFEX - Grato.mp3',block=False)
        
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),sg.Input(key='site', size=(10, 1))],
            [sg.Text('Email/Usuário', size=(10, 1)),sg.Input(key='usuario', size=(10, 1))],
            [sg.Text('Número de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size=(3,1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')]

        ]
        #janela
        self.janela = sg.Window('Gerador de senha', layout)

    def Iniciar(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED:
                break
            if eventos == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choice(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores[site]}, usuario: {valores['usuario']},\
                 nova senha: {nova_senha}")

        print('Arquivo salvo')
gen = PassGen()
gen.Iniciar()
