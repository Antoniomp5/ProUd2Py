import random
ns = list(range(100))
aes = random.sample(ns, 5)

num = int(input("Introduce el Nº a buscar: "))

try:
    pos = aes.index(num)
    print(f"El array generado es {aes} y el {num} se ecuentra ahí")
except ValueError:
    print(f"{num} no se encuentra en {aes}")