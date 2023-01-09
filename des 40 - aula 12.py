# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida.

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('\033[1;31mInsira a sua nota e descubra se você passou de ano!')

nota1 = float(input('\033[1;0mInsira a sua nota de Matematica: '))
nota2 = float(input("\033[1;0mInsira a sua nota de Português: "))

media = (nota1 + nota2) / 2

if media <= 5.0:
    print(f'Sua média foi {media} e infelizmente você foi \033[1;31mREPROVADO')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média foi {media} e você precisará fazer \033[1;33mRECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Sua média foi {media} e você \033[1;32 mPASSOU DE ANO!')