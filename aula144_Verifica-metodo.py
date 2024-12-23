# dir, hasattr e getattr em Python

"""
dir retorna todos os atributos da classe
"""
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo): # Retorna True ou False se o objeto tem ou não esse método
    print('Existe upper')
    print(getattr(string, metodo)()) # Retorna o método ou executa ele dessa forma
else:
    print('Não existe o método', metodo)