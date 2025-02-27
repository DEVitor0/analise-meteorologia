from src.data_loader import load_data
from src.analysis import encontrar_data_mais_chuvosa, encontrar_mes_mais_chuvoso
from src.visualization import gerar_grafico_temperatura

FILE_PATH = "../data/dates.csv"

def main():
    df = load_data(FILE_PATH)

    dia_chuvoso, maior_precipitacao = encontrar_data_mais_chuvosa(df)
    print(f"Data mais chuvosa: {dia_chuvoso} com {maior_precipitacao} mm de precipitação")

    mais_chuvoso = encontrar_mes_mais_chuvoso(df)
    print(f"Ano/Mês mais chuvoso: {int(mais_chuvoso['ano'])}-{int(mais_chuvoso['mes'])} com {mais_chuvoso['precip']} mm")

    mes_escolhido = int(input("Digite o número do mês (1-12): "))
    media_anual = df[(df['mes'] == mes_escolhido)].groupby("ano")["minima"].mean()
    gerar_grafico_temperatura(media_anual, mes_escolhido)

if __name__ == "__main__":
    main()
