from Juego import *
from Podio import Podio

juego = Juego() # Crear objeto Juego e iniciarlo (identificarlo)

jugadores = False 
while not jugadores:
    jugadores = juego.Crear_Jugadores()                    # Crear jugadores, conductores
    
contenedor_victorias = juego.Crear_Contenedor_Victorias()  # Crear contenedor que almacenará los resultados totales del podio
jugar = True
while jugar:
    pista, distancia = juego.Crear_Pista()                 # Crear pista 
    carriles = juego.Crear_Carriles(jugadores, distancia)  # Crear carriles
    carros = juego.Crear_Carros(carriles)                  # Crear carros
    conductores = juego.Crear_Conductores(carros)          # Crear conductores
    indices = list(range(len(carros)))                     # Lista de índices de cada carro (será utilizada para asignar turnos)
    ganadores = []                                         # Lista que contendrá los carros ganadores
    juego.Inicio_Carrera()                                 # Dar aviso del inicio de la carrera
      
    while True:
        turnos = juego.Turnos_Carro(indices)                                # Asignar turnos aleatorios de juego para los carros
        juego.Mover_Carros(carros, turnos, distancia, ganadores, indices)   # Avanzar cada carro por turno (el lanzamiento del dado está implícito en este método)
        if len(ganadores) == 3:
            print ('La carrera ha terminado!')
            podio = Podio(ganadores)                            # Crear podio con los ganadores de la carrera actual
            podio.Imprimir_Podio()                              # Imprimir resultados del podio de la carrera actual
            podio.Agregar_Victorias(contenedor_victorias)       # Registrar los resultados del podio para el archivo final
            jugar = juego.Nueva_Carrera()                       # Verificar si el jugador desea correr una nueva carrera
            break


nombres_jugadores, nombres_conductores = juego.Nombres_Jugadores_Conductores(jugadores)   # Crear listas con nombres de los jugadores y nombres de conductores
counters = juego.Counter_Victorias(contenedor_victorias)                                  # Crear Counter de resultados totales del podio
victorias = juego.Conteo_Victorias(nombres_conductores, counters)                         # Contar resultados para cada conductor
datos_finales = juego.Crear_Dicc(nombres_jugadores, nombres_conductores, victorias)       # Crea diccionario de los resultados para crear DataFrame y archivo csv
juego.Fin_Juego(datos_finales)                                                            # Acaba juego, imprime DataFrame y genera archivo csv
