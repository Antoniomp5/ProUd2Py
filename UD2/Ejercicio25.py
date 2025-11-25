#Inversor de Palabras
p = input("Introduzca una palabra: ")

if p == p[::-1]:
    print(f"{p} y {p[::-1]} son un palíndromo")
else:
    print(f"{p} y {p[::-1]} no son un palíndromo")

#Limpieza de datos
c = "juan.perez@dominio.com"
#TA
cne= c.strip(" ")
print(cne)
#TB
cnp = c.lstrip(" ")
cnf = c.rstrip(" ")
print(cnp)
print(cnf)
cs = c.split("@")
print(cs)
#TC
html = f"<h1 class = 'titulo'>Mi encabezado</h1>"
print(html)