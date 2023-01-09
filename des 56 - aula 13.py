# Desenvola um programa que leia o nome, idade e sexo de 4
# pessoas. No final o programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.


idade_media = 0

for peso in range(1, 5):
    nome = str(input('Insira o nome: '))
    idade = int(input('Insira a idade: '))
    peso = float(input(f'Insira o peso: '))
    idade_media = idade_media + idade / 4
print(idade_media)
