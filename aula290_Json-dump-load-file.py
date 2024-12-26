import json
import os


NOME_ARQUIVO = 'aula290.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

filme_dict = json.loads(string_json)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(filme_dict, arquivo, ensure_ascii=False, indent=2)


with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    print(json.load(arquivo))