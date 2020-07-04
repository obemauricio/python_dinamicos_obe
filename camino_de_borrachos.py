import random
from bokeh.plotting import figure, show
class Borracho: 
    
    def __init__(self, nombre): 
        self.nombre = nombre
    
class BorrachoTradicional(Borracho):  # clase base, genera un contructor con init
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self): # camina aleatoriamente entre 4 opciones
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) #choice permite generar varias opciones que tienen la misma probabilidad

        
