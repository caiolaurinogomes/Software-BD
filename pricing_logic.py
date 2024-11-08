import pandas as pd
 
def calculate_prices(data, settings):
    """
    Calcula os preços ajustados com base nas configurações fornecidas.
 
    Parâmetros:
    - data (DataFrame): Dados processados da coleção, incluindo informações de giro e desconto.
    - settings (dict): Configurações de precificação, incluindo desconto mínimo, máximo, steps e deslocamento da curva.
 
    Retorna:
    - DataFrame atualizado com uma coluna adicional para o novo preço calculado.
    """
    # Extrai as configurações de precificação
    desconto_min = settings.get('desconto_min', 0) / 100
    desconto_max = settings.get('desconto_max', 100) / 100
    deslocamento_curva = settings.get('deslocamento_curva', 0) / 100
    step_desconto_cima = settings.get('step_desconto_cima', 0.02) / 100
    step_desconto_baixo = settings.get('step_desconto_baixo', 0.02) / 100
    step_giro_cima = settings.get('step_giro_cima', 0.02) / 100
    step_giro_baixo = settings.get('step_giro_baixo', 0.02) / 100
 
    # Aplica a lógica de precificação
    def calcular_desconto(row):
        desconto_atual = row['desconto']
        giro = row['giro']
       
        # Se o giro for igual a 0, aplica o desconto máximo
        if giro == 0:
            return desconto_max
        
        # Ajusta o desconto com base no giro e nas configurações de step
        if giro > 0.5:  # Giro alto, aplica step de desconto para cima
            novo_desconto = desconto_atual + step_desconto_cima + deslocamento_curva
        elif giro < 0.2:  # Giro baixo, aplica step de desconto para baixo
            novo_desconto = desconto_atual - step_desconto_baixo - deslocamento_curva
        else:  # Giro médio, mantém o desconto ou ajusta conforme necessário
            novo_desconto = desconto_atual
 
        # Limita o desconto aos valores mínimo e máximo
        novo_desconto = max(desconto_min, min(desconto_max, novo_desconto))
        return novo_desconto
 
    # Aplica a função de cálculo de desconto em cada linha do DataFrame
    data['novo_desconto'] = data.apply(calcular_desconto, axis=1)
   
    # Calcula o novo preço com base no desconto ajustado
    data['novo_preco'] = data['preco_original'] * (1 - data['novo_desconto'])
   
    return data
