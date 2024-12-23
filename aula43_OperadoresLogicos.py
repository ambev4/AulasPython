# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

# nome = input('Digite seu nome: ')
# encontrar = input('Digite o que deseja encontrar: ')

# if encontrar in nome:
#     print(f'{encontrar} está em {nome}')
# else:
#     print(f'{encontrar} não está em {nome}')

# print('pato' in 'carrapato') Aqui ele está checando se existe uma sequência de letras em outra sequência de letras

nome = input('Digite seu nome ')
encontrar = input('Digite o que deseja encontrar ') 

"""
Neste caso aqui ele está checando se ancontrar está em nome E se nome é igual á True, por isso o valor indesejado.
Prestar atenção na ordem de execução dos operadores assim como na aritimética.
"""

if encontrar in nome == True:
    print (f'{encontrar} está em {nome} ') 
else: 
    print(f'{encontrar} não está em {nome}')