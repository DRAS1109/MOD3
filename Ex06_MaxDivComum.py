def MaximoDivisorComum(N1, N2):
    """DEVOLVE o maximo divisor comum de N1 e N2"""

    if N2 > N1:
        Menor = N1
    elif N1 > N2:
        Menor = N2
    else:
        Menor = N2

    for i in range (1, Menor):
        if Menor % i == 0:
            Divisor = i
    
    return Divisor

assert MaximoDivisorComum(6, 12) == 3, "A função deveria devolver 3"
assert MaximoDivisorComum(12, 6) == 3, "A função deveria devolver 3"
print("A função passou em todos os testes")