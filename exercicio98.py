from os import system
print('Validação de CPF')

cpf_validado = False

while True:
    print('Formato válido para CPF: XXX.XXX.XXX-XX')
    cpf_digitado = input('Digite o CPF com pontos e traço ou [s]air para sair: ')

    # Validação do formato do CPF digitado pelo usuário
    if len(cpf_digitado) == 14 and cpf_digitado.count('-') == 1 and cpf_digitado.count('.') == 2:
        cpf, digito = cpf_digitado.split('-')
        if not digito.isnumeric() or len(digito) != 2:
            system('cls')
            print('Digite o CPF no formato correto XXX.XXX.XXX-XX com X sendo apenas números')
            continue
        for numero in cpf.split('.'):
            if not numero.isnumeric() or len(numero) != 3:
                system('cls')
                print('Digite o CPF no formato correto XXX.XXX.XXX-XX com X sendo apenas números')
            else:
                system('cls')
                cpf_validado = True
    elif cpf_digitado == 's':
        system('cls')
        break
    else:
        system('cls')
        print('Digite o CPF no formato correto XXX.XXX.XXX-XX com X sendo apenas números')
    
    # Validação do primeiro dígito do CPF
    primeiro_digito = False
    if cpf_validado == True:
        soma = 0
        multiplicador = 10
        for numero in cpf:
            if numero == '.':
                continue
            else:
                soma += int(numero) * multiplicador
                multiplicador -= 1
        
        soma *= 10
        soma %= 11
        
        soma = 0 if soma > 9 else soma
        # if soma > 9:
        #     soma = 0
        if soma == int(digito[0]):
            primeiro_digito = True
        else:
            print('Primeiro dígito do CPF errado!')

    # Validação do segundo dígito do CPF
    if cpf_validado and primeiro_digito:
        soma = 0
        multiplicador = 11
        for numero in cpf:
            if numero == '.':
                continue
            else:
                soma += int(numero) * multiplicador
                multiplicador -= 1
        else:
            soma += (int(digito[0]) * multiplicador)
        soma *= 10
        soma %= 11
        soma = 0 if soma > 9 else soma
        # if soma > 9:
        #     soma = 0
        if soma == int(digito[1]):
            print('CPF válido!')
        else:
            print('Segundo dígito do CPF errado!')