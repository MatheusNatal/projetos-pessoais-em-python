from random import randint
from time import sleep
print('Jogos Clássicos: Par ou Ímpar v2.0')

escolhadoJogador = str(input('\nPar ou ímpar?[P/I]: ')).upper()[0].strip()
print(f'Você escolheu Par' if escolhadoJogador in 'Pp' else '')
print(f'Você escolheu Ímpar' if escolhadoJogador in 'IiÍí' else '')

jogadasUsuario = -1
pontosJogador = 0
pontosPc = 0

if escolhadoJogador in 'Pp' or escolhadoJogador in 'IiÍí':
    while pontosPc != 1:
        jogadasPc = randint(0, 5)
        jogadasUsuario = int(input('\nDigite um número de 0 a 5: '))
        if jogadasUsuario < 0 or jogadasUsuario > 5:
            break
        sleep(0.2)
        print('aguarde...')
        sleep(0.2)
        if escolhadoJogador in 'Pp' and (jogadasUsuario + jogadasPc) % 2 == 0:
            pontosJogador += 1
            print(f'\nParabéns! O PC escolheu {jogadasPc} e você {jogadasUsuario}, sendo {jogadasPc + jogadasUsuario} Par.')
        elif escolhadoJogador in 'IiÍí' and (jogadasUsuario + jogadasPc) % 2 != 0:
            pontosJogador += 1
            print(f'\nParabéns! O PC escolheu {jogadasPc} e você {jogadasUsuario}, sendo {jogadasPc + jogadasUsuario} Ímpar.')
        elif (jogadasPc + jogadasUsuario) == 0:
            print('O computador jogou 0 e você também. Essa partida foi empate.')

    if jogadasUsuario < 0 or jogadasUsuario > 5:
        print('Jogada inválida! escolha um número entre 0 e 5')
    if pontosJogador > 1:
        print(f'\nO Jogador perdeu, mas teve {pontosJogador} vitórias consecutivas')
    elif pontosJogador == 1:
        print(f'\nO Jogador perdeu, mas teve {pontosJogador} vitória consecutiva')
    else:
        print('O jogador perdeu.')
