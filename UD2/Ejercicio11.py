daw2 = ["Antonio", "Diego", "Carlos"] 

daw1 = ["Juan", "Nicolás", "Enrique"]

daw3 = []

print(f"El array las aulas son DAW1 = {daw1} y DAW2 = {daw2}")

daw3.extend(daw1)
daw3.extend(daw2)

print(f"Ahora solo existe DAW3 {daw3}")