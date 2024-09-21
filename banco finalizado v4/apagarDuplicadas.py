import pandas as pd

# Leia o arquivo CSV combinado
df = pd.read_csv('tabela_combinada_com_id.csv')

# Remova duplicatas na coluna 'titulo', mantendo a primeira ocorrência
df_sem_duplicatas = df.drop_duplicates(subset='titulo', keep='first')

# (Opcional) Se você quiser manter a última ocorrência, use:
# df_sem_duplicatas = df.drop_duplicates(subset='titulo', keep='last')

# Salve o DataFrame sem duplicatas em um novo arquivo CSV
df_sem_duplicatas.to_csv('tabela_sem_duplicatas.csv', index=False)
