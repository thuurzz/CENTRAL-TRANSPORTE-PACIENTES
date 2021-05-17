#  SISTEMA PRINCIPAL
from lib.arquivo.metodos import *
from lib.interface.menus import *
import time


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


# Cria aquivos com a data atual para manipulação
dataAtual = datetime.today()
dataArquivo = str(f'{dataAtual.day}.{dataAtual.month}.{dataAtual.year}')
# data atual para criar arquivo
arqPacSol = (dataArquivo + '-LISTA-TRANSPORTE-PACIENTES-SOLICITADOS' + '.txt')
arqPacEmTransp = (dataArquivo + '-LISTA-TRANSPORTE-PACIENTES-TRANSPORTANDO' + '.txt')
arqPacTranspFinal = (dataArquivo + '-LISTA-TRANSPORTE-PACIENTES-FINALIZADOS' + '.txt')
iniciaArquivosRegistro(arqPacSol)
iniciaArquivosRegistro(arqPacEmTransp)
iniciaArquivosRegistro(arqPacTranspFinal)


# Chama menu
listMenus = ['Lista de pacientes',
             'Solicitar transporte', 
             'Buscar pacientes',
             'Finalizar transporte',
             'Sair do programa']
while True:
    # 1 - Lista de pacientes
    # 2 - Solicitar transporte
    # 3 - Buscar paciente
    # 4 - Finalizar transporte
    # 5 - Sair do sistema
    opt = menu(listMenus, 'CENTRAL DE TRANSPORTE')
    if opt == 1:
        mostraCadastro(arqPacSol, 'PAINEL - SOLICITADOS')
        mostraCadastro(arqPacEmTransp, 'PAINEL - TRANSPORTANDO')
        mostraCadastro(arqPacTranspFinal, 'PAINEL - FINALIZADOS')
    elif opt == 2:
        cadastraPac(arqPacSol)
    elif opt == 3:
        mudaDePainel(arqPacSol, arqPacEmTransp, 'BUSCAR PACIENTE')
    elif opt == 4:
        # Implantar a finalização de transporte
        mudaDePainel(arqPacEmTransp, arqPacTranspFinal, 'FINALIZAR TRANSPORTE')
    elif opt == 5:
        titulo('FIM DO PROGRAMA', txtCor="bgpreto")
        break
    else:
        print(f"{cor['vermelho']}ERRO: Digite uma opção válida!{cor['reset']}")
    time.sleep(1.3)
