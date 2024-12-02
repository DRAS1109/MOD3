"""
A Cifra de Cesar
Este programa codifica ou descodifica uma mensagem com base nos alfabetos fornecidos

ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
Original = "abcdefghijklmnopqrstuvwxyz"
Codificado = "bcdefghijklmnopqrstuvwxyza"

def Menu():
    """ Função para o utilizador escolher se quer codificar ou descidificar uma mensagem """

    Mensagem = input("Introduza a mensagem que quer codificar ou descodificar: ")
    Operação = input("Deseja Codificar (C) ou descodificar (D)? ")
    if Operação.upper() == "C":
        Codificar(Mensagem.lower())
    
    elif Operação.upper() == "D":
        Descodificar(Mensagem.lower())
    
    else:
        print("Operação inválida")

def Codificar(Mensagem):
    """ Uma função que recebe uma mensagem e devolve ja codificada """
    Mensagem_Codificada = ""

    for l in Mensagem:
        for p in range(len(Original)):
            if l == Original[p]:
                Mensagem_Codificada = Mensagem_Codificada + Codificado[p]

        if l not in Original:
            Mensagem_Codificada = Mensagem_Codificada + l

    print (Mensagem_Codificada)
    return Mensagem_Codificada

def Descodificar(Mensagem):
    """ Uma função que recebe uma mensagem codificada e devolve descodificada """
    Mensagem_Descodificada = ""

    for l in Mensagem:
        for p in range(len(Codificado)):
            if l == Codificado[p]:
                Mensagem_Descodificada = Mensagem_Descodificada + Original[p]

        if l not in Codificado:
            Mensagem_Descodificada = Mensagem_Descodificada + l
    
    print(Mensagem_Descodificada)
    return Mensagem_Descodificada

def main():
    Menu()
    assert Codificar("Olá Mundo") == "pmá nvoep", "A função deveria devolver: pmá nvoep"
    assert Descodificar("pmá nvoep") == "olá mundo", "A função deveria devolver: olá mundo"
    
if __name__ == "__main__":
    main()