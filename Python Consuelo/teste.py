import pandas as pd
import sqlite3
conn = sqlite3.connect("filmes.db")

df = pd.read_sql_query("SELECT * FROM filmes", conn)

print(df)


conn.close()
