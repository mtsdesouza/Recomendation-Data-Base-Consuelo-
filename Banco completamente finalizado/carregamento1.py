import sqlite3
import pandas as pd

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('filmes.db')
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    nota REAL,
    tipo_de_nota TEXT,
    diretor TEXT
)
''')

# Ler o CSV e importar para a tabela
df = pd.read_csv('tabela_final_sem_generos.csv')
df.to_sql('filmes', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.commit()
conn.close()
