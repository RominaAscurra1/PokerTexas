from pythonPoker.jugador import Jugador
from pythonPoker.mazo import Mazo

if __name__ == '__main__':
    # se crea el mazo y se mezclan las cartas
    mazo = Mazo()
    mazo.mezclar()

    # se crean 4 jugadores a modo demostracion
    jugador1 = Jugador("coni", 100, False)
    jugador2 = Jugador("ro", 110, False)
    jugador3 = Jugador("flor", 105, False)
    jugador4 = Jugador("marti", 120, False)

    jugadores = [jugador1, jugador2, jugador3, jugador4]
    for jugador in jugadores:
        jugador.recibirMano(mazo.repartir(5))
        print("Mazo de", jugador.nombre)
        for carta in jugador.mano:
            print(carta.palo, carta.valor)
