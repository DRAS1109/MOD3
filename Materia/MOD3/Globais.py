g_resultado = 0 #Variavel Global

def Soma(X, Y):
    global g_resultado
    g_resultado = X + Y #Utiliza a variavel global

Soma (10,5)
print (g_resultado)