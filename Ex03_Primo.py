def Primo(N) -> bool:
    """ Detecta se o N é primo e DEVOLVE com True ou False """

    N_Primo = True

    for divisor in range(2, N):
        if N % divisor == 0:
            N_Primo = False
            break

    return N_Primo

"""
if Primo(10) == True:
    print("É um nº primno")

else:
    print("Não é um nº primno")
"""