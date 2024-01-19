# monta_nomes
Script para gerar nomes e sobrenomes de forma aleatória

O uso deste script é para gerar nomes completos aleatórios para testes em aplicações e serviços

Os arquivos nomes_fonte.txt e sobrenomes_fonte.txt podem ser usados como base para a criação dos nomes

usage: monta_nomes [-h] -n ARQNOMES -l ARQSOBRENOMES [-o SAIDA] [-c {0,1}] [-q QNOMES] [-s ORDEM]


Gera nomes aleatorios a partir de arquivos com nomes e sobrenomes


options:

  -h, --help            show this help message and exit
  
  -n ARQNOMES, --arqnomes ARQNOMES
  
                        Nome do Arquivo com nomes
                        
  -l ARQSOBRENOMES, --arqsobrenomes ARQSOBRENOMES
  
                        Nome do Arquivo com sobrenomes
                        
  -o SAIDA, --saida SAIDA
  
                        Nome do arquivo de saida - padrao saida.txt
                        
  -c {0,1}, --acentos {0,1}
  
                        Remover acentos do nomes - 1 (padrao) para manter e 0 - para remover
                        
  -q QNOMES, --qnomes QNOMES
  
                        Quantidade de nomes a serem gerados - padrao 100
                        
  -s ORDEM, --ordem ORDEM
                        Ordenar a saida em ordem alfabetica - 1 - para ordernar (padrao) - 0 para nao ordenar

Versao 1 - 2024
