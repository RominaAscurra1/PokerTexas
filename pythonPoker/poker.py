from mazo import Mazo
from jugador import Jugador

class Poker:  # inicializo la clase Poker
    def __init__(self):
        self.mazo = Mazo()
        self.turno_actual = 0  # Agregamos el atributo turno_actual e inicializamos en 0
        self.apuesta_actual = 10  # Agregamos el atributo apuesta_actual e inicializamos en 0

    usuario = input("Ingrese un nombre de usuario: ")  # Ingresa el nombre de usuario el jugador

    # Se crean otros 4 jugadores bots que compiten con el usuario
    jugadorReal = Jugador(usuario, 100, False)
    bot1 = Jugador("Bot 1", 100, True)
    bot2 = Jugador("Bot 2", 100, True)
    bot3 = Jugador("Bot 3", 100, True)
    bot4 = Jugador("Bot 4", 100, True)

    jugadores = [jugadorReal, bot1, bot2, bot3, bot4]

    def iniciarJuego(self):
        for jugador in self.jugadores:
            self.mazo.mezclar()
            jugador.recibirMano(self.mazo.repartir(5))
            print(" ")
            print(jugador.nombre, "  Fichas: ", jugador.fichas)
            cont = 1

            for carta in jugador.mano:
                if not jugador.esBot:
                    print(carta.palo, end=" ")
                    print(carta.valor, end=", ")

                if cont == 5:
                    print(" ")
                cont = cont + 1

            if not jugador.esBot:
                jugador.fichas = self.jugadorReal.fichas

    def verificarFinRonda(self):
        if self.turno_actual == 0:  # Se verifica al finalizar un ciclo de turnos
            self.ronda_actual += 1

    def actualizarApuesta(self, apuesta):
        self.apuesta_actual = max(apuesta, self.apuesta_actual)
        jugador = self.jugadores[self.turno_actual]
        if not jugador.esBot:
            jugador.fichas -= apuesta
    def avanzarTurno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

    def mostrarResultadosFinales(self):
        print("---------- Resultados finales ----------")
        for jugador in self.jugadores:
            print(f"{jugador.nombre}: {jugador.fichas} fichas")
        print("----------------------------------------")

    def iniciarJuegoCompleto(self):
        self.iniciarJuego()
        juegoEnCurso = True
        while juegoEnCurso:
            if self.hayJugadoresActivos():
                jugador = self.jugadores[self.turno_actual]
                if jugador.estaJugando:
                    apuesta = jugador.turno(self.apuesta_actual)
                    self.actualizarApuesta(apuesta)
                    self.avanzarTurno()
                    if not jugador.estaJugando and jugador == self.jugadorReal:
                        juegoEnCurso = False
            else:
                break
        self.mostrarResultadosFinales()
    def hayJugadoresActivos(self):
        for jugador in self.jugadores:
            if jugador.estaJugando and jugador.fichas > 0:
                return True
        return False

    def seleccionarGanador(self):  # Selecciona el ganador de la ronda
        jugadores_cartas = {}  # Creo un diccionario que contiene un numero asociado a al jugador, sus cartas y la mano que le toco
        cont = 0

        for jugador in self.jugadores:
            cartas = []

            for carta in jugador.mano:
                cartas.append(carta.valor)

            jugadores_cartas[cont] = [cartas, self.evaluarManos(jugador)]
            cont += 1

            jugadores_cartas = self.asignar_valor(jugadores_cartas)  # Le asigno numero a las cartas con letras

        ganadores = []  # Creo una lista con posibles ganadores
        ganador_final = None

        min_prioridad = min(jugadores_cartas.values(), key=lambda x: x[1])[
            1]  # Determino cual es la mejor mano de la ronda
        for jugador, (mano, prioridad) in jugadores_cartas.items():
            if prioridad == min_prioridad:
                ganadores.append(jugador)  # Guardo en ganadores los jugadores con la misma mano ganadora

        if not ganadores:
            print("No hay ganadores.")
        else:
            if len(ganadores) == 1:  # Si hay un solo jugador guardado ese es el ganador
                ganador_final = ganadores[0]
            else:
                if ganadores:  # Si hay mas de un posible ganador defino quien tiene las cartas mas altas
                    ganadores.sort(key=lambda x: self.comparar_cartas(x, jugadores_cartas), reverse=True)
                    ganador_final = ganadores[0]

        print("El ganador es: ", ganador_final)

    def comparar_cartas(self, jugador, jugadores_cartas):  # En el caso de empate define las cartas mas altas
        mano = jugadores_cartas[jugador][0]
        prioridad = jugadores_cartas[jugador][1]

        if prioridad == 9:  # Un Par
            par = max(set(mano), key=mano.count)
            return par
        elif prioridad == 8:  # Dos Pares
            pares = [carta for carta in set(mano) if mano.count(carta) == 2]
            return max(pares)
        elif prioridad == 7:  # Trio
            trio = max(set(mano), key=mano.count)
            return trio
        elif prioridad == 6:  # Escalera
            mano_ordenada = sorted(mano, reverse=True)
            if all(mano_ordenada[i] - 1 == mano_ordenada[i + 1] for i in range(4)):
                return max(mano)
        elif prioridad == 4:  # Full House
            trio = max(set(mano), key=mano.count)
            par = min(set(mano), key=mano.count)
            return max(trio, par)
        elif prioridad == 3:  # Poker
            poker = max(set(mano), key=mano.count)
            return poker
        elif prioridad == 2:  # Escalera de color
            mano_ordenada = sorted(mano, reverse=True)
            if all(mano_ordenada[i] - 1 == mano_ordenada[i + 1] for i in range(4)):
                return max(mano)

        return max(mano)

    def asignar_valor(self, jugadores_cartas):  # Metodo que asigna numeros a los valores de las cartas que son letras
        mapeo_cartas = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
                        "K": 13, "A": 14}

        for jugador, datos in jugadores_cartas.items():
            cartas = datos[0]
            cartas_convertidas = []

            for carta in cartas:
                if isinstance(carta, int):
                    valor = carta
                else:
                    valor = mapeo_cartas[carta]

                cartas_convertidas.append(valor)

            datos[0] = cartas_convertidas

        return jugadores_cartas


