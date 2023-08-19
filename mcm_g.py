#Escribir una función que calcule el mínimo común múltiplo entre dos números



def mcm(n1, n2):
    k = max(n1, n2) 

    while True: 
        if (k % n1 == 0) and (k % n2 == 0): 
            return k
        
        k += 1 

print(mcm(152, 180))
