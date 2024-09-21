import requests
import time
import sqlite3

# Substitua com a sua chave de API do TMDB
API_KEY = 'd90c32b085b4cb92bcac3d5bd6d92ae2'
BASE_URL = 'https://api.themoviedb.org/3'

# Função para buscar detalhes dos filmes
def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar detalhes do filme {movie_id}: {response.status_code}")
        return None

# Função para buscar diretores do filme
def get_movie_credits(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        credits = response.json()
        # Filtra diretores da lista de equipe (crew)
        directors = [member['name'] for member in credits['crew'] if member['job'] == 'Director']
        return directors
    else:
        print(f"Erro ao buscar créditos do filme {movie_id}: {response.status_code}")
        return []

# Inicializa o banco de dados SQLite
conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        nota REAL,
        generos TEXT,
        diretores TEXT
    )
''')
conn.commit()

# Função para buscar filmes populares
def get_popular_movies(page=1):
    url = f"{BASE_URL}/movie/popular"
    params = {'api_key': API_KEY, 'page': page}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Erro ao buscar filmes populares: {response.status_code}")
        return []

# Coleta dados de n filmes
n_filmes = 20000  # Defina o número de filmes que deseja coletar
filmes_coletados = 0
pagina = 1

while filmes_coletados < n_filmes:
    filmes = get_popular_movies(pagina)
    if not filmes:
        break

    for filme in filmes:
        if filmes_coletados >= n_filmes:
            break
        try:
            # Coleta detalhes do filme
            detalhes = get_movie_details(filme['id'])
            if not detalhes:
                continue

            titulo = detalhes['title']
            nota = detalhes['vote_average']
            generos = ', '.join([genero['name'] for genero in detalhes['genres']])
            diretores = ', '.join(get_movie_credits(filme['id']))

            # Insere os dados no banco de dados
            cursor.execute('''
                INSERT INTO filmes (id, titulo, nota, generos, diretores)
                VALUES (?, ?, ?, ?, ?)
            ''', (filme['id'], titulo, nota, generos, diretores))
            conn.commit()

            filmes_coletados += 1
            print(f"Coletado: {titulo}")

            # Pausa para respeitar o limite de requisições por segundo (20 por 10 segundos)
            time.sleep(0.5)  # Ajuste conforme necessário para não ultrapassar os limites da API
        except:
            time.sleep(0.5) 
            print("unable to collect this movie")
            continue
        
        

    pagina += 1

conn.close()
print(f"Coleta de dados concluída. Total de filmes coletados: {filmes_coletados}")