# Refaça o desafio 35 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado.

# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

print("Insira três números de um reta para ver forma um triângulo!")

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("As retas acima podem formar um triângulo! ", end='')
    if n1 == n2 == n3:
        print('Equilatero')
    if n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print("As retas acima não formam um triângulo!")
