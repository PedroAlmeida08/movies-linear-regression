library(tidyverse)

data <- read.csv('data/movie_metadata.csv')

# Pré-processamento

# 1 - Eliminação das colunas que não serão utilizadas (5043 rows x 6 columns)
data <- data %>% 
  dplyr::select(movie_title, gross, budget, genres, title_year, duration)

# 2 - Eliminação de linhas que contenham NA (3890 rows x 6 columns) -- 1153 filmes continham NaN

data <- data %>% drop_na()

# 3 - Criação da coluna 'profit'

data <- data %>% 
  dplyr::mutate(
    profit = gross - budget
  )

# 4 - Removendo filmes que não são longa metragem

data <- data %>% 
  filter(
    duration >= 70
  )

# 5 - Filtro de filmes entre os anos 2000 e 2016 -- 1152 rows x 7 columns

data <- data %>% 
  filter(
    title_year >= 2000 &
    title_year <= 2016
  )

# 6 - Enconding de gênero

data <- data %>%
  separate_rows(genres, sep = "\\|") %>%
  mutate(value = 1) %>% 
  distinct(movie_title, genres, .keep_all = TRUE) %>% 
  pivot_wider(names_from = genres, values_from = value, values_fill = 0) %>% 
  rename(Sci_Fi = 'Sci-Fi')

# 7 - Normalização da coluna de 'profit' e 'duration'

normalize <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

data <- data %>% 
  mutate(
    profit_norm = normalize(profit),
    duration_norm = normalize(duration)
  )


# 8 - Exportando dados
saveRDS(data, file = "data/dados_R.rds")
