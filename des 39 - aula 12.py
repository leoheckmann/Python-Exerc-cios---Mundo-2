# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

print('\033[1;33mDescubra se você precisará se alistar no exercito brasileiro!')
print('-=-' * 20)

nasc = int(input("\033[1;0mInsira seu ano de nascimento: "))
print('-=-' * 20)

y = 2022 - nasc

if y < 18:
    print('\033[1;34mVocê ainda não precisará se alistar no exercíto, pois a idade necessária é 18 anos!')

elif y == 18:
    print('\033[1;32mVocê tem 18 anos e precisará se alistar no exercíto imediatamente!')

elif y > 18:
    print('\033[1;31mJà passou o tempo de você se alistar no exercíto brasileiro. Se apresente imediatamente em uma '
          'junta militar!')




