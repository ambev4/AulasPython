# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')


"""
O while é mais utilizado para coisas que possuem quantidade de laços dinâmicos ou imprevisíveis,
por exemplo a quantidade de vezes que o usuário tentará digitar uma senha para um login.
O for é utilizado para situações no qual a repetição de laços é previsível, como por exemplo
iterar cada um dos valores de uma string ou uma lista.
"""