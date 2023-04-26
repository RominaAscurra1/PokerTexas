import random
from collections import deque #importo la clase deque del módulo collections para trabajar con los arreglos
from carta import Carta #del archivo carta.py importo la clase Carta

class Mazo: #inicializo la clase Mazo
    def __init__(self):
        self.cartas = deque()
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']                         #defino los diferentes palos de la baraja inglesa
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']    #defino los valores de cartas inglesas
        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo, valor))

    def mezclar(self):
        random.shuffle(self.cartas)#mezclo el orden aleatoreamente de las cartas con la función 'shuffle' del módulo random

    def repartir(self, num_cartas):
        mano = [];                   #arreglo para saber que cartas le toca a cada jugador
        for i in range(num_cartas):  #bucle for que se realiza la cantidad de cartas que se pasa como parámetro en el método
            if len(self.cartas) > 0:
                mano.append(self.cartas.pop()) #guarda la carta en la mano del jugador
        return mano
