from datetime import datetime
import datetime

a=int(input("Ingrese el año (0000): "))
m=int(input("Ingrese el mes (00): "))
d=int(input("Ingrese el dia (00): "))

hoy=datetime.datetime.now().date()
fecha=datetime.date(a,m,d)
edad=int((hoy-fecha).days / 365.25)
print("Usted tiene ",edad,(" años de edad."))




