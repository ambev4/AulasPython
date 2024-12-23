adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # retorno desse operador sempre é float
print('Divisão', divisao)

"""
Este operador abaixo retorna numero inteiro quando possível(dois números inteiros que resultam outro número inteiro),
quando não resultar número inteiro ele retornar um valor float ignorando as casas decimais e setando como '0'
"""

divisao_inteira = 10 // 2.3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 60 % 5  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0) # Checa se é múltiplo de 8 se é divisível por 8
print(16 % 8 == 0)
print(10 % 2 == 0) # Checa se o número é par se é divisível por 2
print(15 % 2 == 0)
print(16 % 2 == 0)

#Concatenação:
nome = 'Lucas ' + 'Barbosa'
print(nome)

#Repetição:
grito = 'aaah ' * 10
risada = 4 * 'kkkk'
print(grito)
print(risada)

# Para raiz quadrada, usar operador de exponenciação
teste = 27 ** (1 / 2)
print(teste)
teste = 27 ** 0.5
print(teste)