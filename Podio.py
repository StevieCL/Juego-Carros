class Podio(): 
    '''
    Debe contener los 3 jugadores ganadores del juego (1ro, 2do, 3ro).
    '''
    
    def __init__(self, ganadores):
        self.ganadores = ganadores
        
    def Imprimir_Podio(self): 
        
        print ('-'*50)
        print ('-'*50)
        print ('-'*10, 'GANADORES', '-'*10)
        print ('El PRIMER puesto es para', self.ganadores[0].conductor)
        print ('El SEGUNDO puesto es para', self.ganadores[1].conductor)
        print ('El TERCER puesto es para', self.ganadores[2].conductor)
        print ('-'*50)
        print ('-'*50)
        
    def Agregar_Victorias(self, contenedor_victorias):
        
        contenedor_victorias['Primer puesto'].append(self.ganadores[0].conductor)
        contenedor_victorias['Segundo puesto'].append(self.ganadores[1].conductor)
        contenedor_victorias['Tercer puesto'].append(self.ganadores[2].conductor)
