# Cores para o terminal
cor = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;37m',
    'reset': '\033[1;0;0m',
    'reverso': '\033[1;2m',
    'bgpreto': '\033[1;40m',
    'bgvermelho': '\033[1;41m',
    'bgverde': '\033[1;42m',
    'bgamarelo': '\033[1;43m',
    'bgazul': '\033[1;44m',
    'bgmagenta': '\033[1;45m',
    'bgciano': '\033[1;46m',
    'bgbranco': '\033[1;47m'}


# tamanho de caracteres ta tela
qtoCaracteres = 145

def linha(espaco=qtoCaracteres):
    print('=' * espaco)


def titulo(msg, txtCor="branco"):
    linha()
    print(f'{cor[txtCor]}{msg:^145}{cor["reset"]}')
    linha()


def leiaInt(msg):
    while True:
        try:
            nInt = int(input(msg))
        except KeyboardInterrupt:
            print(f'\033[1;31mUsuário preferiu não informar dados.\033[0;0m')
            return 0
        except:
            print(f'\033[1;31mValor digitado inválido, tente novamente.\033[0;0m')
        else:
            return nInt


def menu(list, msg):
    titulo(msg, txtCor="bgpreto")
    c = 1
    for opc in list:
        print(f'{cor["vermelho"]}{c} - {cor["reset"]}{cor["branco"]}{opc}{cor["reset"]}')
        c += 1
    linha()
    opt = leiaInt(f'{cor["verde"]}Digite a opção desejada: {cor["reset"]}')
    return opt

