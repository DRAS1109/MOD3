import Utils

def Quadrante():
    #Cria uma imagem de um quadrante
    Quadrante = """
    2 | 1 
   ---+---
    3 | 4
    """
    print (Quadrante)

def Ler_Posição():
    #Lê as coordenadas
    X = Utils.Ler_Inteiro ("Qual o valor de X \n Ex: -50: ")
    Y = Utils.Ler_Inteiro ("Qual o valor de Y \n Ex: -40: ")
    yield X
    yield Y

def Identificar_Posição(X, Y):
    #Identifica a que quadrante pertence
    if X == 0 or Y == 0:
        if X == 0 and Y == 0:
            Quadrante = 0
        else:
            Quadrante = 5
    else:
        if X > 0:
            if Y > 0:
                Quadrante = 1
            
            else:
                Quadrante = 2

        elif X < 0:
            if Y < 0:
                Quadrante = 3
            
            else: 
                Y > 0
                Quadrante = 4
    
    return Quadrante

def Escrever_Posição(Quadrante):
    #Chama a função Quadrante
    Quadrante()

    if Quadrante == 1:
        print ("Esta posição pertence ao quadrate 1")
    
    elif Quadrante == 2:
        print ("Esta posição pertence ao quadrate 2")
    
    elif Quadrante == 3:
        print ("Esta posição pertence ao quadrate 3")
    
    elif Quadrante == 4:
        print ("Esta posição pertence ao quadrate 4")
    
    elif Quadrante == 5:
        print ("Esta posição está sobre um eixo")
    
    else:
        print ("Esta posição está no ponto inicial")

def main():
    Ler_Posição()
    Identificar_Posição()
    Escrever_Posição()

if __name__ == "__main__":
    main()