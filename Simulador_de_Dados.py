#Simulador de Dado
#Simular uma jogada de um dado aleatóriamente 

import PySimpleGUI as sg
import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de jogar o dado?'

        #Layout
        layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button ('sim'),sg.Button('não')]
        ]
        #Criar uma janela
        #Ler os valores na tela
        #Realizar algo com os valores extraidos

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta =='n':
                print('Agradeço a sua participação')
            else:
                print('Favor digitar sim ou o não')
        except:
                print('Ocorreu um erro ao receber sua reposta!!')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

        