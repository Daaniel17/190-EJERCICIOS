lista = [[1, 4, 5], [4, 6, 8], [8, 3, 10]] 
    
grupo = [list(x) for x in zip(*lista)] 
  
print ("Los elementos del mismo indice son: " + str(grupo))
