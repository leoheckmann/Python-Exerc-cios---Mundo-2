# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

print('-=-' * 20)
print('Descubra a média e o menor e maior!')
print('-=-' * 20)

resp = 'S'
quant = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += soma + num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar?  ( S / N ): ')).strip().upper()[0]


media = soma / quant
print(f"Você digitou {quant} números e a média foi {media:.0f}.")
print(f'O maior valor foi {maior} e o menor foi {menor}.')