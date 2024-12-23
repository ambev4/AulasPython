"""
Nesse exercício eu quis o desafio de tentar fazer tudo num input só utilizando while
"""

print(f'Calculadora de 1 input\n+ soma,\n- subtração,\n*  multiplicação,\
      \n/ divisão,\n ^ exponenciação')
conta_str = ''
while conta_str != 'sair':
    conta_str = input('Digite a conta com a operação. Ex: 2+2 ou sair para sair :')
    cont_conta = 0
    digito1_str = ''
    digito2_str = ''
    while cont_conta < len(conta_str):
        if conta_str[cont_conta].isdigit():
            digito1_str += conta_str[cont_conta]
        #elif conta_str[cont_conta] == '+' or conta_str[cont_conta] == '-' or conta_str[cont_conta] == '*' or conta_str[cont_conta] == '/' or conta_str[cont_conta] == '^':
        elif conta_str[cont_conta] in '+-*/^':    
            operacao_str = conta_str[cont_conta]
            cont_conta += 1
            while cont_conta < len(conta_str):
                if conta_str[cont_conta].isdigit():
                    digito2_str += conta_str[cont_conta]
                cont_conta += 1
        else:
            break
        cont_conta += 1
    if digito1_str.isdigit() and digito2_str.isdigit():
        digito1_float = float(digito1_str)
        digito2_float = float(digito2_str)

        if operacao_str == '+':
            print(digito1_float + digito2_float)
        elif operacao_str == '-':
            print(digito1_float - digito2_float)
        elif operacao_str == '*':
            print(digito1_float * digito2_float)
        elif operacao_str == '/':
            print(digito1_float / digito2_float)
        elif operacao_str == '^':
            print(digito1_float ** digito2_float)
    elif conta_str == 'sair':
        continue
    else:
        print('Digite a conta no seguinte formato: Ex. 6*2 Apenas numeros e operação')

