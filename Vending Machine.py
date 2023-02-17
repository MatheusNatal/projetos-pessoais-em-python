print('-=-' * 20)
print('Vending Machine.')
print('-=-' * 20)

# Tabela de cores
vermelho = '\033[31m'
magenta = '\033[35m'
amarelo = '\033[33m'
ciano = '\033[36m'
verde = '\033[32m'
reset = '\033[0;0m'

# Lista de objetos a serem vendidos
products_list = ['celular', 'notebook', 'tablet']
print(f'{"1"} - {products_list[0]}'
      f'\n{"2"} - {products_list[1]}'
      f'\n{"3"} - {products_list[2]}')

# Lista de preços
price_list = [1200, 3000, 800]

choice = int(input('Informe o número do item que você quer: '))

if choice == 1:
    print(f'O valor a ser pago é R${price_list[0]}\n')
    print(f'5 - À vista(Dinheiro/Cheque) com {amarelo}10% de desconto{reset}'
          f'\n6 - À vista no cartão com {amarelo}5% de desconto{reset}'
          '\n7 - Até 2x no cartão'
          f'\n8 - Em até 12x no cartão {vermelho} 20% de juros{reset}')
    formas_pagamento = input('Digite o número da forma de pagamento: ')

    if formas_pagamento == '5':
        print(f'Total:{price_list[0]}, \ncom desconto de 10%, ficou: R${price_list[0] - (price_list[0] * 0.1)}')
    elif formas_pagamento == '6':
        print(f'Total:{price_list[0]}, \ncom desconto de 5%, ficou: R${price_list[0] - (price_list[0] * 0.05)}')
    elif formas_pagamento == '7':
        print(f'Total: 2x R${price_list[0]/2}')
    elif formas_pagamento == '8':
        vezes_pagamento = int(input('Em quantas vezes? (2 até 12): '))
        print(f'Total: {vezes_pagamento}x de {(price_list[0] / vezes_pagamento) + (price_list[0] * 0.2)}')

elif choice == 2:
    print(f'O valor a ser pago é R${price_list[1]}\n')
    print(f'5 - À vista(Dinheiro/Cheque) com {amarelo}10% de desconto{reset}'
          f'\n6 - À vista no cartão com {amarelo}5% de desconto{reset}'
          '\n7 - Até 2x no cartão'
          f'\n8 - Em até 12x no cartão {vermelho} 20% de juros{reset}')
    formas_pagamento = input('Digite o número da forma de pagamento: ')

    if formas_pagamento == '5':
        print(f'Total:{price_list[1]}, \ncom desconto de 10%, ficou: R${price_list[1] - (price_list[1] * 0.1)}')
    elif formas_pagamento == '6':
        print(f'Total:{price_list[1]}, \ncom desconto de 5%, ficou: R${price_list[1] - (price_list[1] * 0.05)}')
    elif formas_pagamento == '7':
        print(f'Total: 2x R${price_list[1]/2}')
    elif formas_pagamento == '8':
        vezes_pagamento = int(input('Em quantas vezes? (2 até 12): '))
        print(f'Total: {vezes_pagamento}x de {(price_list[1] / vezes_pagamento) + (price_list[1] * 0.2)}')

elif choice == 3:
    print(f'O valor a ser pago é R${price_list[2]}\n')
    print(f'5 - À vista(Dinheiro/Cheque) com {amarelo}10% de desconto{reset}'
          f'\n6 - À vista no cartão com {amarelo}5% de desconto{reset}'
          '\n7 - Até 2x no cartão'
          f'\n8 - Em até 12x no cartão {vermelho} 20% de juros{reset}')

    formas_pagamento = input('Digite o número da forma de pagamento: ')

    if formas_pagamento == '5':
        print(f'Total:{price_list[2]}, \ncom desconto de 10%, ficou: R${price_list[2] - (price_list[2] * 0.1)}')
    elif formas_pagamento == '6':
        print(f'Total:{price_list[2]}, \ncom desconto de 5%, ficou: R${price_list[2] - (price_list[2] * 0.05)}')
    elif formas_pagamento == '7':
        print(f'Total: 2x R${price_list[2]/2}')
    elif formas_pagamento == '8':
        vezes_pagamento = int(input('Em quantas vezes? (2 até 12): '))
        print(f'Total: {vezes_pagamento}x de {(price_list[2] / vezes_pagamento) + (price_list[2] * 0.2)}')

else:
    print('Error 404')
