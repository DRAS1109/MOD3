def FizzBuzz(upTo):
    Escreve = ""
    for i in range (1, upTo + 1):
        if i % 3 == 0:
                Escreve = Escreve  + "Fizz"

        if i % 5 == 0:
                Escreve = Escreve  + "Buzz " 

        else:
            Escreve = Escreve  + (" " + str(i) + " ")
    
    print (Escreve)

FizzBuzz(35)