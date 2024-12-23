perguntas = [
    {
        'Pergunta': 'Quais países não fazem fronteira com o Brasil?',
        'Opções': ['Chile e Equador', 'Chile e Venezuela', 'Equador e Peru'],
        'Resposta': '1',
    },
    {
        'Pergunta': 'O colesterol: Qual elemento faz parte do inicio de sua formação?',
        'Opções': ['Glicose', 'Acetil COA', 'Gordura Saturada'],
        'Resposta': '3',
    },
    {
        'Pergunta': 'O licopeno está presente em qual alimento?',
        'Opções': ['Alface', 'Pera', 'Tomate'],
        'Resposta': '3',
    }
]

acertos = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')
    print('')
    print(f'Opções:')
    # for opcao in enumerate(pergunta['Opções']):
    #     print(f'{opcao[0] + 1}) {opcao[1]}')

    for i, opcao in enumerate(pergunta['Opções']): # Lembrar que existe o desempacotamento no for
        print(f'{i + 1}) {opcao}')

    resposta_digitada = input('Escolha uma alternativa: ')

    if resposta_digitada == pergunta['Resposta']:
        print(f'Acertou 🙌')
        acertos += 1
        print('')
    else:
        print(f'Resposta errada ❌')
        print('')

print(f'Você acertou {acertos} perguntas de {len(perguntas)} perguntas.')