# Dinis Sousa, Nº 3, 10ºT
# Exercício de Funções em Python
# Complete cada função conforme indicado na docstring.

def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    print (valor * 2)
	
def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    Media = (n1 + n2 + n3) / 3
    return Media
	
def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	"""
    Fatorial = 0

    for i in range (1, numero + 1, -1):
        Fatorial = Fatorial * i
    
    return (Fatorial)

def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    Fahrenheit = (celsius * (9/5)) + 32

    print (Fahrenheit)

def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    Use pi = 3.14159
    """
    pi = 3.14159
    Area = pi * (raio * raio)
    print (Area)

def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""

    from time import sleep

    for N in range (inicio, -1, -1):
        print(N)
        sleep (1)

def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    Palavra 

    for i in range (len(texto), -1, -1, -1):
        Palavra = Palavra + texto[i]
    return (Palavra)

def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    if a % b == 0:
        print (f"{a} é divisivel por {b}")

def calcular_perimetro_circulo(raio):
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    pi = 3.14159
    perimetro = (2 * pi) * raio
    return (perimetro)

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    minutos = segundos // 60
    segundos = segundos % 60
    tempo = (f"{minutos}:{segundos}")
    return tempo

def gerar_saudacao_periodo():
    from datetime import datetime
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    Horas = datetime.now().hour
    if Horas <= 12:
        return ("Bom dia!")
	
    elif Horas <= 18:
        return ("Boa tarde!")
    else:
        return ("Boa noite!")

def calcular_desconto(preco, percentual: int):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    #O percentual é entre 0 e 100
    Produto = preco - (preco * (percentual / 100))
    return (Produto)

def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    Velocidade = distancia / tempo
    return (Velocidade)

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """

    palavra_inversa = ""
    palavra = palavra.lower().strip()

    for Posição in range (len(palavra)-1,-1,-1):
        palavra_inversa = palavra_inversa + palavra[Posição]

    if palavra == palavra_inversa:
        return ("É um palindrome")
    return ("Nao é um palindrome")