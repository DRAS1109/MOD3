#Completa a função de acordo com a docstring
def ContaVogais(Palavra):
    """
    Recebe uma string e conta o nº de vogais
    Parâmetro:
        texto - string para contar as vogais
    Devolve:
        nº de vogais
    """

    Palavra = Palavra.lower()
    Vogais = 0
    Todas_Vogais = "aeiou"

    for i  in range (len(Palavra)):
        if Palavra[i] in Todas_Vogais:
            Vogais = Vogais + 1
    
    return Vogais


#Testes
assert ContaVogais("Ana") == 2, "Erro a função devia devolver 2"
assert ContaVogais("ZZZ") == 0, "Erro a função devia devolver 0"

print("Função passou nos testes")