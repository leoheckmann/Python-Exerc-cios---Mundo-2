# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('Descubra se você esta no peso ideal!')
print('-=-' * 20)
alt = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / (alt ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print(f'Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você esta acima do peso ideal')
elif 40 >= imc:
    print('Você está com obesidade morbida')