import random

jugador1=input("Piedra,papel o tijera?: ").lower()
jugador2=random.choice(["Piedra", "Papel", "Tijera"]).lower()
print("Jugador 2 selecciono: ",jugador2)

if jugador1 == "piedra" and jugador2 == "papel":
    print("Jugador 2 GANA!!!")
    
elif jugador1 == "piedra" and jugador2 == "tijera":
    print("Jugador 1 GANA!!!")

elif jugador1 == "papel" and jugador2 == "piedra":
    print("Jugador 1 GANA!!!")

elif jugador1 == "papel" and jugador2 == "tijera":
    print("Jugador 2 GANA!!!")

elif jugador1 == "tijera" and jugador2 == "piedra":
    print("Jugador 2 GANA!!!")

elif jugador1 == "tijera" and jugador2 == "papel":
    print("Jugador 1 GANA!!!")

elif jugador1 == jugador2:
    print("Empate")

else:
    print("")
