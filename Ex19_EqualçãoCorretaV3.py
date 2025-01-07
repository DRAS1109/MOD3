#Programa para validar uma expressão matemática quanto aos () e []

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
    Parenteses = ""
    for i in Equação:
        if i == "(" or i == "[":
            Parenteses = Parenteses + i

        if i == ")" or i == "]":
            if Parenteses == "":
                return False
            
            Ultimo = Parenteses[len(Parenteses) - 1]
            if (Ultimo == "(" and i == ")") or (Ultimo == "[" and i == "]"):
                ParentesesT = Parenteses
                Parenteses = ""
                for i in range (len(ParentesesT) - 1):
                    Parenteses = Parenteses + ParentesesT[i]
            else:
                return False
    if Parenteses == "":
        return True
    return False
        
    
if __name__ == "__main__":
    main()