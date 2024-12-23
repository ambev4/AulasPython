"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
del lista[2] # Remove o valor junto com o índice da lista, não é um método
# print(lista)
# print(lista[2])
lista.append(50) # Adiciona o item do argumento no final da lista
lista.pop() # Remove o último item da lista e retorna o seu valor
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # Remove o item de índice 3 da lista e retorna o seu valor
print(lista, 'Removido,', ultimo_valor)