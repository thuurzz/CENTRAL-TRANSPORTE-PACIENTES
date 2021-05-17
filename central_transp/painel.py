from lib.arquivo.metodos import *
from lib.interface.menus import *
import time

# Cria aquivos com a data atual para manipulação
dataAtual = datetime.today()
dataArquivo = str(f'{dataAtual.day}.{dataAtual.month}.{dataAtual.year}')
# data atual para criar arquivo
arqPacSol = (dataArquivo + '-LISTA-TRANSPORTE-PACIENTES-SOLICITADOS' + '.txt')
arqPacEmTransp = (dataArquivo + '-LISTA-TRANSPORTE-PACIENTES-TRANSPORTANDO' + '.txt')
arqPacTranspFinal = (dataArquivo + '-LISTA-TRANSPORTE-PACIENTES-FINALIZADOS' + '.txt')

while True:
        # Limpa tela antes de exibir
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Chama painel a cada 30s
        mostraCadastro(arqPacSol, 'PAINEL - SOLICITADOS')
        mostraCadastro(arqPacEmTransp, 'PAINEL - TRANSPORTANDO')
        mostraCadastro(arqPacTranspFinal, 'PAINEL - FINALIZADOS')
        time.sleep(10)
