import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_temperatura(media_anual, mes_escolhido):
    """Cria um gráfico da média da temperatura mínima por ano."""
    plt.figure(figsize=(10,5))
    sns.barplot(x=media_anual.index, y=media_anual.values, palette='coolwarm')
    plt.xlabel("Ano")
    plt.ylabel("Média da Temperatura Mínima")
    plt.title(f"Média da Temperatura Mínima para o mês {mes_escolhido}")
    plt.xticks(rotation=45)
    plt.show()
