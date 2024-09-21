import pandas as pd

# 1. Ler o arquivo CSV original
df = pd.read_csv('tabela_final_com_id.csv')

# 2. Função para limpar e separar os gêneros
def separar_generos(generos):
    if isinstance(generos, str):  # Verifica se é uma string
        return [genero.strip() for genero in generos.split(',')]
    return []  # Retorna lista vazia se não for string

# 3. Aplicar a função para criar uma nova coluna com listas de gêneros
df['generos'] = df['generos'].apply(separar_generos)

# 4. Explodir a coluna de gêneros em várias linhas
generos = df.explode('generos')

# 5. Obter os gêneros únicos
generos_unicos = generos['generos'].drop_duplicates()

# 6. Criar arquivos CSV para cada gênero individual
for genero in generos_unicos:
    # Filtrar os IDs dos filmes que pertencem a esse gênero
    filmes_do_genero = generos[generos['generos'] == genero][['id']]
    
    # Salvar em um arquivo CSV, usando o nome do gênero
    filmes_do_genero.to_csv(f'{genero}.csv', index=False)

print("Arquivos CSV gerados com sucesso para cada gênero individual!")
