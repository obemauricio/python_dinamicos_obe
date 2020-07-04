"""
Este es un ejemplo cuando no usamos __init__, como se puede ver es complicado cambiar la variable contiene_borrador a True 
"""
"""
class lapiz:
    color = 'amarillo'
    contiene_borrador = False
    usa_grafito = True
    
    def dibujar(self):
        print("el lapiz esta dibujando")
    
    def borrar(self):
        if self.es_valido_para_borrar():
            print("el lapiz esta borrando")
        else:
            print("no es posible borrar")
    
    def es_valido_para_borrar(self):
        return self.contiene_borrador

lapiz_generico = lapiz()
lapiz_generico.dibujar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
"""
""" Este problema se soluciona con __init__  """
class lapiz:

    def __init__(self, color, contiene_borrador, usa_grafito):
        self.color = color
        self.contiene_borrador = False
        self.usa_grafito = True
    
    def color_lapiz(self):
        print(f"el color del lapiz es {self.color}")

    def dibujar(self):
        print("el lapiz esta dibujando")
    def borrar(self):
        if self.es_valido_para_borrar():
            print("el lapiz esta borando")
        else:
            print("no se puede borrar")
    def es_valido_para_borrar(self):
        return self.contiene_borrador

lapiz_generico = lapiz("rosado", True, True)
lapiz_generico.dibujar()
lapiz_generico.borrar()
lapiz_generico.color_lapiz()

lapiz("verde", True, False).borrar()

