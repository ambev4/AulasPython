# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz') # Adiciona um único valor, se tentar por mais argumentos da erro
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4)) # Adiciona um interável, pode ser usado pra adicionar vários valores com uma tupla
# s1.clear() # Limapa todo o set
s1.discard('Olá mundo') # Apaga o item com valor do argumento
s1.discard('Luiz')
print(s1)