texto=input("Ingrese el texto: ")

contador=0

for i in texto:
    if i.isupper():
        contador += 1

print(contador)