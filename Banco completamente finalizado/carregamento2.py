import sqlite3
import pandas as pd
import os

# Conectar ao banco de dados
conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()

# Lista dos arquivos CSV (sem caminho)
arquivos_generos = [
    "Ação.csv", "Animação.csv", "Aventura.csv", "Cinema TV.csv", "Comédia.csv",
    "Crime.csv", "Desconhecido.csv", "Documentário.csv", "Drama.csv",
    "Família.csv", "Fantasia.csv", "Faroeste.csv", "Ficção científica.csv",
    "Guerra.csv", "História.csv", "Mistério.csv", "Música.csv", "nan.csv",
    "Romance.csv", "Terror.csv", "Thriller.csv"
]

# Criar tabelas e importar dados
for arquivo in arquivos_generos:
    genero = arquivo.replace('.csv', '').replace(' ', '_')  # Substitui espaços por underscores
    # Criar a tabela para cada gênero
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS "{genero}" (
        id INTEGER,
        FOREIGN KEY(id) REFERENCES filmes(id)
    )
    ''')
    
    # Ler o CSV e importar para a tabela
    df = pd.read_csv(arquivo)
    df.to_sql(genero, conn, if_exists='replace', index=False)

# Fechar a conexão
conn.commit()
conn.close()
