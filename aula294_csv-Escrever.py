# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path
CAMINHO_CSV = Path(__file__).parent / 'aula294.csv'
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter( # Cria o objeto passando esse parâmetro do fieldname
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader() # Método para escrever o nome das colunas
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente) # Escreve as linhas do csv com os dicionários
# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)
#     escritor.writerow(nome_colunas)
#     for cliente in lista_clientes:
#         escritor.writerow(cliente)