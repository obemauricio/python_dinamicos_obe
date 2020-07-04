class libro: 
    def __init__(self, titulo, autor, editorial, paginas, formato, existencias):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.paginas = paginas 
        self.formato = formato
        self.existencias = existencias
    
    def consultar_existencias(self):
        return self.existencias
    
    def actualizar_existencias(self, unidades, operacion):
        if operacion == "compra":
            self.existencias += unidades
        
        elif operacion == "venta" :
            self.existencias -= unidades
    def imprimir_datos(self): 
        print(self.titulo)
        print(self.autor)
        print(self.editorial)
        print(self.paginas)
        print(self.formato)
        print(self.existencias)

tokio_blues = libro("tokio Blues", "haruki murakami", "Busquets", 458, "pasta blanda", 55)
tokio_blues.actualizar_existencias(1,"venta")
tokio_blues.actualizar_existencias(10,"compra")
tokio_blues.imprimir_datos()

## las existencias fueron modificadas ya que habian 55 pero luego vendieron 1 por 
## lo que quedo 54 pero luego aumentaron stock a 64 porque compraron 10