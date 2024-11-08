import os
from flask import Flask, render_template
from dash import Dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks

# Configuração do aplicativo Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Inicializa o aplicativo Dash
dash_app = Dash(__name__, server=app, url_base_pathname='/dashboard/', external_stylesheets=[dbc.themes.BOOTSTRAP])

# Configura o layout do aplicativo Dash
dash_app.layout = create_layout()

# Registra os callbacks
register_callbacks(dash_app)

# Rota principal do Flask para a página inicial
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o arquivo index.html

if __name__ == '__main__':
    app.run(debug=True, port=5001)
