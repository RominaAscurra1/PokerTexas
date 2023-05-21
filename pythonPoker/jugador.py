class Jugador:
    def __init__(self, nombre, fichas, esBot):
        self.mano = []
        self.esBot = esBot
        self.nombre = nombre
        self.fichas = fichas

    # metodo de jugador para recibir su mano de cartas. Exactamente 5 cartas
    def recibirMano(self, cartas):
        if len(cartas) == 5:
            self.mano = cartas
        else:
            print("El jugador recibio un numero incorrecto de cartas")

    # metodo para mostrar las cartas que tiene en la mano el jugador
    def mostrarMano(self):
        for carta in self.mano:
            print(carta.valor, carta.palo)

    # metodo que ejecuta el metodo correspondiente si es un humano o bot
    def turno(self, minimo):
        apuesta = 0
        if self.esBot:
            apuesta = self._turnoBot(minimo)
        else:
            apuesta = self._turnoHumano(minimo)
        return apuesta

    # falta

    def _turnoBot(self, minimo):
        # TODO: Implementar la logica de apuesta del bot
        return 0

    # metodo de ingreso de apuesta
    def _turnoHumano(self, minimo):
        jugadaValida = False
        apuesta = 0
        print("[Tu turno", self.nombre, "]")
        while not jugadaValida:
            text = input("Cuanto deseas apostar?\n- Apuesta minima de " + str(minimo) + "\n- 0 para retirarse\n")
            if not text.isdigit():
                print("Apuesta invalida. Vuela a intentarlo!")
            else:
                apuesta = int(text)
                if apuesta < 0 or (apuesta < minimo and apuesta != 0):
                    print("Apuesta invalida. Vuelva a intentarlo!")
                else:
                    if self.fichas < apuesta:
                        print("Apuesta invalida. No se tienen las fichas suficientes. Vuelva a intentarlo!")
                    else:
                        if apuesta == 0:
                            print("Se retira del juego!")
                        else:
                            print("Apuesta realizada con exito")
                        self.descontarFichas(apuesta)
                        return apuesta

    # metodo para descontar fichas
    def descontarFichas(self, apuesta):
        print("Se descontaran", apuesta, "fichas del jugador", self.nombre)
        self.fichas = self.fichas - apuesta