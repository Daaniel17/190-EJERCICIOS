import getpass

def validar():
    datos = {"jaime" : "jaime21", "oscar" : "flowkbron", "natalia" : "2345"}
    usuario=input("Ingrese su usuario: ")
    if usuario in datos:        
        contraseña=getpass.getpass("Ingrese su contraseña: ")
    
        if datos.get(usuario) == contraseña:
            print("Acceso valido")
    
        else:
            print("Contraseña incorrecta, vuelva a intentarlo.")
            print(" ")
            validar()
    else:
         print("Usuario no encontrado.")
         validar()

validar()



