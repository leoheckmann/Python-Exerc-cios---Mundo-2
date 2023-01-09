# A confederção nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER



print('\033[1;31mDescubra sua categoria!')


ano = int(input('\033[4;0mInforme seu ano de nascimento: '))
dat = 2022 - ano

if dat <= 9:
    print(f'Sua idade é {dat} e você é \033[1;33mMIRIM!')
elif dat > 9 and dat <= 14:
    print(f'Sua idade é {dat} e você é \033[1;33mINFANTIL!')
elif dat > 14 and dat <= 19:
    print(f'Sua idade é {dat} e você é \033[1;33mJUNIOR')
elif dat == 20:
    print(f'Sua idade é {dat} e você é \033[1;33mSÊNIOR')
elif dat > 20:
    print(f'Sua idade é {dat} e você é \033[1;33mMASTER')