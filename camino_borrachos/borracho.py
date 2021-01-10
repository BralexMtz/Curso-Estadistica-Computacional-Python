import random

class Borracho:
    def __init__(self,nombre):
        self.nombre=nombre


class BorrachoTradicional(Borracho):

    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

class BorrachoDeIzquierda(Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        opciones=[(0,1),(0,-1),(1,0),(-1,0)]
        probabilidades=[0.2,0.2,0.2,0.4]
        return random.choices(opciones,probabilidades)[0]

