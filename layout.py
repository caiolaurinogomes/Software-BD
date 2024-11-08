from dash import dcc, html

def create_layout():
    return html.Div([
        # Cabeçalho
        html.Div(
            html.H2("Ferramenta de Precificação OFF", style={'color': 'white', 'text-align': 'center'}),
            style={'background-color': '#000', 'padding': '10px'}
        ),

        # Botões de upload e exportação
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Button("Carregar Planilha", style={'margin-right': '10px'}),
                style={'display': 'inline-block'}
            ),
            html.Button("Exportar Planilha", id="export-button", n_clicks=0, style={'display': 'inline-block'}),
            dcc.Download(id="download-dataframe-xlsx")
        ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '20px'}),

        # Mensagem de erro
        html.Div(id='error-message', style={'color': 'red', 'text-align': 'center', 'margin-top': '10px'}),

        # Configurações de Precificação
        html.Div([
            html.H4("Configurações de Precificação"),

            # Desconto Mínimo e Máximo
            html.Div([
                html.Label("Desconto Mínimo (%):"),
                dcc.Input(id='desconto-minimo', type='number', placeholder="Digite o desconto mínimo", min=0, max=100),
                html.Label("Desconto Máximo (%):"),
                dcc.Input(id='desconto-maximo', type='number', placeholder="Digite o desconto máximo", min=0, max=100)
            ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-top': '10px'}),

            # Deslocamento da Curva em porcentagem
            html.Div([
                html.Label("Deslocamento da Curva (%):"),
                dcc.Input(id='deslocamento-curva', type='number', placeholder="Digite o deslocamento da curva (%)", value=0)
            ], style={'margin-top': '10px'}),

            # Step Desconto e Giro
            html.Div([
                html.Div([
                    html.Label("Step Desconto p/ Cima (%):"),
                    dcc.Input(id='step-desconto-cima', type='number', value=2.0, step=0.1),
                    html.Button('+', id='increment-desconto-cima', n_clicks=0),
                    html.Button('-', id='decrement-desconto-cima', n_clicks=0),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px'}),

                html.Div([
                    html.Label("Step Desconto p/ Baixo (%):"),
                    dcc.Input(id='step-desconto-baixo', type='number', value=2.0, step=0.1),
                    html.Button('+', id='increment-desconto-baixo', n_clicks=0),
                    html.Button('-', id='decrement-desconto-baixo', n_clicks=0),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px'}),

                html.Div([
                    html.Label("Step Giro p/ Cima (%):"),
                    dcc.Input(id='step-giro-cima', type='number', value=2.0, step=0.1),
                    html.Button('+', id='increment-giro-cima', n_clicks=0),
                    html.Button('-', id='decrement-giro-cima', n_clicks=0),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px'}),

                html.Div([
                    html.Label("Step Giro p/ Baixo (%):"),
                    dcc.Input(id='step-giro-baixo', type='number', value=2.0, step=0.1),
                    html.Button('+', id='increment-giro-baixo', n_clicks=0),
                    html.Button('-', id='decrement-giro-baixo', n_clicks=0),
                ], style={'display': 'flex', 'align-items': 'center', 'margin-top': '10px'}),
            ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}),

            # Exibe as configurações armazenadas para verificação
            html.Div(id="pricing-settings-display", style={'margin-top': '20px', 'color': 'blue'})

        ], style={'width': '30%', 'padding': '20px', 'border': '1px solid #e1e1e1', 'border-radius': '5px', 'margin-right': '20px'}),

        # Área principal (Gráficos e Indicadores)
        html.Div([
            # Seção de gráficos
            html.Div([
                html.H4("Análise de Desempenho do Período Anterior"),
                html.Div(id='output-graphs', children=[
                    dcc.Graph(id='oferta-graph'),
                    dcc.Graph(id='giro-graph')
                ])
            ], style={'width': '65%', 'padding': '20px', 'border': '1px solid #e1e1e1', 'border-radius': '5px', 'margin-right': '20px'}),
           
            # Seção de indicadores
            html.Div([
                html.H4("Indicadores Calculados", style={'text-align': 'center', 'margin-bottom': '10px'}),
                html.Div("Desconto Médio Vendidos:", id='desconto-medio', style={'font-size': '18px', 'margin': '10px', 'border': '1px solid #e1e1e1', 'border-radius': '5px', 'padding': '10px'}),
                html.Div("Desconto Médio Estoque:", id='desconto-medio-ponderado', style={'font-size': '18px', 'margin': '10px', 'border': '1px solid #e1e1e1', 'border-radius': '5px', 'padding': '10px'}),
                html.Div("Giro Médio Vendidos:", id='giro-medio', style={'font-size': '18px', 'margin': '10px', 'border': '1px solid #e1e1e1', 'border-radius': '5px', 'padding': '10px'})
            ], style={'width': '30%', 'padding': '20px'})
        ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center', 'align-items': 'flex-start', 'margin-top': '20px'}),

        # Div oculto para acionar o callback de atualização da tabela
        html.Div(id='hidden-div', style={'display': 'none'})
    ])
