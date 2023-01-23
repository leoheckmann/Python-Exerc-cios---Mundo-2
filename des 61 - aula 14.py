# Refaça o desafio 51, lendo o primeiro PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.

n1 = int(input('Insira o primeiro termo: '))
rz = int(input('Insira a sua razão: '))
termo = n1
count = 0

while count <= 10:
    print(f'{termo} -> ', end='')
    termo += rz
    count = count + 1
print('Finished')

