# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles.
# (Desconsiderando o FLAG)


n1 = count = soma = 0
n1 = int(input('Digite seu número inteiro: '))
while n1 != 999:
    soma += n1
    count += 1
    n1 = int(input('Digite seu número inteiro: '))

print(f'Você digitou {count} números e a soma entre eles foi {soma}')
