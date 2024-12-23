"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#Primeira solução (a que eu pensei):
num = input('Digite um número inteiro: ')

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
except:
    print('Isso não é um número inteiro')

#Solução do professor (Bem melhor, esqueci da existência desse método isdigit()):

num = input('Digite um número inteiro: ')

if num.isdigit(): # Este método retorna True se a string possui apenas números e tem pelo menos 1 character
    num_int = int(num)
    if num_int % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
else:
    print('Isso não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são agora?: ')

if hora.isdigit():
    hora_int = int(hora)
    if hora_int >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora_int > 17 and hora < 24:
        print('Boa noite!')
    else:
        print('Digite a hora no formato de 0 a 23!')
else:
    print('Digite a hora no formato de 0 a 23!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Escreva seu primerio nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
    else:
        print('Seu nome é normal')
else:
    print('Digite mais de uma letra')

"""
Resolvi começar a atribuir variáveis diferentes para tipos diferentes de dados pra se um dia surgir a necessidade
de voltar a utilizar o formato original da primeira variável, ela ainda estar disponível. Isso gera algumas
linhas de código a mais do que simplesmente transformar a mesma variável em um valor diferente mas a longo
prazo acredito que vai ser bom pegar esse costume.
"""