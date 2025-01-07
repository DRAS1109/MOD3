#Programa para validar uma expressão matemática quanto aos ()

def main():
    """Função para receber uma expressão"""
    Equação = input("Introduza uma equação: ")
    Verificação(Equação)

def Verificação(Equação):
    """Função para validar a expressão"""
    Parenteses = 0

    for i in Equação:
        if i == "(" or i == ")":
            Parenteses = Parenteses + 1

    if Parenteses % 2 == 0:
        print ("A Equação está correta")

    else:
        print ("A Equação está errada")
    
if __name__ == "__main__":
    main()