texto=str(input("Ingrese la frase: "))
text=texto.split()

a=" "

for i in text:
    a = a+str(i[0]).upper()

print(a)