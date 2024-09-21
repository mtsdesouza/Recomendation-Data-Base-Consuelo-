import pandas as pd
import re

# Carregar o arquivo CSV
df = pd.read_csv('FilmesScraping.csv')

# Função para remover o ano entre parênteses e o espaço antes dele
def remover_ano(titulo):
    return re.sub(r'\s*\(\d{4}\)', '', titulo)

# Aplicar a função à coluna 'Título (Ano)'
df['Título (Ano)'] = df['Título (Ano)'].apply(remover_ano)

# Salvar o arquivo de volta
df.to_csv('FilmesScraping.csv', index=False)

print("Coluna 'Título (Ano)' modificada e arquivo salvo.")
