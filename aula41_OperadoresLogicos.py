# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

"""
Operadores lógicos não só podem ser usados em condições mas também em atribuição de valor de variáveis
juntos ou não com métodos como no exemplo do input.

Na avaliação de curto circuito do or, a linguagem ignora qualquer checagem após o primeiro True que encontrar
na expressão
"""