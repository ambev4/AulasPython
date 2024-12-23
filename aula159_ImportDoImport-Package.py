# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula159_package.modulo
# from aula159_package import modulo
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)

"""
Criando um __init__.py  no package, faz com que código nele seja imediatamente executado ao importá-lo,
fazendo com que o package aja como um módulo se nele conter os imports dos módulos dentro dele.
"""
# from aula159_package.modulo import fala_oi, soma_do_modulo
# from aula99_package.modulo import fala_oi, soma_do_modulo

# print(__name__)
# fala_oi()
# print(__name__)
# fala_oi()

#from aula159_package import fala_oi, soma_do_modulo, variavel_teste

import aula159_package

print(aula159_package.soma_do_modulo(2, 3))
aula159_package.fala_oi()

print(aula159_package.variavel_teste)