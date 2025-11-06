def maximo (t):
    v = t[0]
    for e in t:
        if e >= v:
            v = e
    return v 
        
t = [1, 5, 4, 9, 2, 10, 3, 6, 7, 11, 14]

num_max = maximo(t)

print (f"El valor máx de {t} es {num_max}")