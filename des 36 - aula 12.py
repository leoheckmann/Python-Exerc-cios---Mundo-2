# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.

print('\033[1;33mEmpréstimo para comprar sua casa rápido e seguro!')
print(' ')

emp = float(input('\033[1;0mQual o valor que você precisa R$ '))
par = int(input('\033[1;0mVocê quer parcelar em quantas vezes? '))
sal = float(input('\033[1;0mQual é o seu salário R$  '))

emp2 = emp / par
trin = sal * 0.30

if trin > emp2:
    print(f'\033[1;32mSeu empréstimo foi APROVADO no valor de R${emp:.2f} em {par} parcelas de R${emp2:.2f}, PARABÉNS!')
else:
    print(f'\033[1;31mSeu empréstimo no valor de R${emp:.2f} foi NEGADO devido ao valor da parcela em R${emp2:.2f} ter ficado acima dos 30% do seu salário')
    print(f'\033[1;0mSentimos muito, em até um mês você poderá fazer a simulação novamente')