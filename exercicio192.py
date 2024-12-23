# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

tarefas, desfazer_tarefas = [], []

while True:
    print('Comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa ou comando: ')
    print('')

    if not comando.replace(" ", "").isalpha():
        print('Digite apenas tarefas com letras')
        continue

    if comando.lower() == 'listar':
        print('TAREFAS:\n')
        for tarefa in tarefas:
            print(tarefa)
        print('')
    elif comando.lower() == 'desfazer':
        if tarefas:
            item = tarefas.pop()
            desfazer_tarefas.append(item)# Adicionar este valor retirado na lista de desfazer_tarefass
    elif comando.lower() == 'refazer':
        if desfazer_tarefas:
            item = desfazer_tarefas.pop()
            tarefas.append(item)# Adicionar este valor retirado na lista de tarefas 
    else:
        tarefas.append(comando)
    print('')