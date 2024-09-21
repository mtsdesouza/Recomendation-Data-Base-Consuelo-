import pandas as pd

# 1. Ler o arquivo CSV original
df = pd.read_csv('tabela_final_com_id.csv')

# 2. Remover a coluna 'generos'
df_sem_generos = df.drop(columns=['generos'])

# 3. Salvar a nova tabela em um novo arquivo CSV
df_sem_generos.to_csv('tabela_final_sem_generos.csv', index=False)

print("Nova tabela criada com sucesso, sem a coluna 'generos'!")
