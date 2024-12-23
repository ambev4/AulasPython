primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior do que o {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior do que o {primeiro_valor=}")
else:
    print("Os valores digitados são iguais")


"""
O '=' na frente da variável das chaves nas f-strings formata
o texto no formato: nome_da_variavel='valor_da_variável'
"""