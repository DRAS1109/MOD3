# Match
dia = (int(input("Insira um número inteiro de 1 a 7: ")))
match dia:
    case 1:
        print ("É segunda-feira")
    case 2:
        print ("É terça-feira")
    case 3:
        print ("É quarta-feira")
    case 4:
        print ("É quinta-feira")
    case 5:
        print ("É sexta-feira")
    case 6:
        print ("É sábado")
    case 7:
        print ("É domingo")
    case _:
        print ("O valor indicado não é valido")