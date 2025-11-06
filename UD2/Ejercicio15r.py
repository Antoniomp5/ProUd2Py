import random
#@TODO: definir función que reciba todos los parámetros

def busqueda(lista, num):
    for e in lista:
        if num == e:
            resultado = num
        else:
            resultado = -1
    return resultado
    
ns = list(range(100))
aes = random.sample(ns, 5)

num = int(input("Introduce el Nº a buscar: "))

if busqueda(aes, num) != -1:
    print(f"El array generado es {aes} y el {num} se ecuentra ahí")
else:
    print(f"{num} no se encuentra en {aes}")