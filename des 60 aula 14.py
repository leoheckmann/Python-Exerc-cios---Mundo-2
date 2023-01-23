# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5x4x3x2x1 = 120

# from math import factorial

# n1 = int(input('Digite um número: '))
# f = factorial(n1)

# print(f)


n1 = int(input('Digite um número para calular o seu Fatorial: '))
count = n1
fac = 1
print(f'Calculando {n1}! = ', end='')

while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    fac = fac * count
    count -= 1
print(f'{fac}')


