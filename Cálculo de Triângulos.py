print('-=-' * 20)
print('Cálculo de triangulo.')
print('-=-' * 20)

print('''Dicas:
Se A = B = C, então é Equilátero.
Se A = B != C, então é Isósceles.
Se A != B != C, então é Escaleno\n''')

a = float(input('Primeiro segmento: '))  #Variáveis para receber numero.1
b = float(input('Segundo segmento: '))  #Variáveis para receber numero.1
c = float(input('Terceiro segmento: '))  #Variáveis para receber numero.1

triangle = ['Equilátero', 'Isósceles', 'Escaleno'] #Lista com nomes dos triângulos.

# Teoria matemática para formação de um triângulo:
if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b) == True:
    print('forma um triângulo')
else:
    print('Não forma um triângulo')

if a == b == c:
    print(triangle[0])  # fórmula para identificação e output de triângulo Equilátero.

elif a == b != c  or a != b == c:
    print(triangle[1])  # fórmula para identificação e output de triângulo Isósceles.

elif a != b != c:
    print(triangle[2])  # fórmula para identificação e output de triângulo Escaleno.
