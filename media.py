import random

def media(X):
    return sum(X) / len(X)

#lo que importa, si ejecutamos directamente este archivo, se ejecute main, pero ahora 
#pero ahora vamos a generar un archivo helper, y no queremos que se ejecute main cada vez que importamos

if __name__ == "__main__":
    X = [random.randint(1, 21) for i in range(20)]
    mu = media(X)
    print(X)
    print(mu)