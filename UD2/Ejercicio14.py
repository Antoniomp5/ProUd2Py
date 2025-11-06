inventario = ["Manzanas", "Platanos", "Naranjas", "Peras"]
#Llegada de mercancia .append()
k = "Kiwi"
u = "Uva"
k = inventario.append(k)
u = inventario.append(u)
print(inventario)
m = ["Melón1", "Melón2", "Melón3"]
inventario.extend(m)
print(inventario)

#Reorganización .insert()
pf = "Platanos frescos"
pf = inventario.insert(2, pf)
print(inventario)

#Venta y descarte .pop() y .remove()
inventario.pop(-1)
print(inventario)
inventario.remove("Peras")
print(inventario)

#Reporte de emergencia [*, *] o [][]
emergencia = inventario[0][4]
for e in emergencia:
    print(e)


