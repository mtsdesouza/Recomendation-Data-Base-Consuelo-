import pandas as pd
import sqlite3
caminho = "filmes.db"

conn = sqlite3.connect(caminho)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tabelas = cursor.fetchall()
df = pd.read_sql_query("SELECT * FROM filmes", conn)
print(tabelas)
conn.close()

print(df)