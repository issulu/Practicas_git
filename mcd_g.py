#Escribir una función que calcule el máximo común divisor entre dos números.
def mcdiv(n1, n2):
    mcdiv = 1 
    if n1 % n2 == 0:
        return n2 
    
    for k in range(int(n2/2), 0, -1): 
        if n1 % k == 0 and n2 % k == 0: 
            mcdiv = k
            break
    
    return mcdiv

print(mcdiv(16, 4))
print(mcdiv(21, 3))
print(mcdiv(16, 86))
print(mcdiv(152, 180))