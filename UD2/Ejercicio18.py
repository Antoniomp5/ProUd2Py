import Ejercicio15r
import Ejercicio16

ns = [0, 10, 20 ,30, 40, 50, 60, 70, 80, 90]
print(ns)

num = int(input("Introduce el Nº a buscar: "))

res1 = Ejercicio15r.busqueda(ns, num)
if res1 != -1:
    print(f"El array generado es {ns} y el {num} se ecuentra ahí")
else:
   print(f"{num} no se encuentra en {ns}")
    
res2 = Ejercicio16.busquedabi(ns, num)
if res2 != -1:
    print(f"El array generado es {ns} y el {num} se ecuentra ahí")
else:
   print(f"{num} no se encuentra en {ns}")

if res1 == res2:
    print("Los números selecionados coinciden")
elif res1 != res2:
    print("Los números selecionados no coinciden")