class Carta: #inicializo la clase Carta
    def __init__(self, palo, valor):   #contructor de la clase
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f'{self.valor} de {self.palo}' #imprimo el valor y palo de cada carta