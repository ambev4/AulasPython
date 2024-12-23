print('Jogo da palavra secreta, digite uma letra por vez para tentar descobrir qual palavra é.')

palavra_secreta = 'paralelepipedo'
letras_digitadas = ''
tentativas = 0
palavra_revelada = ''
while palavra_revelada != palavra_secreta:

    letra = input('Digite uma letra: ')

    if not letra:
        print('Digite alguma letra')
        continue
    
    elif len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    elif letra in letras_digitadas:
        print('Voce já digitou essa letra')

    if letra in palavra_secreta:
        letras_digitadas += letra
    palavra_revelada = ''
    
    for letra_secreta in palavra_secreta:
        letra_revelada = False
        for letra_digitada in letras_digitadas:        
            if letra_digitada == letra_secreta:
                letra_revelada = True
                palavra_revelada += letra_digitada
        if not letra_revelada:
            palavra_revelada += '*'
    print(f'{palavra_revelada}')
    tentativas += 1

print(f'Parabéns! A palavra secreta é {palavra_secreta}')
print(f'\nNúmero de tentativas :{tentativas}')


