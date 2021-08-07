class Conductor():
    '''
    - Debe tener un carro asociado que a su vez está asociado a un carril.
    '''
    
    def __init__(self, nombre_conductor, carro):
        self.nombre = nombre_conductor
        self.carro = carro
        