"""
Criar variáveis recebendo diretamente lambdas é uma má prática de programação, o recomendado é 
criar uma função que executa funções lambdas como mostrado abaixo.

A ideía da lambda é simplificar as coisas, não complicar. O uso dela é principalmente em 
funções pequenas para se escrever em uma linha, caso esteja ficando complexxo de mais
criar uma função nomeada normalmente.

Lambdas tbm podem retornar outras funções.
"""


def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)