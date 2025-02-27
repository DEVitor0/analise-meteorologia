import pandas as pd

def load_data(filepath):
    """Carrega e limpa os dados do arquivo CSV."""
    df = pd.read_csv(filepath, sep=';')
    df.drop(df[df['precip'] < 0].index, inplace=True)  # Remove valores negativos
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['ano'] = df['data'].dt.year.astype(int)
    df['mes'] = df['data'].dt.month.astype(int)
    return df
