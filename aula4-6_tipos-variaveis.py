# print(123)
# print(123)
print(type(123), type('teste')) # Classe type retorna o tipo de variável argumentada
print(type(10 == 10), 12 == 1) # Comparação de operadores lógicos, retorna um valor boolean

# Polimorfismo é utilizar a mesma coisa para finalidades ou operações diferentes
# Tipagem fraca está relacionada com a plavra 'type' de escrita, ou seja escrita fraco ou forte. 

"""
Isso significa que a tipagem forte será mais exigente na escrita e atribuições de variáveis. 
Ex: '1' + 1 ele não vai entender op que fazer com uma soma de str e int
"""

# str, int, float e bool são tipo de variáveis imutáveis
print(type(int('1')))
print(int(int('1') + 2.999)) # Convertendo um float para int, ele simplesemnte ignora o valor decimal depois do ponto
print(bool(0), bool(2)) # Convertendo int para bool, 0 é False e qualqeur outro valor será verdadeiro
print(bool(''), bool(' ')) # string vazia é False e string com qualquer valor é True
print('Eu tenho ' + str(31) + ' anos') # Soma de strings resulta em uma concatenação
idade = 31
maior_de_idade = idade >= 18 # Atribuição de variável a partir de uma condição via operadores lógicos é uma boolean