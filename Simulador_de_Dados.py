#Simulador de Dado
#Simular uma jogada de um dado aleatóriamente 

from http.client import INSUFFICIENT_STORAGE
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de jogar o dado?'

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

        