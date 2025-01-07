#Programa para validar uma expressão matemática quanto aos ()

def main():
    """Função para receber uma expressão"""
    Equação = input("Introduza uma equação: ")
    Resposta = Verificação(Equação)
    
    if Resposta == True:
        print ("A Equação está correta")
    
    elif Resposta == False:
        print ("A Equação está erada")

def Verificação(Equação):
    """Função para validar a expressão"""
    Parenteses = 0
    for i in Equação:
        if i == "(":
            Parenteses = Parenteses + 1
        if i == ")":
            Parenteses = Parenteses + -1
            
        if Parenteses == -1:
            return False

    return True
        
    
if __name__ == "__main__":
    main()