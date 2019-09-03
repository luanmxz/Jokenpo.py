# Author: LM
import random
import os


def jokenpo():
    ppt = [1, 2, 3]
    playerBOT = random.choice(ppt)
    print('\033[1;31m-\033[0;30m' * 33, 'JOKENPÔ', '\033[1;31m-\033[0;30m' * 33, '\n')
    print(' ' * 33, '\033[1;35mREGRAS:\033[1;35m')
    print(
        '\n0 - Os comandos aceitos pelo sistema são: 1 - Pedra; 2- Papel, 3 - Tesoura.\n1 - Você vai jogar contra um BOT.\n2 - Pedra ganha de Tesoura e perde para Papel!\n3 - Papel ganha de Pedra e perde para Tesoura!\n4 - Tesoura ganha de Papel e perde para Pedra!\n\n')
    print('\033[1;31m-\033[0;30m' * 75)
    playerUSER = int(input(
        '\033[1;36mEscolha entre pedra, papel e tesoura:\n 1 para Pedra.\n 2 para Papel.\n 3 para Tesoura.\n\033[0;30m '))
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\n')
    if playerUSER < 1 or playerUSER > 3:
        print('\033[1;31mValor inválido!\033[0;30m')
    elif playerUSER == 1 and playerBOT == 1:
        print(' ' * 15, '\033[1;33mEMPATE!\n Os dois jogadores escolheram {} - Pedra!\033[0;30m'.format(playerUSER))
    elif playerUSER == 2 and playerBOT == 2:
        print(' ' * 15, '\033[1;33mEMPATE!\n Os dois jogadores escolheram {} - Papel!\033[0;30m'.format(playerUSER))
    elif playerUSER == 3 and playerBOT == 3:
        print(' ' * 15, '\033[1;33mEMPATE!\n Os dois jogadores escolheram {} - Tesoura!\033[0;30m'.format(playerUSER))
    elif playerUSER == 1 and playerBOT == 2:
        print('Você - Pedra  x  Papel - Bot')
        print('\033[1;31mVocê perdeu! Tente novamente!\033[0;30m')
    elif playerUSER == 1 and playerBOT == 3:
        print('Você - Pedra  x  Tesoura - Bot')
        print('\033[1;32mVocê ganhou! Parabéns!\033[0;30m')
    elif playerUSER == 2 and playerBOT == 1:
        print('Você - Papel  x   Pedra - Bot')
        print('\033[1;32mVocê ganhou! Parabéns!\033[0;30m')
    elif playerUSER == 2 and playerBOT == 3:
        print('Você - Papel  x  Tesoura - Bot')
        print('\033[1;31mVocê perdeu! Tente novamente!\033[0;30m')
    elif playerUSER == 3 and playerBOT == 1:
        print('Você - Tesoura  x  Pedra - Bot')
        print('\033[1;31mVocê perdeu! Tente novamente!\033[0;30m')
    elif playerUSER == 3 and playerBOT == 2:
        print('Você - Tesoura  x  Papel - Bot')
        print('\033[1;32mVocê ganhou! Parabéns!\033[0;30m')
    print('\n')
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    print('\033[1;31m-\033[0;30m' * 75)
    chose = int(input('Deseja jogar novamente?\n(1) - Sim\n(2) - Não\n '))
    if chose == 1:
        jokenpo()
    else:
        exit(0)


jokenpo()
