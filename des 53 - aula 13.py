# Crie um programa que leia uma frase qualquer e diga se ela
# é políndromo, desconsiderando os espaços

# exÇ
# APOS A SOPA
# a sacada da casa
# a torre da derrota
# O lobo ama o bolo
# anotaram a data da maratona


frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Essa frase é palíndromo')
else:
    print('Essa frase não é palíndromo')
