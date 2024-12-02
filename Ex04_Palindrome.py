def Palavra_Palindrome(Palavra) -> bool:
    """Verifica se Palavra é um palindrome e devolve a variavel Palindrome com True ou False"""

    Palavra_inversa = ""
    Palavra = Palavra.lower().strip()

    for Posição in range (len(Palavra)-1,-1,-1):
        Palavra_inversa = Palavra_inversa + Palavra[Posição]

    if Palavra == Palavra_inversa:
        return True
    return False

if Palavra_Palindrome("ANA") == True:
    print("É um palindrome")

else:
    print("Não é um palindrome")