import pandas as pd

# Leia o arquivo CSV sem duplicatas
df = pd.read_csv('tabela_sem_duplicatas.csv')

# Remova a coluna 'id'
df = df.drop(columns='id')

# Organize os títulos de acordo com as regras especificadas
df['titulo'] = df['titulo'].astype(str)  # Assegure que todos os títulos são strings

# Ordena os títulos, separando números e letras
df_sorted = df.sort_values(
    by='titulo', 
    key=lambda x: x.str.extract('^(\d+)', expand=False).fillna('').astype(str) + 
                  x.str.replace(r'^\d+', '', regex=True),
    ascending=[True]
)

# Salve o DataFrame ordenado em um novo arquivo CSV
df_sorted.to_csv('tabela_ordenada.csv', index=False)
