df.data <- read.csv('data/dados.csv')

df.regression <- lm(profit_norm ~ duration_norm + Action + Adventure + Animation + 
                      Biography + Comedy + Crime + Documentary + Drama + 
                      Family + Fantasy + History + Horror + Music + Musical + 
                      Mystery + Romance + Sci.Fi + Sport + Thriller + 
                      War + Western, data=df.data)

summary(df.regression)

# Resíduos do modelo
res <- residuals(df.regression)

# Quadrados dos erros (resíduos)
squared_errors <- res^2

# Erro Quadrático Médio (EQM)
MSE <- mean(squared_errors)

# Exibir o valor do MSE
print(MSE)
