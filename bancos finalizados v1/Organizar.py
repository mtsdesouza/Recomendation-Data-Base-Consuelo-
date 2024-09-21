import pandas as pd

# Carregue seus arquivos CSV em DataFrames
df1 = pd.read_csv('filmesScrapingAtualizado.csv')
df2 = pd.read_csv('filmes_tmdb.csv')
df3 = pd.read_csv('filmesScrapingAtualizado.csv')

# Função para adicionar a coluna "metodo Avaliacao" e colocá-la ao lado de "rating"
def adicionar_coluna_metodo(df, metodo):
    # Crie a nova coluna
    df['metodo Avaliacao'] = metodo
    
    # Identifique o índice da coluna "rating"
    rating_index = df.columns.get_loc('rating')
    
    # Reorganize as colunas para que "metodo Avaliacao" fique logo após "rating"
    cols = df.columns.tolist()
    new_order = cols[:rating_index + 1] + ['metodo Avaliacao'] + cols[rating_index + 1:-1]
    return df[new_order]

# Adicione o método de avaliação aos DataFrames
df1 = adicionar_coluna_metodo(df1, '0 a 5')
df2 = adicionar_coluna_metodo(df2, '0 a 10')
df3 = adicionar_coluna_metodo(df3, '0 a 10')  # Supondo que o terceiro CSV também use o método "0 a 5"

# Agora você pode salvar novamente os DataFrames ou continuar manipulando-os
df1.to_csv('Scraping_modificado.csv', index=False)
df2.to_csv('tmdb_modificado.csv', index=False)
df3.to_csv('processado_modificado.csv', index=False)
