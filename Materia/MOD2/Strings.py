# Strings
nome = "          ola mundo"
marca = 'ford'
varias_linhas = """
com varias linhas 
"""

#tamanho da string
print(len(nome))

#converter para maiusculas
print(marca.upper)
print(marca)
marca = marca.upper()
print(marca)

#converter para minusculas
print(marca.lower)
print(marca)

#colocar a primeira letra em maiuscula
marca = marca.capitalize()
print(marca)

#remove os espaços em branco no inicio e no final
print(nome.strip())