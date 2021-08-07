class Carril():
    '''
    La clase carril estará asociada con la clase Carro, pues cada carro va ubicado en un carril. 
    '''
    def __init__(self, distancia, nombre_conductor, num_carril):
        self.distancia = distancia
        self.conductor = nombre_conductor
        self.numero = num_carril
        