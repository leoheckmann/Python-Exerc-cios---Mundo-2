# Elabore um programa que calcule o valor a ser pago por um produto,
# consedirando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

print('\033[1;0m-=-' * 10)
print('\033[1;33m           CAIXA     ')
print('\033[1;0m-=-' * 10)

ori = float(input('Valor do produto R$: '))
print('\033[1;0m-=-' * 10)
form = str(input('Qual a forma de pagamento? '))


a_vistadin = ori * 0.90
a_vistacard = ori * 0.95
card_2x = ori / 2
card_parc = ori * 1.20

if form == ('a vista em dinheiro'):
    print(f'Você pagará R${a_vistadin:.2f}!')
elif form == ('a vista no cartão'):
    print(f'Você pagará R${a_vistacard:.2f}!')
elif form == ('2x no cartão'):
    print(f'Você pagará 2 parcelado sem juros de R${card_2x:.2f}, valor total R${ori:.2f}')

if form == ('parcelado no cartão'):
    qts = int(input('Em quantas parcelas: '))
    parc = (ori / qts) * 1.20
    valor_total = parc * qts
    print(f'Você pagara {qts} parcelas de R${parc:.2f} com juros, total de R${valor_total:.2f}.')


