import requests
import csv
import time

# Substitua pela sua chave da API do TMDB
API_KEY = 'd90c32b085b4cb92bcac3d5bd6d92ae2'
TMDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
TMDB_MOVIE_URL = 'https://api.themoviedb.org/3/movie/'

# Função para buscar o ID do filme pelo título
def buscar_filme_id(titulo):
    params = {
        'api_key': API_KEY,
        'query': titulo,
        'language': 'en-US',  # Buscamos pelo título em inglês
    }
    response = requests.get(TMDB_SEARCH_URL, params=params)
    if response.status_code == 200 and response.json()['results']:
        return response.json()['results'][0]['id']  # Retorna o ID do primeiro filme encontrado
    return None

# Função para buscar dados detalhados de um filme pelo ID
def buscar_dados_filme(filme_id):
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR',  # Dados em português
        'append_to_response': 'credits'
    }
    response = requests.get(f'{TMDB_MOVIE_URL}{filme_id}', params=params)
    if response.status_code == 200:
        filme = response.json()
        
        # Título em português
        titulo = filme.get('title', 'N/A')
        
        # Nota média
        avaliacao = filme.get('vote_average', 'N/A')
        
        # Diretor (procuramos nos créditos)
        diretor = 'N/A'
        for pessoa in filme['credits']['crew']:
            if pessoa['job'] == 'Director':
                diretor = pessoa['name']
                break
        
        # Gêneros
        generos = ', '.join([genero['name'] for genero in filme.get('genres', [])])
        
        return {
            'title': titulo,
            'rating': avaliacao,
            'director': diretor,
            'genres': generos
        }
    return None

# Função principal para processar o arquivo CSV
def processar_csv(input_csv, output_csv, limite=1000):
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ['title', 'rating', 'director', 'genres']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i, row in enumerate(reader):
            if i >= limite:
                break
            
            titulo_ingles = row['Title']
            filme_id = buscar_filme_id(titulo_ingles)
            
            if filme_id:
                dados_filme = buscar_dados_filme(filme_id)
                if dados_filme:
                    writer.writerow(dados_filme)
            
            # Pausa para evitar excesso de requisições
            time.sleep(0.3)

# Substitua pelos caminhos corretos dos arquivos
input_csv = 'titulos.csv'  # Caminho do CSV de entrada
output_csv = 'resultado_filmes.csv'  # Caminho do CSV de saída

# Executa o processo para as primeiras 1000 linhas
processar_csv(input_csv, output_csv, limite=1000)
