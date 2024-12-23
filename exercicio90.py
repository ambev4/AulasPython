import os
lista = []

while True:
    print('Lista de Compras')
    print('Selecione uma opção: ')
    opt = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opt == 'i':
        os.system('cls')
        item = input('Item: ')
        if item:
            lista.append(item)
    elif opt == 'a':
        i = input('Escolha o índice para apagar: ')
        try:
            del lista[int(i)]
        except:
            print('Não foi possível apagar este índice')
    elif opt == 'l':
        os.system('cls')
        if lista:
            for item in enumerate(lista):
                indice, nome = item
                print(indice, nome)
        else:
            print('Nada para listar')
    elif opt == 's':
        break
    else:
        print('Opção invalida, tente novamente')