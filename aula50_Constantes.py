"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade_1 = 59  # velocidade atual do carro
local_carro = 50  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if local_carro not in ((LOCAL_1 - RADAR_RANGE), LOCAL_1, (LOCAL_1 + RADAR_RANGE)):
    print('O carro não passou no radar')
elif velocidade_1 > RADAR_1: #Para mudar o nome de todas as variáveis, selecionar e apertar F2
    print('O carro passou acima da velocidade no radar')
else:
    print('O carro passou dentro da velocidade do radar')

"""
Pensando em código enxugado que é o tema da aula, eu faria dessa forma,
mas se fosse algo que um erro de lógica fosse fatal eu deixaria a
condição do if redundante no elif dessa forma:
elif local_carro in ((LOCAL_1 - RADAR_RANGE), (LOCAL_1), (LOCAL_1 + RADAR_RANGE)) and velocidade > RADAR_1:
"""