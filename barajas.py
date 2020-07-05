import random
import collections

PALOS = ["espada", "corazon", "rombo", "trebol"]
VALORES = ["as", "2", "3", "4", "5", "6", "8", "9", "10", "jota", "reina", "rey"]

def crear_baraja():
    baraja = []
    for palos in PALOS:
        for valor in VALORES:
            baraja.append((palos, valor))
    
    return baraja
def obtener_mano(barajas, tamaño_mano):
    #random sample me permite obtener muestras de manera aleatoria, pero al sacar otra muestra no obtiene duplicados
    mano = random.sample(barajas, tamaño_mano)

    return mano

def main(tamaño_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamaño_de_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
                
    probabilidad_par = pares / intentos
    print(f"La probabilidad de obtener un par en una mano de {tamaño_mano} barajas es {probabilidad_par}")
if __name__ == "__main__":
    tamaño_de_mano = int(input("De cuantas barajas sera la mano?: "))
    intentos = int(input("Cuantos intentos para calcular la probabilidad?: "))

    main(tamaño_de_mano, intentos)