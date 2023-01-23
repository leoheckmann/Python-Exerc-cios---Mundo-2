# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 1 > 2 > 3 > 4 > 5 > 8

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1

print('-=-' * 20)
print(f'{t1} - {t2}', end='')

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3

    cont = cont + 1
print('\033[1;33m Fim!')