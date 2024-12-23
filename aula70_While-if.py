frase = 'O Python é uma linguagem de programação ' 'multiparadigma. ' + \
    'Python foi criado' \
    'por Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1
print(frase)
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)

"""
Quebra de linhas em variáveis deve se fechar as aspas, barra invertida (\), enter, tab e por fim abrir e
fechar de aspas novamente, como no exemplo da varável "frase". 

A concatenação de strings é entendida automaticamente pelo Python apenas colocando uma string, espaço,
outra string, sem precisar do sinal de "+". Exemplo do último print e da variável frase neste programa.

Método count percorre toda string e retorna o número de caracteres (ou sequência de caracteres)
passado previamente no argumento da função.
"""