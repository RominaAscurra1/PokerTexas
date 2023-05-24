import random
class Jugador:
    def __init__(self, nombre, fichas, esBot):
        self.mano = []
        self.esBot = esBot
        self.nombre = nombre
        self.fichas = fichas
        self.estaJugando = True
        self.apuestaJugador=0;#variable que acumula apuesta del jugador
        self.apuestaBot = 0;  # variable que acumula la apuesta del bot
        self.ganador = poker.seleccionarGanador()

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

    def _turnoBot(self, minimo): #Metodo momentaneo, lo hice para poder avanzar con el del humano
        apuesta = 0
        if minimo == 0:
            apuesta = random.randint(0, 10) * 10  # Apuesta aleatoria entre 0 y 100 (múltiplos de 10)
            self.apuestaBot += apuestaBot  # Acumula las apuestas
        else:
            if minimo > self.fichas:
                apuesta = 0  # El bot no tiene suficientes fichas, se retira
            else:
                apuesta = minimo + random.randint(0,
                                                  5) * 10  # Apuesta aleatoria entre la apuesta mínima y la apuesta mínima + 50
        if apuesta > self.fichas:
            apuesta = self.fichas  # Si el bot no tiene suficientes fichas, apuesta todo su saldo
        self.descontarFichas(apuesta)
        print("[Turno del bot ", self.nombre, "]")
        print("El bot ", self.nombre, " apuesta ", apuesta)
        return apuesta

    # metodo de ingreso de apuesta
    def _turnoHumano(self, minimo):
        jugadaValida = False
        apuesta = 0
        print("Tu turno", self.nombre, "!")
        #Recuerda al jugador las cartas que tiene
        print("Tus cartas:")
        for carta in self.mano:
            print(carta.palo, end=" ");
            print(carta.valor, end=", ");
        while not jugadaValida:
            #falta agregar que muestre la mano del jugador todas las veces que se apueste
            print("");
            print ("Cantidad de fichas que tenes: ", self.fichas) #Mostramos las fichas que le quedan al jugador
            text = input("Cuanto deseas apostar?\n- Apuesta mínima de " + str(minimo) + "\n- 0 para retirarse\n")
            if not text.isdigit():
                print("Apuesta inválida. Vuelve a intentarlo!")
            else:
                self.apuestaJugador += int(text)#Acumulamos las apuestas
                apuesta = int(text) #Toma el ingreso del jugador para retirarse
                if apuesta == 0 or self.apuestaJugador == 0: #Si el jugador se queda sin fichas, termina la mano
                    self.estaJugando = False
                    print("Te has retirado del juego.")
                    return self.apuestaJugador
                elif self.apuestaJugador < minimo:
                    print("Apuesta inválida. Debes apostar al menos", minimo, "fichas.")
                elif self.apuestaJugador > self.fichas:
                    print("No tienes fichas suficientes, ¿Quieres apostar las fichas restantes o quieres retirarte?")
                else:
                    print("Apuesta realizada con éxito.")
                    self.descontarFichas(int(text))#descuenta sólo la ultima apuesta
                    return self.apuestaJugador

    # metodo para descontar fichas
    def descontarFichas(self, cantidad):
        self.fichas -= cantidad
        if self.fichas < 0:
            self.fichas = 0
    def recibirFichas(self, pozo):
        self.fichas += pozo
