#Simulador de Dado
#Simular uma jogada de um dado aleatóriamente 

import PySimpleGUI as sg
import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6

        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button ('sim'),sg.Button('não')]
        ]
    def Iniciar(self): 
        #Criar uma janela
        self.janela = sg.Window ('Simulador de Dado', layout= self.layout)

        #Ler os valores na tela
        self.eventos, self.valores = self.janela.Read()

        #Realizar algo com os valores extraidos
            try:
                if self.evento == 'sim' or self.evento == 's':
                    self.GerarValorDoDado()
                elif self.evento == 'não' or self.evento =='n':
                    print('Agradeço a sua participação!!')
                else:
                     print('Favor digitar sim ou o não')
            except:
                    print('Ocorreu um erro ao receber sua resposta!!')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

        