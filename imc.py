from rich import print
peso = float(input('Qual o seu peso?: (KG)'))
altura = float(input('Digite sua altura. EX: 1.80: (m)'))
imc = peso / (altura ** 2)

print('O IMC desta pessoa é de {:.1F}'.format(imc))

if imc < 18.5:
    print('[bold red]Magrelo Desgraçado, seu IMC está ABAIXO DO PESO. VÁ COMER AGORA!![/]')
elif imc >= 18.5 and imc <= 25:
    print('[bold green]PARABÉNS! Voce está no peso ideal![/]')
elif imc >= 25 and imc <= 30:
    print('[bold orange]TA COMEÇANDO A DAR MERDA, Seu IMC está em SOBREPESO![/]')
elif imc >= 30 and imc <= 40:
    print('[bold purple]BALOFO, VAI SE TRATAR, IMC DE OBESO JÁ![/]')
elif imc >= 40:
    print('[bold red]PODE ENCOMENDAR O CAIXÃO, SE COUBER ! IMC DE OBESIDADE MORBIDADA!![/]')

