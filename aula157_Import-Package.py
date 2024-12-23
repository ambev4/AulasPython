from sys import path
"""
Diferentes formas de importar módulo dentro de pacotes (package)
"""
import aula157_package.modulo
from aula157_package import modulo # Achei esse mais legível
from aula157_package.modulo import *

# from aula157_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula157_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)