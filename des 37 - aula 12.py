# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão:

# 1 para binário
# 2 para actal
# 3 para hexadecimal

n1 = int(input('Digite um número inteiro: '))
print('''Selecione uma base para realizar a conversão
( 1 ) conversão para Binário
( 2 ) conversão para Octal
( 3 ) conversão para Hexadecial''')
op = int(input('Sua opção: '))

if op == 1:
    print(f'{n1} convertido para Binário é igual a {bin(n1)[2:]}')
elif op == 2:
    print(f'{n1} convertido para Octal é igual a {oct(n1)[2:]}')
elif op == 3:
    print(f'{n1} convertido para Hexadecimal é igual a {hex(n1)[2:]}')
else:
    print('Formado invalido!')