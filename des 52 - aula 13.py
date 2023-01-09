# Faça um programa que leia um número inteiro e diga se ele é
# ou não um número primo

n1 = int(input('Digite um valor inteiro: '))
to = 0
for j in range(1, n1 + 1):
    if n1 % j == 0:
        print('\033[1;33m', end=' ')
        to += 1
    else:
        print('\033[31m', end=' ')
    print(f'{j} ', end=' ')
print(f'\n\033[mO número {n1} foi divisível {to} vezes!')