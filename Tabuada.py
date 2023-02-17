i = 1
num = int(input('Digite um número inteiro para a tabuada: '))

if num > 100:
    print('Este é um número muito grande')

elif num <= 100:
    for i in range(11):
        if i > 0:
            print(f'{num} x {i} =', num * i)