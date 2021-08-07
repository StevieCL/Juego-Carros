
from Jugador import Jugador
from Pista import Pista
from Carril import Carril 
from Carro import Carro
from Conductor import Conductor
import random
from collections import Counter
import pandas as pd

class Juego():
    
    def __init__(self): 
        self.identificador = input('Escribe un identificador para tu juego: ')
       
       
    def Nuevo_Jugador(self) -> object:
        '''
        - Devuelve un nuevo jugador (objeto)
        - Imprime el nombre de conductor del jugador
        '''
        nombre_jugador = input('Escribe tu nombre: ')
        nombre_conductor = nombre_jugador + ' Kart'
        print ('Tu nombre de conductor será', nombre_conductor)
        nuevo_jugador = Jugador(nombre_jugador, nombre_conductor)
    
        return nuevo_jugador
    
    
    def Crear_Jugadores(self) -> list:    
        '''
        Devuelve una lista que contendrá los jugadores (objetos) que se registren en el juego
        '''    
        lista_jugadores = []    
        while True: 
            preg = input('Deseas crear un nuevo jugador? (si/no): ')       
            if preg in ['si', 'SI', 'Si', 'Sí']:
                player = self.Nuevo_Jugador()
                lista_jugadores.append(player)   # Lista de jugadores                              
            else:
                verif = self.Verificar_Jugadores(lista_jugadores)
                if verif: break
        
        return lista_jugadores
        
        
    def Verificar_Jugadores(self, lista_jugadores) -> bool:  
        '''
        Verifica que se haya registrado al menos 3 jugadores en el juego
        '''
        if len(lista_jugadores) >= 3:
            return True
        else:
            print ('Debe haber al menos 3 jugadores registrados para iniciar una carrera!')  
            return False 
        
        
    def Crear_Pista(self) -> object:
        '''
        Devuelve un objeto 'pista' que ya tiene una distancia definida como atributo
        '''    
        while True:
            dist = float(input('Digita la distancia (km) en la que deseas la pista: '))  
            if dist > 0: break
            else: print ('Debe ser un número positivo para poder competir en la carrera!')
            
        pista = Pista(dist)
           
        return pista, dist
    
    
    def Crear_Carriles(self, lista_jugadores:list, distancia:float) -> list:
        '''
        - Devuelve una lista de carriles (objetos) por cada jugador (conductor) registrado.
    
        - Cada carril ya está asociado con cada jugador; el orden de las listas jugadores (lista_jugadores)
        y carriles son equivalentes
        '''
        carriles = []   
        for ind in range(len(lista_jugadores)):
            carril = Carril(distancia, lista_jugadores[ind].conductor, ind)
            carriles.append(carril)
               
        return carriles
    
    
    def Crear_Carros(self, carriles:list) -> list:      
        '''
        Devuelve una lista de carros (objetos)
        '''    
        carros = []
        for carril in carriles: 
            carro = Carro(carril.conductor, carril.numero)
            carros.append(carro)
        
        return carros
    
    
    def Crear_Conductores(self, carros) -> list:
        '''
        Devuelve una lista de conductores (objetos)
        '''
        conductores = []
        for  carro in carros:
            conductor = Conductor(carro.conductor, carro)
            conductores.append(conductor)
            
        return conductores
    
    
    def Crear_Contenedor_Victorias(self) -> dict:
        '''
        Devuelve un diccionario que servirá como contador de los jugadores en cada puesto del podio
        '''
        contenedor_victorias = {'Primer puesto':[],
                            'Segundo puesto':[],
                            'Tercer puesto':[]} 
        
        return contenedor_victorias
    
    
    def Separador(self):
        '''
        Imprime una línea que será útil para separar impresiones del programa
        '''
        print ('-'*50)
    
     
    def Inicio_Carrera(self):
        '''
        Imprime el aviso del inicio de la carrera
        '''
        self.Separador()
        print ('EN SUS MARCAAAAAAAAAS...!')
        print ('LISTOOOOOS...!')
        print ('FUERAAAAAAAAAAAAAAAAAAAA...!!!!!!!!!!!')
        self.Separador()
        
                
    def Lanzar_Dado(self) -> int:
        '''
        Devuelve un entero que equivale a los metros que recorre un carro en un turno
        '''
        dado = random.randint(1, 6)
        metros = dado*100
        print ('El número del dado es', dado)  
             
        return metros
        
        
    def Turnos_Carro(self, indices) -> list:
        '''
        Devuelve una lista con las posiciones de los carros puestas aleatoriamente
        '''
        turnos = indices.copy()
        random.shuffle(turnos)
        return turnos
        
        
    def Mover_Carros(self, carros, turnos, dist, ganadores, indices):
        '''
        - Mueve cada carro (según posición originada por Turnos_Carro())
        - Verifica si ya existen tres carros en el podio
        '''
        for turno in turnos:
            self.Separador()
            print ('Es el turno del carro ', turno)
            metros = self.Lanzar_Dado()
            print ('El carro', turno,'del conductor', carros[turno].conductor, 'avanza', metros, 'metros!')
            self.Separador()
            carros[turno].Avanzar(metros/1000)
            indices = self.Verificar_Ganador(carros[turno], dist, ganadores, indices, turno)
            if len(ganadores) == 3: break
           
                                  
    def Verificar_Ganador(self, carro, dist, ganadores, indices, turno) -> list:
        '''
        - Verifica si un carro ya llegó a la meta
        - Si algún carro ya llegó a la meta, elimina la posición del mismo y devuelve la lista de posiciones (indices) sin ella
        '''
        if carro.recorrido >= dist:
            print ('El carro', turno, 'del conductor', carro.conductor, 'HA LLEGADO A LA METAAAAA!!!!!!!!')
            self.Separador()
            ganadores.append(carro)
            indices.remove(turno)
        
        return indices
    
    
    def Counter_Victorias(self, contenedor_victorias) -> list:
        '''
        Devuelve una lista que contiene Counters que cuentan las veces que un jugador quedó en primer, segundo y tercer puesto
        '''
        counters = []
        for puesto in contenedor_victorias:
            counter = Counter(contenedor_victorias[puesto])
            counters.append(counter)
        
        return counters
    
    
    def Nueva_Carrera(self) -> bool:
        '''
        Devuelve un booleano que servirá para definir si se juega o no una nueva carrera
        '''
        new = input('Deseas empezar una nueva carrera? (si/no): ') 
        if new in ['si', 'SI', 'Sí', 'Si']: 
            jugar = True
        else: 
            jugar = False
        
        return jugar
            
    
    def Nombres_Jugadores_Conductores(self, lista_jugadores) -> list:
        '''
        Devuelve dos listas: una con los nombres de los jugadores y la otra con los nombres de los conductores
        '''
        nombres_jugadores = []
        nombres_conductores = []
        for jugador in lista_jugadores: 
            nombres_jugadores.append(jugador.nombre)
            nombres_conductores.append(jugador.conductor)
        
        return nombres_jugadores, nombres_conductores
    
    
    def Conteo_Victorias(self, nombres_conductores, counters) -> list:
        '''
        Devuelve una lista que a su vez contiene tres listas: están ordenadas según el podio, donde las posiciones de la lista (0, 1, 2) 
        corresponden a los puestos del podio (1,2,3). En cada sublista están las veces en las que un conductor quedó en tal puesto del podio.
        La organización de los elementos de la sublista es equivalente al orden de los conductores o jugadores en las listas que contienen sus 
        nombres. 
        '''
        victorias = [[], [], []]
        for ind in range(len(counters)):
            for conductor in nombres_conductores:
                (victorias[ind]).append((counters[ind])[conductor])
        
        return victorias
    
    
    def Crear_Dicc(self, nombres_jugadores, nombres_conductores, victorias) -> dict:
        '''
        Devuelve un diccionario con los datos (podio) del juego
        '''      
        datos_finales = {
        'Jugadores': nombres_jugadores,
        'Conductores': nombres_conductores,
        'Primer puesto': victorias[0],
        'Segundo puesto': victorias[1],
        'Tercer puesto': victorias[2]
        }
        self.Separador()
        self.Separador()
        
        return datos_finales
    
    
    def Fin_Juego(self, datos_finales):
        '''
        - Imprime DataFrame (Pandas) con los nombres de los jugadores y conductores y su respectivo conteo en el podio
        - Genera archivo csv con tal información
        '''
        df = pd.DataFrame(datos_finales)
        print ('TABLA DE PUNTAJES POR PUESTO EN EL PODIO!!!!\n')
        print (df,'\n')
        name = 'Datos_'+self.identificador+'.csv'
        df.to_csv(name, index=False)
        print('Se ha creado un archivo csv llamado',name,'con los datos del juego. \nEspero te haya ENCANTADO el juego, nos vemos pronto!!!')