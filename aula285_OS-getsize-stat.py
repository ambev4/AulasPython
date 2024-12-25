import os, math

base_dir = os.path.abspath('.')

# def formata_tamanho(tamanho: int) -> str:
#     if tamanho <= 0:
#         return '0 B'

#     if tamanho < 1024:
#         return str(tamanho) + ' B'
#     elif tamanho >= 1024 and tamanho < (1024 ** 2):
#         potencia = 1024 ** 1
#         tamanho /= potencia
#         return str(round(tamanho, 2)) + ' KB'
#     elif tamanho >= (1024 ** 2) and tamanho < (1024 ** 3):
#         potencia = 1024 ** 2
#         tamanho /= potencia
#         return str(round(tamanho, 2)) + ' MB'
#     elif tamanho >= (1024 ** 3) and tamanho < (1024 ** 4):
#         potencia = 1024 ** 3
#         tamanho /= potencia
#         return str(round(tamanho, 2)) + ' GB'
#     else:
#         potencia = 1024 ** 4
#         tamanho /= potencia
#         return str(tamanho) + ' TB'

def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # Logaritmo é resultado de "a base é preciso elevar a quanto pra dar aquele resultado que está sendo passado"
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base)) # Método int ignora as casas decimais
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


for arquivo in os.listdir(base_dir):
    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
    if extensao_arquivo != '.py':
        continue

    stats = os.stat(arquivo)
    print(stats) # Tupla com alguns atributos de arquivo
    tamanho = stats.st_size
    # print(arquivo, formata_tamanho(os.path.getsize(arquivo)))
    print(arquivo, formata_tamanho(tamanho))

