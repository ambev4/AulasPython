lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y) # List comprehension com mais de um for para gerar uma tupla
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x, letra) for letra in 'Luiz'] # List comprehension para gerar tuplas dentro de uma lista para cada letra da str
    for x in range(3)
]

print(lista)