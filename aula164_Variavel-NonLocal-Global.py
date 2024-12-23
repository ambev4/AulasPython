# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())



# Dessa forma abaixo, como parâmetro a função de dentro tem acesso ao valor estabelecido.
# Mas dessa forma vc não consegue guardar o valor da execução anterior da função
# para caso queira ir incrementando mais strings por exemplo

# def concatenar(string_inicial):
#     def interna(valor_a_concatenar=''):
#         return string_inicial + valor_a_concatenar
#     return interna

# Porém, como variável de dentro da função interna, vc precisa especificar que está buscando 
# o valor da função de fora utilizando o nonlocal.
# Pelo valor estar sendo armazenado em variável antes da execução, é possível guardar o 
# valor anterior e ir incrementando strings, por exemplo.

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)