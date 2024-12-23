# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'aula187.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n') # Escreve em uma linha
    arquivo.write('Linha 2\n')
    arquivo.writelines( # Escreve em linhas um íteravel
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read()) # Lê o arquivo inteiro
    print('Lendo')
    arquivo.seek(0, 0) # Posiciona o cursos do python
    print(arquivo.readline(), end='') # readline lê uma linha como se fosse um next
    print(arquivo.readline().strip()) # Strip remove espaços e quebras de linha
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): # Vira uma lista de linhas
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())