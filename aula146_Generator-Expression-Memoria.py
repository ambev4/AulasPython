import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000)) # É um interável que não carrega o elemento inteiro na memória,
# ele vai carregando valores um de cada vez

print(sys.getsizeof(lista)) # Exibe tamanho em bytes(ou bites?) que o objeto está ocupando na memória
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)