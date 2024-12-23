"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
"""
Para copiar o valor de uma lista para outra usasse
esse método copy (Isso se a lista for apenas de objegos imutáveis).
Sem o método copy as duas variáveis irão apontar para o mesmo objeto em memória,
o que vai causar situações de alterações em uma das variáveis irá replicar para outra e vise versa
"""
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

valor_a = lista_a[0]

lista_a[0] = 123

print(valor_a, lista_a)