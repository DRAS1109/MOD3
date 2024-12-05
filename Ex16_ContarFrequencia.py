"""
Para cada letra do alfabeto portugues, indique o nº de vezes que aparece na frase
Todos os caracteres que não existirem no alfabeto portugues nao deverão ser contados
O maximo de caracteres que a frase pode ter é 200
ord a-z = chr 97-122
"""

def Frase():
    Frase = input("Introduza uma frase: ")
    return Frase.lower()

def N_Caracteres(Frase):

    #Percorrer todas as letras do alfabeto
    for X in range (97, 122 + 1):

        #Reiniciar a variavel Contar
        Contar = 0

        #Percorrer todas as letras da frase e contar as vezes que essa letra apareceu
        for i in Frase:
            if ord(i) == X:
                Contar += 1
        if Contar > 0:
            print (f"A função tem {Contar} letras {chr(X)}")

def main():
    frase = Frase()
    N_Caracteres(frase)

if __name__ == "__main__":
    main()