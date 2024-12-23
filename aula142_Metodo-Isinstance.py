# isinstace - para saber se objeto é de determinado tipo
"""
Recebe o item a ser checado como primeiro parâmetro e uma classe de segundo parâmetro,
checa se o item pertence à aquela classe e retorna True ou False.

"""
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)