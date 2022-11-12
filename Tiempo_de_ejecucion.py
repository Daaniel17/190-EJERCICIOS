from timeit import default_timer
import math

def formula():
    farenheit= celsius*9 /5+32
def principal():
    celsius=int(input("Ingrse los grados celcius que quiere convertir a farenheit: "))
    farenheit= celsius*9 /5+32
    print(celsius," grados Celsius son: ",farenheit," grados Fahrenheit.")


inicio_programa=default_timer()
principal()
fin_programa=default_timer()

print("\nEL TIEMPO DE EJECUCION DEL PROGRAMA FUE: ",fin_programa-inicio_programa)
