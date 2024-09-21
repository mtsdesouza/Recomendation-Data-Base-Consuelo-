import requests
import csv
import os

def search_movie(title, api_key):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(search_url)
    return response.json()

def get_movie_details(movie_id, api_key):
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(details_url)
    return response.json()

def get_movie_credits(movie_id, api_key):
    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
    response = requests.get(credits_url)
    return response.json()

def find_director(credits):
    for crew_member in credits.get('crew', []):
        if crew_member['job'] == 'Director':
            return crew_member['name']
    return "Unknown"

def log_failed_title(title, file_path='failed_titles.csv'):
    """Grava títulos que não puderam ser processados em um arquivo CSV"""
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title])

def remove_failed_titles_file(file_path='failed_titles.csv'):
    """Remove o arquivo CSV de títulos falhados, se ele existir"""
    if os.path.exists(file_path):
        os.remove(file_path)

def read_titles_from_csv(file_path):
    """Lê os títulos de filmes de um arquivo CSV"""
    titles = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            titles.append(row[0])  # Assume que os títulos estão na primeira coluna
    return titles

def save_movie_data(title, rating, genres, director, file_path='movies_data.csv'):
    """Grava os dados dos filmes em um arquivo CSV"""
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([title, rating, ', '.join(genres), director])

def process_movie(title, api_key):
    try:
        # 1. Buscar o filme pelo título
        search_results = search_movie(title, api_key)
        
        if not search_results['results']:
            raise ValueError("Nenhum filme encontrado")

        # Pegar o ID do primeiro resultado relevante
        movie_id = search_results['results'][0]['id']
        
        # 2. Pegar detalhes do filme (nota e gêneros)
        movie_details = get_movie_details(movie_id, api_key)
        rating = movie_details.get('vote_average', 'N/A')
        genres = [genre['name'] for genre in movie_details.get('genres', [])]
        
        # 3. Pegar informações dos créditos (para buscar o diretor)
        movie_credits = get_movie_credits(movie_id, api_key)
        director = find_director(movie_credits)
        
        print(f"Título: {movie_details['title']}")
        print(f"Nota: {rating}")
        print(f"Gêneros: {', '.join(genres)}")
        print(f"Diretor: {director}")
        
        # Salvar dados do filme
        save_movie_data(movie_details['title'], rating, genres, director)
        
    except Exception as e:
        print(f"Erro ao processar '{title}': {e}")
        log_failed_title(title)

# Chave da API e arquivo de entrada
api_key = "d90c32b085b4cb92bcac3d5bd6d92ae2"
input_csv = "titulos.csv"  # Arquivo CSV com os títulos de filmes

# Remover arquivo de falhas se existir
remove_failed_titles_file()

# Criar ou limpar o arquivo de dados dos filmes
with open('movies_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Título', 'Nota', 'Gêneros', 'Diretor'])  # Cabeçalhos das colunas

# Ler os títulos do arquivo CSV
titles = read_titles_from_csv(input_csv)

# Processar cada título
for title in titles:
    process_movie(title, api_key)

# Remover o arquivo CSV de falhas se não houver falhas
if not os.path.exists('failed_titles.csv'):
    print("Todos os filmes foram processados com sucesso.")
else:
    print("Alguns filmes falharam ao processar. Veja 'failed_titles.csv'.")
