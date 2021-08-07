class Carro(): 
    '''
    - La clase Carro debe estar asociada con un conductor.
    - Debe estar sociada a un carril. 
    '''
    def __init__(self, conductor, num_carril):
        self.conductor = conductor
        self.numero_carril = num_carril
        self.recorrido = 0
        
    def Avanzar(self, km):
        self.recorrido = self.recorrido + km
        