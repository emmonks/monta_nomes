#!/usr/bin/python3
# monta_nomes.py - versao 1
# Desenvolvido por Eduardo Maronas Monks - 2024
# Uso permitido, venda proibida!
# Arquivo de nomes somente com o primeiro nome, um por linha
# Arquivo de sobrenomes somente com um sobrenome, um por linha

 
import csv
import sys
import random
import re
import argparse
from datetime import datetime

# Remove acentos do username
def f_remove_accents(old):
    new = old.lower()
    new = re.sub(r'[àáâãäå]', 'a', new)
    new = re.sub(r'[èéêë]', 'e', new)
    new = re.sub(r'[ìíîï]', 'i', new)
    new = re.sub(r'[òóôõö]', 'o', new)
    new = re.sub(r'[ùúûü]', 'u', new)
    new = re.sub(r'[ç]', 'c', new)
    new = re.sub(r'[ñ]', 'n', new)
    return new


parser = argparse.ArgumentParser(prog='monta_nomes', description='Gera nomes aleatorios a partir de arquivos com nomes e sobrenomes',  epilog='Versao 1 - 2024')
parser.add_argument('-n', '--arqnomes', required=True, type=str, help='Nome do Arquivo com nomes')
parser.add_argument('-l', '--arqsobrenomes', required=True, type=str, help='Nome do Arquivo com sobrenomes')
parser.add_argument('-o', '--saida', required=False, default='saida.txt', type=str, help='Nome do arquivo de saida - padrao saida.txt')
parser.add_argument('-c', '--acentos', required=False, default=1, type=int, choices=range(0,2), help='Remover acentos do nomes - 1 (padrao) para manter e 0 - para remover')
parser.add_argument('-q', '--qnomes', required=False, default=100, type=int, help='Quantidade de nomes a serem gerados - padrao 100')
parser.add_argument('-s', '--ordem', required=False, default=1, type=int, help='Ordenar a saida em ordem alfabetica - 1 - para ordernar (padrao) - 0 para nao ordenar')
args = parser.parse_args()


arquivonomes=args.arqnomes
arquivosobrenomes=args.arqsobrenomes
arquivosaida=args.saida
acentos=int(args.acentos)
qnomes=int(args.qnomes)
ordem=int(args.ordem)


# Abre o arquivo com o nome completo dos usuarios

try:
        reader = csv.reader(open(arquivonomes, "r", encoding='utf-8'), delimiter=';')
except FileNotFoundError:
        print ("Erro na abertura do arquivo: " + arquivonomes)
        sys.exit()

try:
        reader2 = csv.reader(open(arquivosobrenomes, "r", encoding='utf-8'), delimiter=';')
except FileNotFoundError:
        print ("Erro na abertura do arquivo: " + arquivosobrenomes)
        sys.exit()


def sorteia_indice(tamanho_lista):
     return random.randrange(0, tamanho_lista)

def verifica_sobrenome(nome, lista_sobrenome, tamanho):
    if len(lista_sobrenome) >= tamanho:
        if '%s %s' %(nome,' '.join(lista_sobrenome[0:tamanho])) not in snomes:
                return "%s %s" %(nome,' '.join(lista_sobrenome[0:tamanho]))
        else:
             return False
    else:
        return False

def gera_tamanho_do_sobrenome(limite_inferior,limite_superior):
     proporcao_tamanho_sobrenome = random.randrange(0, 10) 
     if (proporcao_tamanho_sobrenome >= 0) and (proporcao_tamanho_sobrenome < limite_inferior):
          return 3
     elif (proporcao_tamanho_sobrenome >= limite_inferior) and (proporcao_tamanho_sobrenome < limite_superior):
          return 2
     else:
          return 1

# Lista auxiliares
nomes=[]
sobrenomes=[]
snomes=[]


for row in reader:
        cont = row
        nome=cont[0].split()
        nomes.append(nome[0])

for row in reader2:
        cont = row
        sobrenome=cont[0].split()
        sobrenomes.append(sobrenome[0])

conta=0

while len(snomes) < qnomes:
    indice_nome = sorteia_indice(len(nomes))
    rnome=nomes[indice_nome]
    indice_sobrenome = sorteia_indice(len(sobrenomes))
    lista_sobrenomes = [] 
    for _ in range(0,3):
         indice_sobrenome = sorteia_indice(len(sobrenomes))
         lista_sobrenomes.append(sobrenomes[indice_sobrenome])

    tamanho_do_sobrenome = gera_tamanho_do_sobrenome(3,8)
    nome_completo = verifica_sobrenome(rnome, lista_sobrenomes, tamanho_do_sobrenome)
    
    if nome_completo != False:
        snomes.append(nome_completo)    

    conta=conta+1


if ordem == 1:
    snomes.sort()

# Salva em arquivo o resultado da execucao
with open(arquivosaida, 'w+') as f:
	# write elements of list
    for items in snomes:
        nomecompleto = "".join(str(element) for element in items)
        if acentos == 1:
             nomecompleto=f_remove_accents(nomecompleto)
        f.write(nomecompleto.title() + '\n')

# Fecha o arquivo
f.close()

print("Arquivo: " + arquivosaida + " escrito com sucesso")
print ("Voltas:" + str(conta))
print ("Qte Nomes Gerados:" + str(len(snomes)))





