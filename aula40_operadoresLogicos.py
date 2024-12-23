# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')  

# Avaliação de curto circuito
# print(True and False and True)
print(False and not False)
# print(True and 0 and True) # Neste caso retorna o valor 0 pois é considerado False pelo Python

"""
# Avaliação de curto circuito, ao encontrar um valor Falso em uma expressão que precisa ser toda verdadeira,
a linguagem nem checa mais o resto para economizar recurso
"""