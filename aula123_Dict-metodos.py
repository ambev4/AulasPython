# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave se ela não exxistir, retorna None
# pop - Apaga um item com a chave especificada (del) e retorna o valor apagado
# popitem - Apaga o último item adicionado e retorna o valor apagado
# update - Atualiza chaves e valores de um dict, se não existir chave e valor será criado
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = ('nome', 'novo valor'), # Tupla de um único valor tem como escrever dessa forma, uma vírgula vazia no final
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista) # Método update aceita listas, tuplas no formato de chave valor com listas dentro de listas e tuplas dentro de tuplas
# Também aceita argumentos nomeados como uma função:
p1.update(nome='novo valor', idade=32)
print(p1)