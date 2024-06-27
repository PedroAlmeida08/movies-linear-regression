import pandas as pd

dados = pd.read_csv('data/movie_metadata.csv', sep=',')

# Pré-processamento

# 1 - Eliminação das colunas que não serão utilizadas (5043 rows x 6 columns)

dados = dados[['movie_title', 'gross', 'budget',
               'genres', 'title_year', 'duration']]

# 2 - Eliminação de linhas que contenham NA (3890 rows x 6 columns) -- 1153 filmes continham NaN

dados = dados.dropna(axis=0, how='any')

# 3 - Criação da coluna 'profit'

profit = dados['gross'] - dados['budget']
dados['profit'] = profit

# 4 - Removendo filmes que não são longa metragem (7 filmes removidos)

dados = dados[(dados['duration'] >= 70)]

# 5 - Filtro de filmes entre os anos 2000 e 2016 -- 1152 rows x 7 columns

dados = dados[(dados['title_year'] >= 2000) &
              (dados['title_year'] <= 2016)]

# 6 - Não é necessário tratar valores iguais a zero pois o dataframe não possui colunas com valores iguais a zero

has_zero = (dados == 0).any().any()
# print("O DataFrame contém zeros:", has_zero)

# 7 - Expandindo a coluna de gêneros

'''
Para realizar o encoding de gêneros de forma que cada gênero em genres seja considerado individualmente,
você pode usar a técnica chamada one-hot encoding. No contexto do dataframe fornecido, isso significa criar
colunas binárias para cada gênero possível, onde 1 indica a presença do gênero em um filme e 0 indica a ausência.

Veja como você pode fazer isso usando pandas:

1 - Expandir os gêneros: Dividir a coluna genres em múltiplos gêneros para cada filme.

2 - Obter todos os gêneros únicos: Identificar todos os gêneros que aparecem em todos os filmes.

3 - Criar as colunas binárias: Criar novas colunas no dataframe para cada gênero único, preenchendo com 1 ou 0
conforme a presença do gênero em cada filme.

str.get_dummies(sep='|') é usada para expandir os gêneros em colunas binárias.
A função divide os gêneros com base no separador | e cria uma coluna binária para cada gênero

'''

dummies = dados['genres'].str.get_dummies(sep='|')  # 21 gêneros diferentes
dados = pd.concat([dados, dummies], axis=1)

# 7.1 - Criação de uma lista com os gêneros dos filmes
genres = dados.columns[7:].tolist()
genres = ','.join(genres)

# with open('data/genres.txt', 'w') as file:
#     file.write(genres)

# 8 - Normalização da coluna de 'profit' e 'duration'
dados['profit_norm'] = (dados['profit']-dados['profit'].min()) / \
    (dados['profit'].max() - dados['profit'].min())

dados['duration_norm'] = (dados['duration']-dados['duration'].min()) / \
    (dados['duration'].max() - dados['duration'].min())

# 8 - Exportação do dado tratado

dados.to_csv('data/dados.csv', index=False, sep=',')
