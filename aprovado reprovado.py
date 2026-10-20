n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
media = (n1 + n2) / 2

print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))

if media >=5 and media <=7:
    print('O aluno está em recuperação !')

elif media <5:
    print('O aluno foi reprovado !')
elif media >=7 and media <=10:
    print('o aluno foi aprovado !')
elif media >10:
    print('Valor de Média acima de 10. Revise as notas digitadas.')






