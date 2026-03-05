import random
numero_aleatorio = random.randint(0,100)
acerto = False
while not acerto:
    ...
    escolha_usuario = int(input("Escolha um numero: "))
    if escolha_usuario == numero_aleatorio:
        print('Acertou')
        acerto = True
    else:
        if escolha_usuario < numero_aleatorio:
            print('Errou! o seu numero e menor')
        elif escolha_usuario > numero_aleatorio:
            print('Errou! o seu numero e maior')