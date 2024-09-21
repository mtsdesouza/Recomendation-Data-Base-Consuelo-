import requests
import csv
import time

# Chave da API do TMDB
api_key = 'd90c32b085b4cb92bcac3d5bd6d92ae2'


api_url = 'https://api.themoviedb.org/3/search/movie'
details_url = 'https://api.themoviedb.org/3/movie/{movie_id}'
headers = {'Authorization': f'Bearer {api_key}'}

def get_movie_data(title):
    # Faz a busca do filme pelo título
    params = {
        'api_key': api_key,
        'query': title,
        'language': 'pt-BR'
    }
    
    response = requests.get(api_url, params=params)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if data['total_results'] == 0:
        return None
    
    movie_id = data['results'][0]['id']
    
    # Faz a busca dos detalhes do filme pelo movie_id
    movie_details = requests.get(details_url.format(movie_id=movie_id), params={'api_key': api_key, 'language': 'pt-BR'})
    
    if movie_details.status_code != 200:
        return None
    
    details = movie_details.json()

    # Busca os gêneros
    genres = ', '.join([genre['name'] for genre in details['genres']])
    
    # Busca o diretor
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    credits = requests.get(credits_url, params={'api_key': api_key, 'language': 'pt-BR'}).json()
    
    director = None
    for member in credits['crew']:
        if member['job'] == 'Director':
            director = member['name']
            break

    # Retorna os dados do filme
    return {
        'title': details['title'],
        'rating': details.get('vote_average', 'N/A'),
        'director': director if director else 'Desconhecido',
        'genres': genres
    }

# Função principal que lê o CSV e processa as primeiras 1000 linhas
def process_movies(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        results = []
        
        # Processa as primeiras 1000 linhas
        for i, row in enumerate(reader):
            if i >= 1000:
                break
            
            title = row['Title']
            print(f'Processando o filme: {title}')
            
            try:
                movie_data = get_movie_data(title)
                if movie_data:
                    results.append(movie_data)
                    print(f'Sucesso ao buscar dados para: {title}')
                else:
                    print(f'Falha ao buscar dados para: {title}')
            except Exception as e:
                print(f'Erro ao processar o filme {title}: {str(e)}')
            
            # Pequeno delay para evitar sobrecarregar a API
            time.sleep(0.25)
    
    # Escreve os dados processados para um novo CSV
    with open('filmes_processados.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'rating', 'director', 'genres'])
        writer.writeheader()
        writer.writerows(results)

# Chame a função com o caminho para o seu arquivo CSV
process_movies('titulos.csv')