def evaluarManos(valores, palos):
    valor_carta = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}

    valores_unicos = set(valores)
    valores_ordenados = sorted(valores, key=lambda x: valor_carta[x], reverse=True)

    # Evaluo cada mano y le asigno un numero de prioridad

    # CARTA MAS ALTA
    if len(valores_unicos) == 5:
        return 10

    # UN PAR
    pares = [valor for valor in valores_unicos if valores.count(valor) == 2]
    if len(pares) == 1:
        return 9

    # DOS PARES
    if len(pares) == 2:
        return 8

    # TRES CARTAS IGUALES
    for valor in valores_unicos:
        if valores.count(valor) == 3:
            return 7

    # ESCALERA
    if len(valores_unicos) == 5 and valor_carta[valores_ordenados[0]] - valor_carta[valores_ordenados[4]] == 4:
        return 6

    # COLOR
    if len(set(palos)) == 1:
        return 5

    # FULL HOUSE
    if len(valores_unicos) == 2:
        for valor in valores_unicos:
            if valores.count(valor) == 3:
                return 4

    # PÓKER
    for valor in valores_unicos:
        if valores.count(valor) == 4:
            return 3

    # ESCALERA DE COLOR
    if len(set(palos)) == 1 and valor_carta[valores_ordenados[0]] - valor_carta[valores_ordenados[4]] == 4:
        return 2

    # ESCALERA REAL
    if set(valores) == {'10', 'J', 'Q', 'K', 'A'} and len(set(palos)) == 1:
        return 1
