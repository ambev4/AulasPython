# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime

emprestimo = 1000
data_inicio = datetime(2020, 12, 20)
tempo_financiamento = (5, 0)


def valor_parcela(emprestimo, numero_parcelas):
    return emprestimo / numero_parcelas

def cria_financiamento(*args, **kwargs):
    def numero_parcela(years=0, mounths=0):
        if isinstance(years, int) and isinstance(mounths, int) and mounths > 12:
            raise TypeError('Param deve ser int')
        print(years)
        if years is not None:
            years *= 12
        return years + mounths
    return numero_parcela

emprestimo_Maria = cria_financiamento(5, 0)

print(emprestimo_Maria())