import pandas as pd

# Leia o arquivo CSV combinado
df = pd.read_csv('tabela_combinada.csv')

# Adicione a coluna de chave primária (numerada)
df.insert(0, 'id', range(1, len(df) + 1))

# Reorganize as colunas (caso necessário)
# df = df[['id', 'titulo'] + [col for col in df.columns if col not in ['id', 'titulo']]]

# Salve o resultado em um novo CSV, se necessário
df.to_csv('tabela_combinada_com_id.csv', index=False)
