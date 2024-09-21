import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('filmes.db')

# Criar a consulta SQL
query = '''
SELECT f.*
FROM filmes f
INNER JOIN "Ação" a ON f.id = a.id
INNER JOIN "Animação" an ON f.id = an.id
'''

# Executar a consulta e ler os resultados em um DataFrame
df_filmes = pd.read_sql_query(query, conn)

# Imprimir os resultados
print(df_filmes)

# Fechar a conexão
conn.close()
