def esPrimo():
    numero = 0
    if numero <= 1:
        return False
    if numero == 2:
        return True
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1
    return True


num = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
primo = []
print(f"La lista de los 10 primeros N.º {num}")
i = 0
while i < len(num[i]):
    if esPrimo(num[i]):
        primo.append(num.pop(num[i]))
    else:
        i += 1


print(f"La lista de los primeros primos {primo}")