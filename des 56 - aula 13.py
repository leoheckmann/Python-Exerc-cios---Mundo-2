# Desenvola um programa que leia o nome, idade e sexo de 4
# pessoas. No final o programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.


for cent in range(1, 5):
    print(f'-=-=-=-=-=-= {cent} -=-=-=-=-=-=')
    nome = str(input('Insira o nome: ')).upper()
    sexo = str(input('Seu sexo: ')).upper()
    idade = int(input('Insira a idade: '))
    soma_idade += idade
    if cent == 1 and sexo in 'Mm':
        man_older = idade
        name_older = nome
    if sexo in 'Mm' and idade > man_older:
        man_older = idade
        name_older = nome
    if sexo in 'Ff' and idade < 20:
        woman20 += 1


idade_media = soma_idade / 4


print(f'A média da idade do grupo é de {idade_media} anos!')
print(f'A idade do homem mais velho é de {man_older} anos e o nome dele é {name_older}')
print(f'Ao todo são {woman20} mulheres que tem menos de 20 anos')

