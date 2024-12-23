"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
#del lista[-1] # A contagem de índice invertida é útil quando vc não sabe o tamanho dela
# lista.clear() # Limpa todo o conteúdo e índices da lista
lista.insert(-1, 5) # Primeiro argumento é o índice que vc quer inserir o segundo é o seu valor
# Não sei pq mas se vc passar -1 no indice do método insert, ele entende como o penúltimo ao invés do último
print(lista)