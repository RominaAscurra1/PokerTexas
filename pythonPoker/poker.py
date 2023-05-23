from mazo import Mazo
from jugador import Jugador

class Poker: #inicializo la clase Poker
    def __init__(self):
        self.mazo = Mazo()
        self.turno_actual = 0  # Agregamos el atributo turno_actual e inicializamos en 0
        self.apuesta_actual = 10  # Agregamos el atributo apuesta_actual e inicializamos en 0


    usuario = input("Ingrese un nombre de usuario: ")  # Ingresa el nombre de usuario el jugador

    # Se crean otros 4 jugadores bots que compiten con el usuario
    jugadorReal = Jugador(usuario, 100, False);
    bot1 = Jugador("Bot 1", 100, True)
    bot2 = Jugador("Bot 2", 100, True)
    bot3 = Jugador("Bot 3", 100, True)
    bot4 = Jugador("Bot 4", 100, True)

    jugadores = [jugadorReal, bot1, bot2, bot3, bot4]

    def iniciarJuego(self): #Metodo para inicial el juego

        for jugador in self.jugadores:
            self.mazo.mezclar() #LLamo al metodo que mezcla las cartas
            jugador.recibirMano(self.mazo.repartir(5))
            print(" ")
            print(jugador.nombre, "  Fichas: ", jugador.fichas)
            cont = 1

            #Si es el usuario muestro su cartas, de lo contrario solo muestro el nombre y sus fichas
            for carta in jugador.mano:
                if jugador.esBot == False:
                    print(carta.palo, end=" ")
                    print(carta.valor, end=", ")

                if cont == 5:
                    print(" ")
                cont = cont + 1

    def evaluarManos(self, jugador):  # Creo un metodo que evalua las manos
        valores = []
        palos = []

        for carta in jugador.mano:  # Guardo cada mano en arrays separando valor de palo
            valor = carta.valor
            palo = carta.palo
            valores.append(valor)
            palos.append(palo)

        valor_carta = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

        # Evaluo cada mano y le asigno un numero de prioridad

        # CARTA MAS ALTA
        valores_unicos = set(valores)
        if len(valores_unicos) == 5:
            valores_ordenados = sorted(valores, reverse=True)
            carta_mas_alta = valores_ordenados[0]
            return 10

        # UN PAR
        for valor in valores:
            if valores.count(valor) == 2:
                return 9

        # DOS PARES
        pares = set()
        for valor in valores:
            if valores.count(valor) == 2:
                pares.add(valor)
        if len(pares) == 2:
            return 8

        # TRES CARTAS IGUALES
        for valor in valores:
            if valores.count(valor) == 3:
                return 7

        # ESCALERA
        valores_ordenados = sorted(valores, key=lambda x:valor_carta[x], reverse=True)
        valores_unicos = sorted(list(set(valores_ordenados)), key=lambda x: valor_carta[x], reverse=True)
        if len(valores_unicos) == 5:
            indices = [valor_carta[valor] for valor in valores_unicos]
            if indices[0] - indices[4] == 4:
                return 6

        # COLOR
        if len(set(palos)) == 1:
            return 5

        # FULL HOUSE
        valores_unicos = set(valores)
        if len(valores_unicos) == 2:
            for valor in valores_unicos:
                if valores.count(valor) == 3:
                    return 4

        # PÓKER
        for valor in valores:
            if valores.count(valor) == 4:
                return 3

        # ESCALERA DE COLOR
        valores_ordenados = sorted(valores, key=lambda x: valor_carta[x], reverse=True)
        if len(set(palos)) == 1:
            indices = [valor_carta[valor] for valor in valores_ordenados]
            if indices[0] - indices[4] == 4:
                return 2

        # ESCALERA REAL
        if set(valores) == {'10','J','Q','K','A'} and len(set(palos)) == 1:
            return 1
    def verificarFinRonda(self):
        if self.turno_actual == 0:  # Se verifica al finalizar un ciclo de turnos
            self.ronda_actual += 1
    def actualizarApuesta(self, apuesta):
        self.apuesta_actual = max(apuesta, self.apuesta_actual)

    def avanzarTurno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

    def iniciarJuegoCompleto(self):
        self.iniciarJuego()
        while True:
            if self.hayJugadoresActivos():
                jugador = self.jugadores[self.turno_actual]
                if jugador.estaJugando:
                    apuesta = jugador.turno(self.apuesta_actual)
                    self.actualizarApuesta(apuesta)
                    self.avanzarTurno()
            else:
                break

    def hayJugadoresActivos(self):
        for jugador in self.jugadores:
            if jugador.estaJugando and jugador.fichas > 0:
                return True
        return False