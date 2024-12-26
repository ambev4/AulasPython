from pathlib import Path

caminho_arquivo = Path(__file__) # Recebe caminho absoluto

teste_txt = caminho_arquivo.parent / 'teste.txt' # Adiciona o nome do arquivo ao caminho da pasta acima do caminho absoluto do arquivo

caminho_arquivo = Path.home() / 'Aulas Python' / 'arquivo.txt' # Path.home() retorna a pasta home do user
caminho_arquivo.touch() # Igual o touch do Linux
caminho_arquivo.write_text('Olá Mundo') # Escreve no arquivo sem append
caminho_arquivo.unlink() # apaga o arquivo

caminho_pasta = Path.home() / 'Aulas Python' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True) # Cria uma pasta
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

#caminho_pasta.rmdir() # Remove diretório se estiver vazio

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'arquivo_{i}.txt'

    if file.exists(): # Retorna True ou False se existir
        file.unlink()
    else:
        file.touch()

    with file.open('a+', encoding='utf-8') as text_file: # Outra forma de trabalhar com Path e open juntos
        text_file.write('Olá mundo\r\n')
        text_file.write(f'arquivo_{i}.txt')

def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'): # Retorna lista de arquivos e subpastas iterável
        if file.is_dir(): # Retorna True ou False se for diretório
            rmtree(file, False) # Recursividade da função, ela se executa com parametros atualizados
            file.rmdir()
        else:
            file.unlink()
    if remove_root:
        root.rmdir()

rmtree(caminho_pasta) # Outra opção para fazer isso é o rmtree do shutil