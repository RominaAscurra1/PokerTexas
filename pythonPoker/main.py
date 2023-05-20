from juego import repartir_cartas
from pythonPoker.jugador import Jugador

if __name__ == '__main__':
    num_jugadores = 4
    num_cartas = 5
    manos = repartir_cartas(num_jugadores, num_cartas)

    for i, mano in enumerate(manos):
        print(f'Jugador {i+1} mano:')
        for carta in mano:
            print(carta)


