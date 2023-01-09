# Crie um programa que faça o computador jogar Jokenpô com você.
import random
div = ('Papel', 'Tesoura', 'Pedra')
pc = random.randint(0, 2)
print(f'O computador escolheu: {div[pc]}')
print("Vamos jogar Jokenpô!")
print('''ESCOLHA
( 1 ) PAPEL
( 2 ) TESOURA
( 3 ) PEDRA''')
play = int(input('Selecione: '))
print('-=-' * 11)
print(f'O computador escolheu: {div[pc]}')
print(f'O jogador escolheu: {div[play]}')
print('-=-' * 11)

if pc == 0:
    if play == 0:
        print('Empate')

    elif play == 1:
        print('Jogador vence')

    elif play == 2:
        print('Computador vence')

    else:
        print('Jogada inválida!')

elif pc == 1:
    if play == 0:
        print('Computador vence')

    elif play == 1:
        print('Empate')

    elif play == 2:
        print('Jogador vence')

    else:
        print('Jogada inválida!')

elif pc -- 2:
    if  play == 0:
        print('Jogador vence')

    elif play == 1:
        print('Computador vence')

    elif play == 2:
        print('Empate')

    else:
        print('Jogada inválida!')

