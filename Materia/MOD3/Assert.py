def MaiorDeDois(N1, N2):

    "Se N1 e N2 forem iguais, DEVOLVE None, se não, DEVOLVE o maior"

    if N1 > N2:
        return N1
    elif N2 < N1: #O < everia ser >
        return N2
    return None

assert MaiorDeDois(10, 5) == 10, "A função deveria devolver 10"
assert MaiorDeDois(5, 10) == 10, "A função deveria devolver 10"
assert MaiorDeDois(10, 10) == None, "A função deveria devolver None pq os nº sao iguais"
print("A função passou em todos os testes")