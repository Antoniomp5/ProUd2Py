#lista_a = [30, 40, 50]
#lista_b = [30, 40, 50]
#lista_c = [40, 30, 50] # Mismos elementos, orden diferente
#lista_d = [30, 40]     # Longitud diferente

#print(f"A == B: {lista_a == lista_b}") # True
#print(f"A == C: {lista_a == lista_c}") # False (el orden importa)
#print(f"A == D: {lista_a == lista_d}") # False (la longitud importa)

#TODO: Algoritmo que dice si dos arrays son iguales
def iguales(lista1, lista2):
    if len(lista1) != len(lista2):
        res = False
    else:
        for e in lista1:
            if lista1 != lista2:
                res = False
            else:
                res = True

    #TODO: retorna un valor boleano
    return res

lista_a = [30, 40, 50]
lista_b = [30, 40, 50]

print(f"A == B: {iguales(lista_a, lista_b)}")

lista_a = [30, 40, 50]
lista_c = [40, 30, 50]

print (f"A == C: {iguales(lista_a, lista_c)}")

lista_a = [30, 40, 50]
lista_d = [30, 40]

print (f"A == D: {iguales(lista_a, lista_d)}")
