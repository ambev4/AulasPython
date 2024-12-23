nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    texto_linha1 = f'Seu nome é {nome}'
    texto_linha2 = f'Seu nome invertido é {nome[::-1]}'
    if ' ' in nome:
        texto_linha3 = f'Seu nome contém espaço(s)'
    else:
        texto_linha3 = f'Seu nome não contém espaço'
    texto_linha4 = f'Seu nome tem {len(nome)} letras'
    texto_linha5 = f'A primeira letra do seu nome é {nome[0]}'
    texto_linha6 = f'A última letra do seu nome é {nome[-1]}'
    print(texto_linha1, texto_linha2, texto_linha3, texto_linha4,
          texto_linha5, texto_linha6, sep='\n')
else:
    print('Desculpe, você deixou campos vazios')
