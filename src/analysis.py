def encontrar_data_mais_chuvosa(df):
    """Retorna a data com maior precipitação registrada."""
    dia_chuvoso = df.loc[df['precip'].idxmax()]
    return dia_chuvoso['data'].strftime('%d-%m-%Y'), dia_chuvoso['precip']

def encontrar_mes_mais_chuvoso(df):
    """Identifica o mês com maior precipitação total."""
    precip_total = df.groupby(['ano', 'mes'])['precip'].sum().reset_index()
    return precip_total.loc[precip_total['precip'].idxmax()]
