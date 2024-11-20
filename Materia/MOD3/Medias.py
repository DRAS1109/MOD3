#4 medias diferentes, Media1, Media2, Media3 e Media4

def Media1():
    """
    A função le do utilizador os 3 nº inteiros, calcula e mostra a media
    """

    N1 = int(input("Introduza um Nº: "))
    N2 = int(input("Introduza um Nº: "))
    N3 = int(input("Introduza um Nº: "))

    Media = (N1 + N2 + N3) / 3

    print (f"A media é {int(Media)}")


def Media2(N1, N2, N3):
    """
    A função RECEBE 3 nº inteiros, calcula e mostra a media
    """

    Media = (N1 + N2 + N3) / 3

    print (f"A media de {N1}, {N2} e {N3} é: {int(Media)}")


def Media3():
    """
    A função le do utilizador os 3 nº, calcula e DEVOLVE a media
    """

    N1 = int(input("Introduza um Nº: "))
    N2 = int(input("Introduza um Nº: "))
    N3 = int(input("Introduza um Nº: "))

    Media = (N1 + N2 + N3) / 3

    return Media


def Media4(N1, N2, N3):
    """
    A função RECEBE 3 nº, calcula e DEVOLVE a media
    """

    Media = (N1 + N2 + N3) / 3

    return Media


def main():
    Media1()
    print("")

    Media2(6,7,8)
    print("")

    #Media3()
    print(f"A media é: {Media3()} \n")

    #Media4(6,7,8)
    print(f"A media é: {Media4(3,4,5)} \n")

if __name__ == '__main__':
   main()