def soma_quadrados(n:int): 
    import math
    Soma = 0

    for i in range(1, n + 1):
        Soma = Soma + (math.pow(i, 2))
    
    Soma = round(Soma)
    
    print(Soma)

soma_quadrados(5)