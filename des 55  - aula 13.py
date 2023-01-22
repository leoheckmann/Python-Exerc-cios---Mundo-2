# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for peso in range(1, 6):
    pesagem = float(input(f'Insira o peso da {peso}ª pessoa: '))
    if peso == 1:
        maior = pesagem
        menor = pesagem
    else:
        if pesagem > maior:
            maior = pesagem
        if pesagem < menor:
            menor = pesagem

print(f'O maior peso lido foi o de {maior}kg!')
print(f'O menor peso lido foi o de {menor}kg!')
