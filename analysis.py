import pandas as pd

dados = pd.read_csv('OK_Anexo_Arquivo_Dados_Projeto.csv', sep=';')

dados.head(10)
type(dados)
dados.shape
dados.columns
dados.info()
dados.isnull().sum()

dados.query('precip < 0').index
registros_a_remover = dados.query('precip < 0').index
dados.drop(registros_a_remover, axis=0, inplace=True)
dados.query('precip < 0')
dados.head(10)
