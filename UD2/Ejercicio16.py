import random
def busquedabi(lista, num):
    i = 0
    d = len(lista) -1
    
    while i <= d:
        med = (i + d) // 2
        if lista[med] == num:
            return med
        elif lista[med] < num:
            i = med + 1
        else:
            d = med - 1
    return -1


ns = [0, 10 ,20, 30, 40, 50, 60, 70, 80, 90]

num = int(input("Introduce el Nº a buscar: "))

res = busquedabi(ns, num)
    
    
print(f"El array generado es {ns} y el {num} se ecuentra en la posición {res}")
