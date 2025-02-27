import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('OK_Anexo_Arquivo_Dados_Projeto.csv', sep=';')

# Exibir informações gerais
def exibir_informacoes(df):
    print("\nPrimeiras 10 linhas:")
    print(df.head(10))
    print("\nTipo de dados:")
    print(type(df))
    print("\nDimensões do dataset:", df.shape)
    print("\nColunas disponíveis:")
    print(df.columns)
    print("\nResumo dos dados:")
    print(df.info())
    print("\nValores nulos por coluna:")
    print(df.isnull().sum())

def limpar_dados(df):
    """Corrige valores inconsistentes e converte tipos de dados"""
    df.drop(df[df['precip'] < 0].index, inplace=True)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['ano'] = df['data'].dt.year.astype(int)
    df['mes'] = df['data'].dt.month.astype(int)
    return df

def encontrar_data_mais_chuvosa(df):
    """Retorna a data com maior precipitação"""
    dia_chuvoso = df.loc[df['precip'].idxmax()]
    return dia_chuvoso['data'].strftime('%d-%m-%Y'), dia_chuvoso['precip']

def encontrar_mes_mais_chuvoso(df):
    """Identifica o mês e ano com maior precipitação total"""
    precip_total = df.groupby(['ano', 'mes'])['precip'].sum().reset_index()
    mais_chuvoso = precip_total.loc[precip_total['precip'].idxmax()]
    return mais_chuvoso

def calcular_media_temperatura(df, mes_escolhido):
    """Calcula a média da temperatura mínima entre 2006 e 2016 para o mês escolhido"""
    filtro_dados = df[(df['mes'] == mes_escolhido) & (df['ano'].between(2006, 2016))]
    media_anual = filtro_dados.groupby("ano")["minima"].mean()
    media_total = filtro_dados["minima"].mean()
    return media_anual, media_total

def gerar_grafico_temperatura(media_anual, mes_escolhido):
    """Gera um gráfico de barras para visualizar a temperatura mínima ao longo dos anos"""
    plt.figure(figsize=(10,5))
    sns.barplot(x=media_anual.index, y=media_anual.values, palette='coolwarm')
    plt.xlabel("Ano")
    plt.ylabel("Média da Temperatura Mínima")
    plt.title(f"Média da Temperatura Mínima para o mês {mes_escolhido}")
    plt.xticks(rotation=45)
    plt.show()

def gerar_grafico_precipitacao(df):
    """Gera um gráfico da precipitação média mensal ao longo dos anos"""
    plt.figure(figsize=(12,6))
    media_mensal = df.groupby(['ano', 'mes'])['precip'].mean().unstack()
    media_mensal.T.plot(kind='line', colormap='viridis', figsize=(12,6))
    plt.title("Precipitação Média Mensal por Ano")
    plt.xlabel("Mês")
    plt.ylabel("Precipitação Média")
    plt.legend(title='Ano', bbox_to_anchor=(1,1))
    plt.grid()
    plt.show()

# Execução do código
exibir_informacoes(df)
df = limpar_dados(df)
dia_chuvoso, maior_precipitacao = encontrar_data_mais_chuvosa(df)
mais_chuvoso = encontrar_mes_mais_chuvoso(df)
print(f"Data mais chuvosa: {dia_chuvoso} com {maior_precipitacao} mm de precipitação")
print(f"Ano/Mês mais chuvoso: {int(mais_chuvoso['ano'])}-{int(mais_chuvoso['mes'])} com {mais_chuvoso['precip']} mm")

# Solicita o mês ao usuário
mes_escolhido = int(input("Digite o número do mês (1-12): "))
media_anual, media_total = calcular_media_temperatura(df, mes_escolhido)
print(f"Média geral da temperatura mínima para o mês {mes_escolhido}: {media_total:.2f}°C")
gerar_grafico_temperatura(media_anual, mes_escolhido)
gerar_grafico_precipitacao(df)
