import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

dados = pd.read_csv('data/dados.csv', sep=',')

'''
Para predizer a duração ideal de um filme baseado no profit, separados por genres, usando regressão linear, 
você pode seguir os passos abaixo:

Preparação dos Dados: Primeiro, você precisa preparar os dados de forma que cada filme esteja representado por uma linha, 
onde cada gênero único é uma variável preditora (feature).

Escolha do Modelo: Utilize regressão linear múltipla para prever a duração do filme (duration) com base no lucro (profit) e 
nos gêneros como variáveis preditoras.

Codificação dos Gêneros: Como você fez o encoding dos gêneros usando one-hot encoding, essas colunas binárias de gêneros
 serão suas variáveis independentes na regressão.

Divisão dos Dados: Divida os dados em conjunto de treino e conjunto de teste para avaliação do modelo.

Treinamento do Modelo: Aplique a regressão linear sobre os dados de treino.

Avaliação do Modelo: Avalie o desempenho do modelo usando métricas como o erro quadrático médio sobre os dados de teste.
'''

# 1 - Selecionando as variáveis independentes (X) e a variável dependente (y)
x = dados.profit
y = dados.duration

# 2 - Dividindo os dados em conjunto de treino e teste
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42)

# 3 - Criando e treinando o modelo de regressão linear
modelo = LinearRegression().fit(x_train.values.reshape(-1, 1), y_train)

# 4 - Fazendo predições com os dados de teste
y_pred = modelo.predict(x_test.values.reshape(-1, 1))

# 5 - Calculando o Erro Quadrático Médio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(mse)

# # 6 - Gerando o gráfico
# fig, ax = plt.subplots()
# ax.scatter(y_pred, y_test)
# plt.show()
