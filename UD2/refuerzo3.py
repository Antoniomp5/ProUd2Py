precios = [12.50, 45.99, 5.00, 22.75, 10.00]

# Recorrido Simple: Recorre la lista precios e imprime cada precio. Puedes usar un for-each.
for e in precios:
    print(f"Precio {e}€")
    
# Recorrido con Índice: Recorre la lista e imprime tanto el índice como el valor de cada elemento.
# Utiliza la función len() para obtener el tamaño de la lista.
for i in range (len(precios)):
    print(f"Los precios del los prductos con #{i} son {precios[i]}€")
    
# Cálculo de la Suma: Recorre la lista y calcula la suma total de todos los precios.
# Finalmente, imprime la suma.
suma_total = 0

for e in precios:
    suma_total += e

print(f"La suma total de los precios es {suma_total}")
