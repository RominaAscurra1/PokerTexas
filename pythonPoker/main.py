from poker import Poker
from jugador import Jugador


if __name__ == '__main__':

    poker = Poker()  # Se crea un objeto de la clase Poker

    poker.iniciarJuego()
    poker.evaluarManos(poker.jugadorReal)  # Le paso como parametro un jugador para que evalue su mano

