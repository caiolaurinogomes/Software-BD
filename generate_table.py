import pandas as pd

def generate_pricing_table(step_giro_up, step_giro_down, step_discount_up, step_discount_down, curve_shift):
    """
    Função para gerar a tabela de precificação com as colunas:
    - Delta Giro (p.p)
    - Desconto Adicional
    - Desconto Adicional Calibrado

    Parâmetros:
    - step_giro_up: Step de giro para cima (incremento positivo)
    - step_giro_down: Step de giro para baixo (incremento positivo)
    - step_discount_up: Step de desconto para cima (incremento positivo)
    - step_discount_down: Step de desconto para baixo (incremento positivo)
    - curve_shift: Deslocamento da curva para ajustar o desconto adicional calibrado

    Retorna:
    - DataFrame com a tabela de precificação
    """

    # Cria uma lista para armazenar os valores das colunas
    data = {
        'Delta Giro (p.p)': [],
        'Desconto Adicional': [],
        'Desconto Adicional Calibrado': []
    }

    # Gera 50 valores para cima e para baixo do ponto 0
    for i in range(-50, 51):  # De -50 a 50, totalizando 101 linhas, com o 0 no meio
        if i == 0:
            delta_giro = 0
            delta_discount = 0
        elif i > 0:
            # Acima de 0
            delta_giro = -i * step_giro_down  # Subtrai o step giro para baixo
            delta_discount = i * step_discount_up  # Soma o step desconto para cima
        else:  # i < 0
            # Abaixo de 0
            delta_giro = -i * step_giro_up  # Soma o step giro para cima (i é negativo, -i é positivo)
            delta_discount = i * step_discount_down  # Subtrai o step desconto para baixo (i é negativo)

        # Adiciona os valores às listas
        data['Delta Giro (p.p)'].append(round(delta_giro, 1))
        data['Desconto Adicional'].append(round(delta_discount, 1))

        # Calcula o Desconto Adicional Calibrado somando o deslocamento da curva
        calibrated_discount = delta_discount + curve_shift
        data['Desconto Adicional Calibrado'].append(round(calibrated_discount, 1))

    # Converte o dicionário em um DataFrame do Pandas
    df_pricing_table = pd.DataFrame(data)

    return df_pricing_table

