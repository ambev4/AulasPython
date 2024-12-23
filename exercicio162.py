# Exercício - Adiando execução de funções


# def cria_soma(x):
#     def soma(y):
#         return x + y
#     return soma

# def cria_multiplicador(x):
#     def multiplica(y):
#         return x * y
#     return multiplica

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

# Sempre que tiver um adiamento de execução de função, PRECISA ter uma função que retorna outra sem executar
'''
Assim como as funções de cima, essa função abaixo adia a execução da função interna com a única diferença
das funções de cima estarem especificando a lógica lógicas dentro delas, enquanto à de baixo
está fazendo isso sem especificar a lógica aguardando receber ela das funções de fora que chegarão
como argumento
'''
def criar_funcao(funcao, x):
    def internal(y):
        return funcao(x, y) # O x está vindo da função externa e o y da função interna
    return internal

'''
O adiamento de execução de funções, permite criar funções com execuções semelhantes de forma rápida
e sem repetir código, por exemplo, com o criar_funcao(soma, x) eu posso criar um soma com 5, ou
um soma com 6, ou um soma com qualqeur outro valor específico sem ficar tendo que reescrever
esse valor específico em uma função, apenas passando como argumento na criação de funcão
e logo executando a "nova função" com apenas o valor que quer soma com 5 por exemplo.
'''
soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(5))
print(multiplica_por_dez(2))