nome = 'Lucas Barbosa'
altura = 1.76
peso = 73
imc = peso / altura ** 2

# f-strings:
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} kilos e seu IMC é'
linha_3 = f'{imc:.2f}'

"""
f-strings podem receber valor de variáveis sem necessidade de conversão e além disso
os valores podem ser formatados como no exemplo da aula, especificando o número de casas
decimais exibidas após a vírgula.
"""

# Método format:
linha_1 = '{} tem {} de altura, {}'.format(nome, altura, 'teste')
linha_2 = 'pesa {} kilos e seu IMC é'.format(peso)
linha_3 = '{:.2f}'.format(imc)
teste_indice = 'Valores em ordem invertida: {3:.2f}, {2}, {1}, {0}'.format(nome, altura, peso, imc)

"""
O método format adiciona o valor das variáveis informadas no campo de argumentos
em suas respectivas chaves dentro da string seguindo a ordem de cada uma. A formatação
é indicada dentro das chaves na string.
Também é possível passar valores diretos nos argumentos da função.
Nas chaves dentro da string existe a possibilidade de indicar os valores através dos indices
de cada um, possibilitando assim exibir os valores na ordem desejada independentemente da ordem
dos argumentos da função e também repetição de valores caso seja necessário.
"""

print(linha_1)
print(linha_2)
print(linha_3)
print(teste_indice)

"""
Parâmetros nomeados podem ser indicados nos argumentos da função ou método
caso sejam nomeados o indice deve ser usado com o nome ao invés dos números.
Todos os parametros em seguida do que foi nomeado também devem ser nomeados,
se existir outros parametros anteriores eles seguem a lógica de números nos índices.
Exemplo:
"""
teste_indice = 'Valores em ordem invertida: {imc:.2f}, {peso}, {1}, {0}'.format(nome, altura, peso=peso, imc=imc)
print(teste_indice)

# Quando nomeado é chamado de parametro e quando a referência for o valor da variável é um argumento
