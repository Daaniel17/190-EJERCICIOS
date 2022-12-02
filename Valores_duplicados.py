def valores(x):
    cantidad=len(x)
    duplicados=[]

    for i in range(cantidad):
        n=i+1
        for a in range(n,cantidad):
            if x[i]==x[a] and x[i] not in duplicados:
                duplicados.append(x[i])
    return duplicados

nombres=["Daniel","Winston","Ayda","Nelson","Daniel"]

print(valores(nombres))