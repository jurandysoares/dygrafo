#!/usr/bin/env python3
'''
  Cria grafo de citações (@nome.sobrenome) a partir de um 
  diretório com arquivos de texto escritos no formato Markdown.
'''
import glob
import re
import os

# https://docs.python.org/3/howto/regex.html
padrao = re.compile('@[a-z]+\.[a-z]+')

# https://docs.python.org/3/library/glob.html#glob.glob
historias = glob.glob('historinhas/[a-z]*.md')

citacoes = {}
for h in historias:
    # https://docs.python.org/3/library/os.path.html#os.path.basename
    nome = os.path.basename(h)[:-3]
    print(nome)
    with open(h) as arq:
        conteudo = arq.read()
        citacoes[nome] = [cit[1:].lower() for cit in list(set(padrao.findall(conteudo)))]
        if nome in citacoes:
            citacoes[nome].remove(nome)


with open('grafo-citacoes.dot', 'w') as arq_grafo:
    arq_grafo.write('digraph citacoes {\n');
    for citador,citados in citacoes.items():
        for citado in citados:
            arq_grafo.write(f'    {citador} -> {citado};\n');
            # https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
               
    arq_grafo.write('}\n');
