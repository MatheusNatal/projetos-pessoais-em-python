
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
menu = ' '
while True:
    print('=' * 40)
    print('{:^40}'.format('\033[0;49;93mAULA 16 - TUPLAS\033[m'))
    print('=' * 40)
    menu = int(input('[ 1 ] Reconhecendo tipos de estruturas'
'\n[ 2 ] Index de uma tupla'
'\n[ 3 ] Mostrar tupla em determinada ordem'
'\n[ 4 ] Usando estruturas de repetição For com tuplas'
'\n[ 5 ] Organizando tupla por ordem alfabética'
'\n[ 6 ] Soma de tuplas'
'\n[ 7 ] Múltiplos valores de tuplas'
'\n[ 8 ] Deletando tuplas'
'\n Escolha o item: '))
    if menu == 1:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Reconhecendo tipos de estruturas'))
        print('=' * 40)
        print('lanche = (tupla) [lista] {dicionario}')
        print('\n')

    elif menu == 2:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Index de uma tupla'))
        print('=' * 40)
        print("lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')")
        print('Index:          0          1       2        3')
        print('\n')

    elif menu == 3:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Mostrar tupla em determinada ordem'))
        print('=' * 40)
        print('lanche = ', lanche)
        print('\n')
        print("print(lanche[1] - Mostra o segundo item da tupla lanche")
        print(lanche[1])
        print('\n')
        print("lanche[0:3] - Mostra o primeiro, segundo e terceiro itens da tupla lanche, ignorando o ultimo item")
        print(lanche[0:3])
        print('\n')
        print("lanche[2:]) - Mostra do terceiro item em diante")
        print(lanche[2:])
        print('\n')
        print("lanche[:2]) - Mostra do primeiro item até o terceiro")
        print(lanche[:2])
        print('\n')
        print("lanche[-2]) - Inverte a ordem da listagem e mostra até o terceiro item")
        print(lanche[-2])
        print('\n')
        print("lanche[-2:]) - Inverte a ordem da listagem e mostra do terceiro item até o ultimo")
        print(lanche[-2:])
        print('\n')
        print("len(lanche)")
        print(len(lanche))
        print('\n')

    elif menu == 4:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Usando estruturas de repetição For com tuplas'))
        print('=' * 40)
        print('\n')
        print('for comida in lanche:'
              '\n    print(f"Eu vou comer {comida}")')
        for comida in lanche:
            print(f'\nEu vou comer {comida}')
        print('Comi muito!')

        print("\nfor cont in range(0, len(lanche)):"
                "\n   print(cont, end=' = ')  # Mostra o index"
                "\n   print(lanche[cont])  # Mostra o item do index respectivo")
        for cont in range(0, len(lanche)):
            print(cont, end=' = ')  # Mostra o index
            print(lanche[cont])  # Mostra o item do index respectivo

        print("\nfor pos, comida in enumerate(lanche):"
                "\n   print(f'eu vou comer {comida} na posição {pos}')")
        print('\n')
        for pos, comida in enumerate(lanche):
            print(f'eu vou comer {comida} na posição {pos}')
        print('\n')

    elif menu == 5:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Organizando tupla por ordem alfabética'))
        print('=' * 40)
        print("print(sorted(lanche))")
        print(sorted(lanche))
        print('\n')

    elif menu == 6:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Soma de tuplas'))
        print('=' * 40)
        print('''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(c))
print(len(c))
print(c.count(5))  # Mostrar quantas vezes aparece 5 dentro de C
print(c.index(2))  # Mostrar em que posição está o primeiro numero 2
print(c.index(5, 1))  # Método deslocamento. Descobrir em quais posições o 5 está''')
        print('\n')
        a = (2, 5, 4)
        b = (5, 8, 1, 2)
        c = a + b
        print(sorted(c))
        print(len(c))
        print(c.count(5))  # Mostrar quantas vezes aparece 5 dentro de C
        print(c.index(2))  # Mostrar em que posição está o primeiro numero 2
        print(c.index(5, 1))  # Método deslocamento. Descobrir em quais posições o 5 está
        print('\n')
    elif menu == 7:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Múltiplos valores de tuplas'))
        print('=' * 40)
        print("pessoa = ('Matheus', 24, 'M', 86.5)")
        pessoa = ('Matheus', 24, 'M', 86.5)
        print('\n')

    elif menu == 8:
        print('\n')
        print('=' * 40)
        print('{:^40}'.format('Múltiplos valores de tuplas'))
        print('=' * 40)
        print("pessoa = ('Matheus', 24, M, 86.5)"
              "\ndel(pessoa)")
        pessoa = ('Matheus', 24, 'M', 86.5)
        del (pessoa)
        print('\n')
    else:
        print('\n')
        print('Digite um número válido')
        print('\n')