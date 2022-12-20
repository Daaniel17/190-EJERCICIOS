texto = "Hola como estas, hola"

texto=texto.lower()

palabras=texto.split(" ")

contador={}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

for palabra in contador:
    frecuencia=contador[palabra]
    print("la palabra",{palabra},"tiene una frecuencia de",frecuencia)