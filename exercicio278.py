# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000
data_inicio = datetime(2020, 12, 20)
tempo_financiamento = relativedelta(years=5)
data_final = data_inicio + tempo_financiamento


data_parcelas = []
data_parcela = data_inicio

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

fmt = '%d/%m/%Y'
valor_parcelas = (emprestimo / len(data_parcelas))
for data in data_parcelas:
    print(datetime.strftime(data, fmt), round(valor_parcelas, ndigits=2))