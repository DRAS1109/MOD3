def Contar(n):
    if n == 100:
        return n
    return Contar(n + 1)

print (Contar (10))