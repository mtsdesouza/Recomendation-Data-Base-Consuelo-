import pandas as pd

# Leia os arquivos CSV
df1 = pd.read_csv('processado_modificado.csv')
df2 = pd.read_csv('Scraping_modificado.csv')
df3 = pd.read_csv('tmdb_modificado.csv')

# Combine as tabelas
df_combined = pd.concat([df1, df2, df3], ignore_index=True)

# Salve o resultado em um novo CSV, se necessário
df_combined.to_csv('tabela_combinada.csv', index=False)
