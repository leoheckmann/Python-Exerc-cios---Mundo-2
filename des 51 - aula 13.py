# Desenvolva um programa que leia o primeiro termo e a razão
# de uim PA. No final, mostre os 10 primeiros termos dessa progressão;

n1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
dec = n1 + (10 - 1) * rz
for num in range (n1, dec + rz, rz):
    print(f'{num}', end=' -> ')
print('\033[1;33mFinal!')