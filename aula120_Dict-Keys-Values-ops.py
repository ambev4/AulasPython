# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None: # Este método retorna None por padrão se a chave não existir
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome']) # Se existir ele retorna o valor da chave

# print('ISSO Não vai')