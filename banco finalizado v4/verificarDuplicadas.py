import pandas as pd

# Leia o arquivo CSV combinado
df = pd.read_csv('tabela_combinada_com_id.csv')

# Verifique duplicatas na coluna 'titulo'
duplicatas = df[df['titulo'].duplicated(keep=False)]

# Exiba as duplicatas
print(duplicatas)

# (Opcional) Salve as duplicatas em um novo arquivo CSV
duplicatas.to_csv('duplicatas_titulos.csv', index=False)
