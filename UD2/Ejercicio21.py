m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m)
# Apartados 1 y 2. Posición:
print(m[1][1])
print(m[1][2])
# Apartado 3. Véctor:
for f in m[1]:
    print(f, end=" ")
print()
# Apartado 4. Mátriz bidimesional completa:
for f in m:
    for e in f:
        print(e, end=" ")
    print()
    
# Apartado 5. Copia
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for fila in range(len(m)):
    for columna in range(len(m[fila])):
        if fila % 2 == 0:
            m2[fila][columna] = m[fila][columna]
            m[fila][columna] = 0
        
print("M\: ")
for fila in m:
    print(fila)
    
print("M2\: ")
for fila in m2:
    print(fila)