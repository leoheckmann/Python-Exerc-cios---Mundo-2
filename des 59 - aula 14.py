# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitado em cada caso.

n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
sel = 0

while sel != 5:
    print('''Você deseja fazer o que com esses valores?
    ( 1 ) Somar
    ( 2 ) Multiplicar
    ( 3 ) Mostrar o maior
    ( 4 ) Adicionar novos valores
    ( 5 ) Sair do programa''')
    sel = int(input("Insira a opção desejada: "))
    if sel == 1:
        soma = n1 + n2
        print(f'Os dois números somados é: {soma:.0f}')
    elif sel == 2:
        mult = n1 * n
        print(f'Os dois números multiplicados é: {mult}')
    elif sel == 3:
        if n1 > n2:
            print(f'{n1:.0f} é maior que {n2}:.0f!')
        else:
            print(f'{n2:.0f} é maior que {n1:.0f}!')
    elif sel == 4:
        print('-=-' * 13)
        print('Insira os valores novamente!')
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
    elif sel == 5:
        print('Saindo do programa')
    else:
        print('Opção invalida')
    print("-=-" * 14)

print('Você saiu do programa')

