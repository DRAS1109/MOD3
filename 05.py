def MaiorDeDois(N1, N2):

    "Se N1 e N2 forem iguais, DEVOLVE None, se não, DEVOLVE o maior"

    if N1 > N2:
        return N1
    elif N2 > N1:
        return N2
    return None

print(MaiorDeDois(1, 2))