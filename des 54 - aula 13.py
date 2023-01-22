# Crie um programa que leia o ano de nascimento de sete
# pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e qunatas já são maiores.

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    ano = int(input(f'Insira o ano de nascimento da {pessoas}ª pessoa: '))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'\033[1;33mAo todo temos o total de {totalmaior} pessoas maior de idade e {totalmenor} menor de idade.')
