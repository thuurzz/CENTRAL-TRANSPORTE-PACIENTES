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
    
    # Pede nome, origem, destino, protocolo de isolamento, tipo de transporte
    cad = {
        'horaSolict' : str(horaAtual),
        'nome':  input('Nome do paciente: '),
        'atendimento':  input('Atendimento: '),
        'origem' : input('Leito Origem: '),
        'destino' : input('Destino: ').upper(),
        'protIsolamento' : input('Procolodo Isolamento: [P-PADRÃO][G-GOTÍCULAS][C-CONTATO][A-AEROSÓIS] ').upper(),
        'tipoTransp' : input('Tipo de transporte: [C-CADEIRA][M-MACA] ').upper()[0],
        'termoNoSetor' : input('Termo no SADT: [S-SIM][N-NÃO] ').upper()[0]}
    
    # Testa se está vazio após ter usado
    verifi=""
    with open(nomeArquivo, 'r') as verificaVazio:
        verifi = verificaVazio.read()
        
    if verifi[:2] == "\n":
        with open(nomeArquivo,'w+') as cadastro:
            # Escreve no arquivo em JSON
            cadastro.write((str(cad).replace('\'', '\"')) + '\n')
    else:     
        with open(nomeArquivo, 'a+') as cadastro:
            # Escreve no arquivo em JSON(append)
            cadastro.writelines((str(cad).replace('\'', '\"')) + '\n')
            
    time.sleep(1)
    print(f'{cor["verde"]}Cadastro realizado com sucesso.{cor["reset"]}')
    linha()

def mostraCadastro2(nomeArquivo, nomePainel):
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


def mostraCadastro(nomeArquivo, nomePainel):
    import json
    try:
        # Abre arquivo com os nomes cadastrados
        with open(nomeArquivo, 'r') as cadastro:
            txt = cadastro.read().split('\n')
            titulo(nomePainel, txtCor="bgpreto")
            for i in range(len(txt)-1):
                dicionario = json.loads(txt[i])
                print(f'HR: {dicionario["horaSolict"]} | ORIGEM: {dicionario["origem"]:<5} | NOME: {dicionario["nome"]:.<25} | ATEND: {dicionario["atendimento"]:<7} | DESTINO: {dicionario["destino"]:<5} | ISOLAMENTO: {dicionario["protIsolamento"]:<3} | TIPO TRANS: {dicionario["tipoTransp"]} | TERMO SETOR: {dicionario["termoNoSetor"]}')
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
    
    # Abre arquivo de origem.
    retorno = ""
    with open(arqOrigem, 'r') as origem:
        text = origem.read().split('\n')
        
    # Procura pelo atendimento
    for linha in text:
        if atendimento in linha:
            #Remove da lista de origem.
            index = text.index(linha)
            retorno = text.pop(index)
            with open(arqDestino, 'a') as destino:
                destino.writelines(retorno + '\n')
            acumuladora=""
            for linhas in text:
                acumuladora+=linhas+"\n"
            acumuladora = acumuladora[:-2:]   
            with open(arqOrigem, 'w+') as novoOrigem:
                novoOrigem.write(acumuladora+'\n')
            print(f'{cor["verde"]}Operação realizada com sucesso.{cor["reset"]}')
    # Registra nome e horário da transação.
    # Adiciona na lista de destino.
    # Mensagem de confirmação de transporte
        else:
            print(f'{cor["vermelho"]}Operação cancelada.{cor["reset"]}')