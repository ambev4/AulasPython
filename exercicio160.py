# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = [ 
    {**produto, 'preco': round(produto['preco'] * 1.1, ndigits=2)}
    for produto in produtos
]

# produtos_ordenados_por_nome = [
#     {**produto}
#     for produto in produtos
# ]
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_preco = copy.deepcopy(produtos)

def get_dict_in_list(item, chave):
    return item[chave]

# O ideal seria resolver com uma função mesmo, mas um lambda pra esse caso basta
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)


# produtos_ordenados_por_preco = [
#     {**produto}
#     for produto in produtos
# ]

produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])

produtos[0]['nome'] = 'Teste' # Testando a deepcopy

print(*novos_produtos, sep='\n')
print(*produtos_ordenados_por_nome)
print(*produtos_ordenados_por_preco)