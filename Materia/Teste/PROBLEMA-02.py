#Dinis Rafael Albuquerque de Sousa | Nº3 | 10º T

def Menu():
    """
    Apresenta um Menu para o utilizador
    Verifica se o Preço do produto é positivo
    Opcoes, Divisa, Pais -> str
    Preco, PrecoF -> float
    """

    Opcoes = input("Consultar Taxas? (S/N): ")
    Preco = float(input("Preço do produto (Euros): "))
    if Preco <= 0:
        return
    
    Divisa = input("Divisa (R/D/L/T): ")

    if Opcoes.upper() == "S":
        Taxa()
    
    PrecoF = PrecoFinal(Preco, Divisa)

    Pais = QualPais(Divisa)

    print(f"Preço do produto: {PrecoF} {Pais}")

def QualPais(Divisa: str) -> str:
    """
    Identifica a Moeda e o respetivo Pais a partir da Divisa
    Pais -> str
    """

    if Divisa.upper() == "R":
        Pais = "Reais [Brasil]"

    elif Divisa.upper() == "D":
        Pais = "Dólares [EUA]"

    elif Divisa.upper() == "L":
        Pais = "Libras Estrelinas [UK]"

    elif Divisa.upper() == "T":
        Pais = "Liras Turcas [Turquia ]"

    return Pais

def PrecoFinal(Preco: float, Divisa: str) -> float:
    """
    Identifica o preco da Moeda e o Acrescimo dependendo do Pais
    Preco de cada moeda:
    R = Real = 4,05
    D = Dólar = 1,23
    L = Libras Estrelinas = 0,89
    T = Liras Turcas = 4,67

    Acrescimo:
    Todos os Paises fora da Europa (Basil e EUA) pagam + 10%

    Moeda, Acrescimo, PrecoF -> float
    """
    if Divisa.upper() == "R":
        Moeda = 4.05
        Acrescimo = 1.1

    elif Divisa.upper() == "D":
        Moeda = 1.23
        Acrescimo = 1.1

    elif Divisa.upper() == "L":
        Moeda = 0.89
        Acrescimo = 1

    elif Divisa.upper() == "T":
        Moeda = 4.67
        Acrescimo = 1

    PrecoF = (Preco * Moeda) * Acrescimo
    PrecoF = round(PrecoF, 2)

    return PrecoF 


def Taxa():
    """
    Apresenta no monitor o preço de cada Moeda
    """
    Taxas ="""
Taxas:
    R -> 4,05
    D -> 1,23
    L -> 0,89
    T -> 4,67

""" 
    print(Taxas)

if __name__ == "__main__":
    Menu()