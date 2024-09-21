import pandas as pd

# Leia o arquivo CSV ordenado
df_sorted = pd.read_csv('tabela_ordenada.csv')

# Adicione a coluna de chave primária (numerada) antes da coluna 'titulo'
df_sorted.insert(0, 'id', range(1, len(df_sorted) + 1))

# Salve o DataFrame atualizado em um novo arquivo CSV
df_sorted.to_csv('tabela_final_com_id.csv', index=False)
