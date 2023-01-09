# Faça um programa que calcule a soma entre os números ímpares que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
con = 0
for mult3 in range(1, 500, 2):
    if mult3 % 3 == 0:
        con = con + 1
        soma = soma + mult3
print(f'A soma de todos os {con} valores é de: \033[1;33m{soma}\033[1;0m!')
