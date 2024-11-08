import pandas as pd
 
def process_data(df):
    # Verifica se todas as colunas necessárias estão presentes
    expected_columns = ['codigo', 'vendas', 'estoque_atual', 'desconto', 'preco']
    if len(df.columns) != len(expected_columns):
        raise ValueError(f"A planilha deve conter exatamente {len(expected_columns)} colunas: {', '.join(expected_columns)}")
   
    # Renomeia as colunas para facilitar a manipulação
    df.columns = expected_columns
   
    # Verifica se os tipos de dados estão corretos
    try:
        df['vendas'] = df['vendas'].astype(float)
        df['estoque_atual'] = df['estoque_atual'].astype(float)
        df['desconto'] = df['desconto'].astype(float)
        df['preco'] = df['preco'].astype(float)
    except ValueError:
        raise ValueError("As colunas 'vendas', 'estoque_atual', 'desconto' e 'preco' devem conter valores numéricos.")
   
    # Salva o preço original
    df['preco_original'] = df['preco']
   
    # Calcula o estoque inicial (vendas + estoque atual)
    df['estoque_inicial'] = df['estoque_atual'] + df['vendas']
   
    # Calcula o giro (vendas divididas pelo estoque inicial)
    df['giro'] = df.apply(lambda row: max(row['vendas'] / row['estoque_inicial'], 0) if row['estoque_inicial'] > 0 else 0, axis=1)
       
    # Calcula o giro médio dos produtos
    giro_medio = ((df['giro'] * df['estoque_inicial']).sum() / df['estoque_inicial'].sum())
   
    # Calcula o delta entre o giro médio e o giro de cada produto
    df['delta_giro'] = df['giro'] - giro_medio
   
    # Define faixas de desconto em intervalos de 2%
    faixas = pd.interval_range(start=0, end=1, freq=0.02)
    df['faixa_desconto'] = pd.cut(df['desconto'], bins=faixas)
   
    # Agrupa os dados por faixa de desconto para análise
    df_faixas = df.groupby('faixa_desconto').agg({
        'codigo': 'count',            # Contagem de produtos
        'vendas': 'sum',              # Total de vendas
        'estoque_atual': 'sum',       # Estoque atual somado por faixa
        'estoque_inicial': 'sum'      # Estoque inicial somado por faixa
    }).reset_index()
   
    # Renomeia colunas para facilitar a leitura
    df_faixas.columns = ['faixa', 'qtd_produtos', 'vendas', 'estoque_atual', 'estoque_inicial']
   
    # Calcula os indicadores
    desconto_medio = df['desconto'].mean() * 100  # Média de desconto em percentual
    desconto_medio_ponderado = (df['desconto'] * df['estoque_atual']).sum() / df['estoque_atual'].sum() * 100
    giro_medio_percent = giro_medio * 100  # Converter para percentual
   
    return df, df_faixas, desconto_medio, desconto_medio_ponderado, giro_medio_percent