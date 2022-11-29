from difflib import SequenceMatcher

texto1=input("Introduzca el primer texto: ")
texto2=input("Introduzca el segundo texto: ")

similitud=SequenceMatcher(None,texto1,texto2).ratio()
print(f"Ambos son {similitud * 100} % similares")