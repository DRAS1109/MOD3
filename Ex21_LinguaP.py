#Função para traduzir uma frase na lingua dos P

def LinguaP(Frase: str) -> str:
    """Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
    Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
    """

    Resultado = ""
    Ultimo = ""

    for i in range (1, len(Frase)):
        Letra = Frase[i - 1]
        Resultado = Resultado + Letra

        if Letra in "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙ":
            if Frase[i] not in "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙ":
                
                Resultado = Resultado + "p"
                Resultado = Resultado + Ultimo + Letra.lower()
            
            else:
                Ultimo = Letra

    Resultado = Resultado + Frase[i] + "p" + Frase[i]

    return Resultado

print (LinguaP("Casa"))