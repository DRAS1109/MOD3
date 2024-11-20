import random

#Gera 3 números aleatórios entre 0 e 9
numeros_secretos = (random.randint(0, 9) for _ in range(3))
tentativas_maximas = 100  # Um número alto para tentativas indefinidas

print("Bem-vindo ao Mastermind!")
print("Tente adivinhar 3 números entre 0 e 9.")
print(numeros_secretos)

# Loop para várias tentativas
for tentativas in range(1, tentativas_maximas + 1):
    palpite = input(f"Tentativa {tentativas}: Digite seu palpite (3 números separados por espaço): ")
    palpite = [int(num) for num in palpite.split()]

    if len(palpite) != 3:
        print("Por favor, insira exatamente 3 números.")
        continue

    # Inicializa contadores
    acertos_no_lugar_certo = 0
    acertos_no_lugar_errado = 0

    # Verifica acertos no lugar certo
    for i in range(3):
        if palpite[i] == numeros_secretos[i]:
            acertos_no_lugar_certo += 1

    # Verifica acertos no lugar errado
    for num in palpite:
        if num in numeros_secretos:
            acertos_no_lugar_errado += 1

    # Remove os acertos no lugar certo do total de acertos no lugar errado
    acertos_no_lugar_errado -= acertos_no_lugar_certo

    # Mostra resultados
    print(f"Acertos no lugar certo: {acertos_no_lugar_certo}")
    print(f"Acertos no lugar errado: {acertos_no_lugar_errado}")

    # Verifica se o usuário acertou todos os números
    if acertos_no_lugar_certo == 3:
        print(f"Parabéns! Você adivinhou os números em {tentativas} tentativas.")
        break
else:
    print("Você não acertou os números.")
    print(f"Os números secretos eram: {numeros_secretos}")