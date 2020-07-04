class Libro: 
    def __init__(self, genero, autor, fecha_publicacion):
        self.genero = genero
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.libros = 0
    
    def agregar_ejemplar(self, numero_de_libros):
        self.libros += numero_de_libros
    
    def eliminar_ejemplar(self, numero_de_libros):
        self.libros -= numero_de_libros
    
    def contar_ejemplares(self):
        return self.libros

    pandereta = Libro("novela", "Gabriel", "20-02-2000")
    aventuraenelcielo = Libro("posia", "pombo", "20-01-1999")
    pandereta.agregar_ejemplar(2)
    aventuraenelcielo.agregar_ejemplar(5)

    print(f"Del libro pandereta hay {pandereta.contar_ejemplares()} ejemplares disponibles")
    print(f"Del libro aventura en el cielo hay {aventuraenelcielo.contar_ejemplares} ejemplares disponibles")


