""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

"""
No python, o while tem else. O else é executado unica e exclusivamente no término natural do laço
do while, isso significa que caso seja forçadamente finalizado a partir de um break, por exemplo
o else não é executado.
"""