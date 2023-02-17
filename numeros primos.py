# Tabela de cores:
verde = '\033[32m'
vermelho = '\033[31m'
reset = '\033[m'

while True:
# Input para ler número e descobrir se é primo:
    num = int(input('Digite um número inteiro: \n'))
    cont = 0

    # Laço de repetição para gerar números
    for c in range(1, num + 1):
        if num % c == 0:
            cont += 1
            print(f'{verde} {c} {reset}', end=' ')
        elif num % c != 0:
            print(f'{vermelho} {c} {reset}', end=' ')

    # Condições para ser primo ou não
    if cont > 2:
        print(f'\nO número {num} não é primo, pois é divisível por {cont} números.\n\n')
    elif cont == 2:
        print(f'\nO número {num} é primo.\n\n')
