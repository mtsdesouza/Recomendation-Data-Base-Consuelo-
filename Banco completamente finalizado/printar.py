import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('filmes.db')

# Criar um cursor
cursor = conn.cursor()

# Obter a lista de tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Imprimir o conteúdo de cada tabela
for tabela in tabelas:
    tabela_nome = tabela[0]
    print(f"Conteúdo da tabela: {tabela_nome}")
    
    # Ler a tabela em um DataFrame e imprimir
    df = pd.read_sql_query(f"SELECT * FROM '{tabela_nome}'", conn)
    print(df)
    print("\n")  # Adiciona uma linha em branco entre as tabelas

# Fechar a conexão
conn.close()
