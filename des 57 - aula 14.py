# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# "M" ou "F".

# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Insira o sexo [M/F]: ')).upper().strip()[0]
while sexo not in "M,F":
    print('Resposta não reconhecida, digite novamente')
    sexo = str(input('Insira o sexo [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso.')

