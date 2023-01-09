# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# 0 primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

print('\033[1;32mDescubra qual número é maior!')

n1 = int(input('\033[1;0mInsira o primeiro número: '))
print('-=-' * 20)
n2 = int(input('\033[1;0mInsira o segundo número: '))

if n1 > n2:
    print(f'O número {n1} é maior que o {n2}.')
elif n2 > n1:
    print(f'O número {n2} é maior que o {n1}.')
elif n1 == n2:
    print(f'Os números {n1} e {n2} são iguais!')