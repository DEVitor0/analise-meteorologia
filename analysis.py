import pandas as pd

dados = pd.read_csv('./dates.csv', sep=';')

dados.head(10)
type(dados)
dados.shape
dados.columns
dados.info()
dados.isnull().sum()
