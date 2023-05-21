from mazo import Mazo

# def repartir_cartas(num_jugadores, num_cartas):
#     mazo = Mazo()
#     mazo.mezclar() #llamo al método de la clase Mazo para mezclar la baraja
#     manos = [] #creo el arreglo para guardar las manos de todos los jugadores
#     for i in range(num_jugadores): #se realiza la cantidad de jugadores que juegan la ronda
#         mano = mazo.repartir(num_cartas) #a cada jugador se le reparte la cantidad de cartas indicadas
#         manos.append(mano) #en el arreglo de todas las manos de los jugadores se guarda cada mano individual
#     return manos