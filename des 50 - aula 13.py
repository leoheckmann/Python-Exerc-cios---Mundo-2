# Desenvola um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for
# ímpar, desconsidere-o.


som = 0
con = 0
for cont in range(1, 7):
    n1 = int(input(f'Digite o {cont} primeiro número: '))
    if n1 % 2 == 0:
        som = som + n1
        con = con + 1
print(f'Essa foi a quantidade de números pares {con} e soma foi de >>> \033[1;33m{som}!')
