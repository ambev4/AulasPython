"""
Teste DocStrings
Esse tipo de recurso o interpretador lê e portanto processa
este recurso
"""
'''

DosStrings tbm podem ser 3 aspas simples e NÃO são consideradas como comentários 
apesar de poderem ser usadas como

'''

# Este comentário com # não é lido pelo interpretador, atalho para comentar linha = Ctrl + ;
print('Hello, world! 2')
# A linha abaixo printa 3
print('Hello, world! 3', end='@') # Essa linha printa 3, argumento nomeado end para definir separador padrão após o último valor do argumento
# A linha acima printa 3
print(12, 'Hello, world! 4', sep='-') 
# A função print pode receber mais de um argumento, argumento nomeado sep para definir separador padrão entre os valores
print('Estou destacando essa \'palavra\'') # Caracter de escape \ para ignorar o próximo caracter como um caracter de comando
print(r'Estou destacando essa \'palavra\'') # Caracter 'r' exibe o caracter de escape
# Aspas duplas dentro de aspas simples
print('Estou destacando essa "palavra"')
# Aspas simples dentro de aspas duplas
print("Estou destacando essa 'palavra'")
