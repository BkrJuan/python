from random import randint
from time import sleep
from rich import print
from rich.panel import Panel
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
caixa = Panel("[bold white ]BEM VINDO![/]", title="JokenPo do Baker", style="bold blue", width=35)
print(caixa)


print('''Suas opções são :
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')

Você = int(input('Qual é a sua jogada? :  '))

print("[bold blue]JO[/]", end="", flush=True)
sleep(1)

print(" [bold red]KEN[/]", end="", flush=True)
sleep(1)

print(" [bold yellow]PO!!![/]", flush=True)
sleep(1)


print ( '~~'* 12)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[Você]))
print('~~'* 12)
if computador == 0: # computador jogou pedra
    if Você == 0:
        print('EMPATE!')
    elif Você == 1:
        print('[bold green]Voce venceu!![/]')
    elif Voce == 2:
        print('[bold red]Voce Perdeu!![/]')
    else:
        print('Jogada invalida!')

if computador == 1: # computador jogou Papel
    if Você == 1:
        print('EMPATE!')
    elif Você == 0:
        print('[bold green]Voce venceu!![/]')
    elif Voce == 2:
        print('[bold red]Voce Perdeu!![/]')
    else:
        print('Jogada invalida!')
if computador == 2: # computador jogou tesoura
    if Você == 2:
        print('EMPATE!')
    elif Você == 0:
        print('[bold green]Voce venceu!![/]')
    elif Você == 1:
        print('[bold red]Voce Perdeu!![/]')
    else:
        print('Jogada invalida!')



