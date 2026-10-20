from datetime import date

nascimento  = int(input('Ano de nascimento: '))
idade = 2026 - nascimento
ano = date.today().year
alistamento = nascimento + 18
print('Quem nasceu em {} tem {} anos em 2026'.format(nascimento,idade))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento será em {}'.format(18-idade+ano))

elif idade > 18:
    print('seu alistamento foi em {}'.format(alistamento))
elif idade == 18:
    print('Seu alistamento Será este ano!')



