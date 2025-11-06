a = [1, 2, 3, 4]

for i in range (len(a)): # El error se ubicaba en el rango, ya que con 5 contamos desde 0 hasta 4 y
    # el array es de una longitud de 4 no de 5, cono len(a) hacemos que el array lea la longitud del mismo.
    print(a[i])