import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dados = pd.read_csv('data/dados.csv', sep=',')

# 1 - Selecionando as variáveis independentes (X) e a variável dependente (y)
x = dados[['duration', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
           'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
           'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
           'Sport', 'Thriller', 'War', 'Western']]
y = dados.profit_norm

# 2 - Dividindo os dados em conjunto de treino e teste
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42)

# 3 - Criando e treinando o modelo de regressão linear
modelo = LinearRegression().fit(x_train, y_train)

# 4 - Fazendo predições com os dados de teste
y_pred = modelo.predict(x_test)

# Calculando o MSE
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse}')

# Calculando o R²
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')
