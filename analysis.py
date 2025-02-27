import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
dados = pd.read_csv('OK_Anexo_Arquivo_Dados_Projeto.csv', sep=';')

dados.head(10)
type(dados)
dados.shape
dados.columns
dados.info()
dados.isnull().sum()

# Correção de preciptações negativas
dados.query('precip < 0').index
registros_a_remover = dados.query('precip < 0').index
dados.drop(registros_a_remover, axis=0, inplace=True)
dados.query('precip < 0')
dados.head(10)

# Definir colunas de data
dados['data'] = pd.to_datetime(dados['data'], format='%d/%m/%Y')
dados['ano'] = dados['data'].dt.year.astype(int)
dados['mes'] = dados['data'].dt.month.astype(int)

# Encontrar data mais chuvosa
def encontrar_data_mais_chuvosa(dados):
    data_chuvosa = {}
    for _, row in dados.iterrows():
        mes_ano = row['data'].strftime('%d-%m-%Y')
        precipitacao = row['precip']
        data_chuvosa[mes_ano] = precipitacao
    
    dia_chuvoso = max(data_chuvosa, key=data_chuvosa.get)
    maior_precipitacao = data_chuvosa[dia_chuvoso]
    return dia_chuvoso, maior_precipitacao

dia_chuvoso, maior_precipitacao = encontrar_data_mais_chuvosa(dados)
print("Data mais chuvosa:", dia_chuvoso)
print("A preciptação nesse dia foi de:", maior_precipitacao)

# Encontrar ano/mês mais chuvoso
precip_total = dados.groupby(['ano', 'mes'])['precip'].sum().reset_index()
mais_chuvoso = precip_total.loc[precip_total['precip'].idxmax()]
print("O ano/mês com a maior precipitação é:")
print("Ano:", int(mais_chuvoso['ano']))
print("Mês:", int(mais_chuvoso['mes']))
print("A precipitação total nesse ano/mês foi de:", mais_chuvoso['precip'])