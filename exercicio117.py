def mult(n): # Primeiro passo é entender que as funções de dentro tem acesso ao argumento da função de fora
    def duplicar():
        return n * 2
    def triplicar():
        return n * 3
    def quadruplicar():
        return n * 4
    return duplicar(n), triplicar(n), quadruplicar(n)


#print(mult(2))


def multv2(numero, quantidade):
    def operacao(n, q):
        n *= q
        return n
    for i in range(quantidade, 2, -1):
        print(i * numero)

#multv2(2, 10)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
"""
# Importante entender que o retorno de função sem executar-la irá armazenar a função na memória
 e não o resultado de execução dela
"""

t1 = criar_multiplicador(5)
"""
A variável t1 está recebendo a função multiplicar uma vez que a função criar_multiplicador está retornando
a multiplicar sem executá=la, por isso ela passa um comportamento como se estivesse craindo uma nova função
porque ela está armazenando a função multiplicar na variável t1 com o parâmetro 5
"""
print(t1(2)) # Aqui estou passando a execução da função que ficou no return da anterior

tupla = []
for i in range(20, 1, -1):
    tupla.append(t1(i))
print(tuple(tupla))

"""
O objetivo deste recurso é economizar linhas de código, imaginando que fosse uma função muito grande
em linhas e que precisasse se repetir várias vezes, essa mesma repetição seria resumida na atribuição
da função sem executar à uma variável, no caso na linha 32 deste código

"""