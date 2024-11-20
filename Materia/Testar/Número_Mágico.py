'''
PSI - Módulo 2
Estruturas de repetição
Ciclo While - Jogo do número mágico
'''
 
# Importar módulo Random
import random
import winsound
 
# Gerar um número aleatório
numero_magico=random.randint(1,100)
 
# inicializar a variavel
palpite=0
tentativas=0
 
# Repetir ENQUANTO não acertar
while(numero_magico!=palpite and tentativas<10):
 
    # --- Input ---
    # Ler o palpite do utilizador
    palpite=int(input("Qual o número do seu palpite:"))
    tentativas+=1
 
    # Testar se o número mágico é igual ao palpite do utilizador
    if(palpite==numero_magico):
        print(f"Parabéns.\nAcertaste em {tentativas} tentativas")
        if(tentativas==9):
            winsound.Beep(200,1000)
    else:
        print(f'O número não é esse.\nRestam {10-tentativas} tentativas')
        if(palpite<numero_magico):
            print(f'O número mágico á maior do que {palpite}\n')
        else:
            print(f'o número mágico é menor do que {palpite}\n')