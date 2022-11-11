import statistics
from statistics import mean
from statistics import mode,multimode

def media():
    
    n=[]
    cantidad=int(input("Cuantos valores desea agregar?: "))

    for i in range(cantidad):
        valores=int(input("Ingrese el valor: "))
        n.append(valores)
        med=mean(n)
    print("\nLa media es: ",med)

def mediana():
    n=[]
    cantidad=int(input("Cuantos valores desea agregar?: "))

    for i in range(cantidad):
        valores=int(input("Ingrese el valor: "))
        n.append(valores)
        n.sort()
        print(n)
        med=statistics.median(n)
    print("\nLa mediana es: ",med)

def moda():
    n=[]
    cantidad=int(input("Cuantos valores desea agregar?: "))

    for i in range(cantidad):
        valores=int(input("Ingrese el valor: "))
        n.append(valores)
        med=multimode(n)
    print("\nLa moda es: ",med)
    

while True:
    print("\n****Menu****")
    
    print("Que desea averiguar?: ")
    print("1. Media")
    print("2. Mediana")
    print("3. Moda")

    opc=input("Ingrese una opcion: ")

    if opc=="1":
        media()

    elif opc=="2":
        mediana()

    elif opc=="2":
        moda()

    else:
        print("\nOpcion incorrecta.")
    


    





