class Cohete: 
    def __init__(self, proyecto, destino):
        self.ancho=5 #metros
        self.alto=30 #metros
        self.proyecto= proyecto
        self.destino=destino
        self.jefe_proyecto=" "
    
    def asignar_jefe_proyecto(self, responsable):
        self.jefe_proyecto = responsable

    def cambiar_alto(self, nuevo_alto):
        self.alto = nnuevo_alto
    
    def cambiar_destino(self, nuevo_destino):
        self.destino = nuevo_destino

fenix2020 = Cohete("Armagedon", "Marte")
fenix2020.asignar_jefe_proyecto("Crstihian")
print(f"El destino del Cohete es {fenix2020.destino}")
print(f"El jefe del proyecto e {fenix2020.jefe_proyecto}")
print(f"tamaño de la nave {fenix2020.ancho} x {fenix2020.alto}")
