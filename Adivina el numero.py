from random import randint

n=randint(0,10)

def juego():
    print("Adivina el numero ganador")
    usuario=int(input("Que numero es?: "))
    if usuario>n:
        print("Menos")
        juego()
    elif usuario<n:
        print("Más")
        juego()

    elif usuario==n:
        print("FELICIDADES, ¡¡¡GANASTE!!!")
    else:
        juego()

juego()
