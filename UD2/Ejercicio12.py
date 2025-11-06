num = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
print(f"La lista de los 10 primeros N.º {num}")

for e in num:
    if e % 2 == 0:
        num.remove(e)

print(f"La lista de los 5 primeros impares {num}")
