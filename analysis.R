data <- readRDS('data/dados_R.rds')

modelo <- lm(profit_norm ~ duration_norm + Action + Adventure + Animation + 
             Biography + Comedy + Crime + Documentary + Drama + 
             Family + Fantasy + History + Horror + Music + Musical + 
             Mystery + Romance + Sci_Fi + Sport + Thriller + 
             War + Western, data=data)

summary(modelo)

# Resíduos do modelo
res <- residuals(modelo)

# Quadrados dos erros (resíduos)
squared_errors <- res^2

# Erro Quadrático Médio (EQM)
MSE <- mean(squared_errors)

# Exibir o valor do MSE
print(MSE)
