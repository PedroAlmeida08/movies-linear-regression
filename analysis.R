df.data <- read.csv('data/dados.csv')

df.regression <- lm(profit ~ duration + Action + Adventure + Animation + 
                      Biography + Comedy + Crime + Documentary + Drama + 
                      Family + Fantasy + History + Horror + Music + Musical + 
                      Mystery + Romance + Sci.Fi + Short + Sport + Thriller + 
                      War + Western, data=df.data)

summary(df.regression)
