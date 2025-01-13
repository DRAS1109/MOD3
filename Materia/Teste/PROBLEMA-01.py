#Dinis Rafael Albuquerque de Sousa | Nº3 | 10º T
def main():
    """
    N = Numero inserido pelo utilizador
    Apresenta no monitor se N é Perfeito
    N -> int
    """
    n = int(input("N = "))

    if n > 0:
        EPerfeito = Perfeito(n)

        if EPerfeito == True:
            print("Número perfeito")
        
        else: 
            print("Número não perfeito")


def Perfeito(n: int) -> bool:
    """
    Verifica se N (numero inserido pelo utilizador) é Perfeito 
    E conseguentemente os seus numeros primos excluindo ele proprio
    Primos -> int
    """
    Primos = 0

    #Primos de N
    for i in range (1, n):
        if n % i == 0:
            Primos = Primos + i

    #Perfeito
    if Primos == n:
        return True
    return False


if __name__ == "__main__":
    main()