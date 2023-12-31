import numpy as np

class Edges:
    'Clase Arisa'
    def __init__(self, source, target):
        '''
        :atrib source: origen de arista
        :atrib target: destino de arista
        :atrib weight: peso de la arista
        '''
        self.n0 = source
        self.n1 = target
        self.weight = np.random.randint(1,100)


    def __iter__(self):
        'Regresa la arista como una lista de sus atributos n0 y n1'
        yield self.n0
        yield self.n1
    

    def __eq__(self, other):
        'Compara que dos aristas sean iguales'
        if isinstance(other, Edges):
            return (self.n0 == other.n0 and self.n1 == other.n1) 
        return False
    
    def __ne__(self, other):
        'Compara aristas para evitar un digrafo'
        if isinstance(other, Edges):
            return (self.n0 == other.n1 and self.n1 == other.n0) 
        return False 
    
