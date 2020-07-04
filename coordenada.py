class Coordenada:

    def __init__(self, x, y): #contructor
        self.x = x
        self.y = y
    
    def mover(self, delta_x, delta_y): 
        # deltas definen cuanto se mueven a cada direccion. regresa una nueva coordenada con la suma de la coordenada actual + los cambios en delta x
        #cada que generamos un cambio creamos una nueva coordenada, es inmutable, 
        return Coordenada(self.x + delta_x, self.y + delta_y) 
        
    
    def distancia(self, otra_coordenada): # estamos en una coordenada actual y necesitamos otra coordenada, para calcular la distancia usamos pitagoras
        delta_x = self.x - otra_coordenada.x #diferencia, se calcula la distancia entre dos coordenadas.
        delta_y = self.y - otra_coordenada.y 

        return(delta_x**2 + delta_y**2)**0.5
