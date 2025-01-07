"""Completa as seguintes funções"""

def E_Impar(numero:int) -> bool:
    """Devolve true se o numero é impar e false se par"""
    if numero % 2 != 0:
        return True
    
    return False

print("Testes E_Impar")
assert E_Impar(10) == False, "Erro no primeiro teste. Devia dar False"
assert E_Impar(11) == True, "Erro no segundo teste. Devia dar True"
print("Completou testes E_Impar")

############################################################################
def Ola_User(nome:str):
    """Diz olá ao user. Se nome não estiver preenchido não diz nada"""
    if nome != "":
        print ("Olá", nome)

print("Testes Ola_User")
Ola_User("")        #Com este argumento não deve mostrar nada
Ola_User("Joaquim") #Com este argumento deve mostrar Olá Joaquim
print("Completou testes Ola_User")

#############################################################################
def JuntaDoisNomes(nome1:str,nome2:str) -> str:
    """Devolve os nomes numa string separados por um espaço em branco. O primeiro nome deve ser o que alfabeticamente for menor."""

    if nome1.lower() <= nome2.lower():
        Resultado = (nome1 + " " + nome2)
    
    else:
        Resultado = (nome2 + " " + nome1)

    return Resultado

print("Testes JuntaDoisNomes")
assert JuntaDoisNomes("Joaquim","Ana") == "Ana Joaquim", "Erro no quinto teste, devia dar Ana Joaquim"
assert JuntaDoisNomes("Maria","Zé") == "Maria Zé","Erro no sexto teste, devia dar Maria Zé"
print("Completou testes JuntaDoisNomes")

#############################################################################
maior = ""

def QualOMaior(nome1:str, nome2: str):
    """Função para alterar a variável global maior guardando o nome com mais letras. Caso sejam de igual tamanho deve guardar a palavra Iguais"""
    Letras1 = len(nome1)
    Letras2 = len(nome2)
    global maior

    if Letras1 > Letras2:
        maior = nome1
    
    elif Letras2 > Letras1:
        maior = nome2
    else:
        maior = "Iguais"
    
    return maior


print("Testes QualOMaior")
QualOMaior("Ana","Maria")
assert maior == "Maria", "Erro no sétimo teste, maior devia ser Maria"
QualOMaior("João","José")
assert maior == "Iguais", "Erro no oitavo teste, maior devia ser Iguais"
QualOMaior("António","Zé")
assert maior == "António", "Erro no nono teste, maior devia ser António"
print("Completou testes QualOMaior")

##################################################################################
Baralho = "23456QJK7A"

def CartaMaisForte(carta1:str, carta2:str) -> str:
    """Função que recebe duas cartas de um baralho e devolve a mais forte ou None caso sejam iguais"""
    global Baralho

    for i in range (len(Baralho)):
        CartaBaralho = Baralho[i]
        if CartaBaralho == carta1:
            NCarta1 = i
        if CartaBaralho == carta2:
            NCarta2 = i

    if NCarta1 > NCarta2:
        return carta1
    elif NCarta2 > NCarta1:
        return carta2
    else:
        return None
    
print("Testes CartaMaisForte")
assert CartaMaisForte("2","3") == "3", "Erro no décimo teste, devia devolver 3"
assert CartaMaisForte("A","A") == None, "Erro no décimo primeiro teste, devia devolver None"
assert CartaMaisForte("K","7") == "7", "Erro no décimo segundo teste, devia devolver 7"
print("Completou testes CartaMaisForte")