# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # Um return sem finalizar a função, pode ser colocado dentro de um laço while
        n += 1

        if n >= maximum:
            return # Ao atingir esse if o return sai da função e consequentemente sai do while 


gen = generator(maximum=1000000)
for n in gen:
    print(n)