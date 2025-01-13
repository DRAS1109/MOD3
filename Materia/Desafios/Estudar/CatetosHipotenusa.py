import math
def Hipotenusa(A, B):
    H2 = (math.pow(A, 2)) + (math.pow(B, 2))
    H = math.sqrt(H2)
    return H

print(Hipotenusa(2, 3))