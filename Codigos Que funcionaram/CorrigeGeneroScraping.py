import pandas as pd
import requests
import time

# Sua chave de API do TMDB
API_KEY ='d90c32b085b4cb92bcac3d5bd6d92ae2'


# Função para buscar o ID do filme no TMDB e obter os gêneros
def buscar_generos(filme):
    url_busca = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={filme}&language=pt-BR"
    resposta_busca = requests.get(url_busca)
    if resposta_busca.status_code == 200:
        resultados = resposta_busca.json().get('results', [])
        if resultados:
            # Pega o ID do primeiro resultado (o mais relevante)
            movie_id = resultados[0]['id']
            
            # Agora, busca os detalhes do filme pelo ID
            url_detalhes = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=pt-BR"
            resposta_detalhes = requests.get(url_detalhes)
            if resposta_detalhes.status_code == 200:
                detalhes_filme = resposta_detalhes.json()
                # Extrai os gêneros e junta os nomes em uma string
                generos = [g['name'] for g in detalhes_filme.get('genres', [])]
                return ', '.join(generos) if generos else 'Desconhecido'
    return 'Desconhecido'

# Carregar o arquivo CSV original
df = pd.read_csv('FilmesScraping.csv')

# Acompanhar o progresso
total_filmes = len(df)
print(f"Total de filmes: {total_filmes}")

# Iterar pelas linhas do DataFrame com enumerate para acompanhar o progresso
for idx, row in enumerate(df['Título (Ano)']):
    # Buscar e substituir o gênero
    df.at[idx, 'Gênero'] = buscar_generos(row)
    
    # Exibir o progresso
    print(f"Processado {idx+1}/{total_filmes}: {row}")
    
    # Esperar um pouco para não sobrecarregar a API (ajuste se necessário)
    time.sleep(0.5)

# Salvar o novo arquivo CSV com os gêneros atualizados
df.to_csv('FilmesScrapingAtualizado.csv', index=False)

print("Processo concluído! Gêneros atualizados e arquivo salvo.")
