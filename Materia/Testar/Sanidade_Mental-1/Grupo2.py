#Grupo 2
"""
Ex 1
Cria uma função que recebe uma string e devolve verdadeiro se todas as letras da string são iguais 
e falso nos restantes casos.
"""

def LetrasIguais1(Texto:str) -> bool:
    for Letra in Texto:
        if Letra != Texto[0]:
            return False
    return True

def LetrasIguais2(Texto:str) -> bool:
    for Posição in range (len(Texto) -1):
        if Texto[Posição] != Texto[Posição + 1]:
            return False
    return True


"""
Ex 2
Cria uma função que recebe 3 valores e devolve o maior caso sejam todos positivos, 
caso sejam todos negativos deve devolver o menor. Nos seguintes casos devolve None
"""

def Maior_Menor(N1, N2, N3):
    #Qual o Maior:
    if N1 > N2:
        Maior = N1
    
    else:
        Maior = N2
    
    if N3 > Maior:
        Maior = N3

    #Qual o menor

    if N1 > N2:
        Menor = N2
    
    else: 
        Menor = N1
    
    if Menor > N3:
        Menor = N3
    
    if N1 > 0 and N2 > 0 and N3 > 0:
        return Maior
    
    elif N1 < 0 and N2 < 0 and N3 < 0:
        return Menor
    
    else:
        return None