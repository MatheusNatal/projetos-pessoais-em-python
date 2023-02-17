from random import randint
from time import sleep

# Tabela de cores
vermelho = '\033[31m'
magenta = '\033[35m'
amarelo = '\033[33m'
ciano = '\033[36m'
verde = '\033[32m'
reset = '\033[0;0m'

lista = ["Pedra", "Papel", "Tesoura"]
pontos_pc = 0
pontos_player = 0

while 1 > 0:
    computador = randint(0, 2)
    print(f'Pontos Jogador: {pontos_player}\n'
          f'pontos computador: {pontos_pc}')
    perguntar = int(input('''Escolha uma opção para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura

Digite sua escolha: '''))

    print("JO\n")
    sleep(0.256)
    print("KEN\n")
    sleep(0.256)
    print("POOH!!!\n")
    sleep(0.256)

    print(f'{vermelho}-=-{reset}' * 12)
    print(f'{verde}O computador escolheu: {lista[computador]}{reset}')
    print(f'{ciano}O jogador escolheu: {lista[perguntar]}{reset}')
    print(f'{vermelho}-=-{reset}' * 12)

    if computador == 0:  # Pedra
        if perguntar == 0:
            print("Empate!\n")
        elif perguntar == 1:
            print(f'{ciano}Jogador{reset} venceu!\n')  #
            pontos_player = (pontos_player + 1)
        elif perguntar == 2:
            print(f"{verde}Computador{reset} venceu!\n")  #
            pontos_pc = (pontos_pc + 1)
        else:
            print(f'{vermelho}Operação inválida.{reset}\n')  #

    elif computador == 1:  # Papel
        if perguntar == 0:
            print(f"{verde}Computador{reset} venceu!\n")  #
            pontos_pc = (pontos_pc + 1)
        elif perguntar == 1:
            print("Empate!\n")  #
        elif perguntar == 2:
            print(f'{ciano}Jogador{reset} venceu!\n')  #
            pontos_player = (pontos_player + 1)
        else:
            print(f'{vermelho}Operação inválida.{reset}\n')  #
    elif computador == 2:  # Tesoura
        if perguntar == 0:
            print(f'{ciano}Jogador{reset} venceu!\n')  #
            pontos_player = (pontos_player + 1)
        elif perguntar == 1:
            print(f"{verde}Computador{reset} venceu!\n")  #
            pontos_pc = (pontos_pc + 1)
        elif perguntar == 2:
            print("Empate!\n")
        else:
            print(f'{vermelho}Operação inválida.{reset}\n')
            