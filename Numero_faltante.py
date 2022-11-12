def encontrar(numeros): 
    return [x for x in range(numeros[0], numeros[-1]+1)  
                               if x not in numeros] 
  
numeros = [1, 2, 4, 6, 7, 9, 10] #Aqui se pone la lista de numeros que desee
print(encontrar(numeros))
