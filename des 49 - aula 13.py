#Refaça o des 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

n = int(input('Insira um número e descubra a tabuada dele: '))
for mult in range(1, 11):
    print(f'\033[1;35m{n} x {mult} = ', n * mult)