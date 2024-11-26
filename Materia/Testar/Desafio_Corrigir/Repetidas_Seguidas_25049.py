#Completa a função de acordo com a docstring
def RepetidasSeguidas(Palavra):
    """
    Recebe uma string com um texto que deve ser verificado para encontrar letras seguidas iguais
    Parâmetro:
        texto: string a verificar
    Devolve:
        True: se o texto contém letras seguidas iguais
        False: se o texto não tem letras seguidas iguais
    """
    Seguidas = False
    Palavra = Palavra.lower()

    for i in range (len(Palavra)-1):
            if Palavra[i] == Palavra[i + 1]:
                Seguidas = True
    
    return Seguidas

#Testes
assert RepetidasSeguidas("Ana") == False, "Erro a função devia devolver False"
assert RepetidasSeguidas("Assar") == True, "Erro a função devia devolver True"
assert RepetidasSeguidas("") == False,"Erro a função devia devolver False"
assert RepetidasSeguidas("AsSado") == True, "Erro a função devia devolver False"

print("Função passou nos testes")