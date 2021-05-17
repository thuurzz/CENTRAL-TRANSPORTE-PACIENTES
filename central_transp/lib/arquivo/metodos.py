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


from datetime import datetime
from time import strftime


def iniciaArquivosRegistro(nomeArquivo):
    # Cria arquivos para manipulação
    arq = open(nomeArquivo, 'a')
    # Fecha arquivo
    arq.close()
    
    

def cadastraPac(nomeArquivo):
    # hora atual para registrar momento da solicitação do paciente
    horaAtual = strftime("%a, %d %b %Y %H:%M:%S +0000").split()[4]
    titulo('CADATRO DE PACIENTES', txtCor="bgpreto")
    # Abre arquivo para cadastro com data atual
    with open(nomeArquivo, '+a') as cadastro:
        # Pede nome, origem, destino, protocolo de isolamento, tipo de transporte
        nome = input('Nome do paciente: ')
        atendimento = input('Atendimento: ')
        origem = input('Leito Origem: ')
        destino = input('Destino: ').upper()
        protIsolamento = input('Procolodo Isolamento: [P-PADRÃO][G-GOTÍCULAS][C-CONTATO][A-AEROSÓIS] ').upper()
        tipoTransp = input('Tipo de transporte: [C-CADEIRA][M-MACA] ').upper()[0]
        termoNoSetor = input('Termo no SADT: [S-SIM][N-NÃO] ').upper()[0]
        # Escreve no arquivo
        cadastro.write(f'HORARIO: {horaAtual} | ORIGEM:{origem:<5}| NOME:{nome:.<25} |ATEND:{atendimento:<7}| DESTINO: {destino:<5} | ISOLAMENTO: {protIsolamento:<3} | TIPO TRANS: {tipoTransp} | TERMO SETOR: {termoNoSetor}\n')
    time.sleep(1)
    print(f'{cor["verde"]}Cadastro realizado com sucesso.{cor["reset"]}')
    linha()


def mostraCadastro(nomeArquivo, nomePainel):
    try:
        # Abre arquivo com os nomes cadastrados
        with open(nomeArquivo, 'r') as cadastro:
            txt = cadastro.read()
            titulo(nomePainel, txtCor="bgpreto")
            print(txt)
            linha()
    except:
        # Se não encontrado arquivo, exibe erro
        print(f'{cor["vermelho"]}ERRO: Arquivo inexistente ou não encontrado.{cor["reset"]}')
        


def mudaDePainel(arqOrigem, arqDestino, msg):
    titulo(msg, txtCor="bgpreto")
    # Pede o atendimento do paciente
    atendimento = input('Atendimento do paciente que será transportado: ')
    # Pede o nome do agente de transporte
    nomeTransporte = input('Nome do agente de transporte: ')
    
    # Abre arquivo de transporte solicitados.
    # Procura pelo atendimento.
    # Remove da lista de origem
    # Adiciona na lista de destino
        
    # Mensagem de confirmação de transporte
    if True:
        print(f'{cor["verde"]}Limpeza realizada com sucesso.{cor["reset"]}')
    else:
        print(f'{cor["vermelho"]}Operação cancelada.{cor["reset"]}')
