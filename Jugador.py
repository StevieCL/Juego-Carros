class Jugador():
    '''
    - Un jugador puede ser un conductor (se asocia a un conductor). 
    - No debe tener un carro asociado, es la clase Conductor quien tiene el carro asociado. 
    '''
    
    def __init__(self, nombre_jugador, conductor):
        self.nombre = nombre_jugador
        self.conductor = conductor
        