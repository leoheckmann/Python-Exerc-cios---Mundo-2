# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que quer mostrar
# 0 termos.



n1 = int(input('Insira o primeiro termo: '))
rz = int(input('Insira a sua razão: '))
termo = n1
count = 0
total = 0
more = 10
while more != 0:
    total += more
    while count <= total:
        print(f'{termo} -> ', end='')
        termo += rz
        count = count + 1
    more = int(input('Quantos termos você quer mostrar a mais? '))

print('Fim')