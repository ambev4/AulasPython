"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
indice = 0
nova_string = ''    
    
print(nome)    

while indice < len(nome):

    #nova_string += '*' + nome[indice]
    nova_string += f'*{nome[indice]}'
    indice += 1

print(nova_string)

