# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def cria_funcao(func):
    def mergelist_checkparam(*args, **kwargs):
        for arg in args:
            is_list(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return mergelist_checkparam

@cria_funcao
def mergelist(list1, list2):
    # if len(list1) < len(list2) :
    #     lista = len(list1)
    # else:
    #     lista = len(list2)
    indice = min(len(list1), len(list2)) # função min trás o menor número e max o maior
    lista_concatenada = [
        (list1[i], list2[i])
        for i in range(indice)
    ]
    return lista_concatenada

def is_list(value):
    if not isinstance(value, list):
        raise TypeError('Param deve ser uma lista')
    

junta_listas = mergelist(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['5'])
print(junta_listas)

#print(mergelist)


# Resolução com funções prontas feita pelo professor:

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2))) # Função zip junta valores de 2 listas em tuplas em uma lista
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
# Função zip_longest faz a mesma coisa porém usa a maior lista e preenche o que faltar com algum outro valor
