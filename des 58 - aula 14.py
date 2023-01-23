# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
pc = randint(0, 10)
cont = 0
win = False

print('Vamos brincar, estou pensando em um número entre 1 e 10, consegue adivinhar?')

while not win:
    cont += 1
    player = int(input('Digite sua adivinhação: '))
    if player == pc:
        win = True
    else:
        if player < pc:
            print('Está quase lá, é MAIS.')
        elif player > pc:
            print('Está quase lá, é MENOS')
print(f'\033[1;35mVOCÊ GANHOU!, o computador e você escolheu o número {player} e houve {cont} tentativas')