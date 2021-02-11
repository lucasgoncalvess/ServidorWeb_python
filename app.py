#bibliotecas necessarias
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import math
import requests
from assets.textos import referencia_text, cabecalho_text, introducao_text, passabaixa1_text, passabaixa2_text, passabaixa3_text,\
    passaalta1_text, passaalta2_text, passafaixa1_text, passafaixa2_text, rejeitafaixa1_text, rejeitafaixa2_text, aplicacao_text

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    #texto do cabeçalho
    html.Div([
        dcc.Markdown(children=cabecalho_text)
    ], className="cabecalho"),
    #introdução
    html.Div([
        html.H1("Filtros Passivos", style={'textAlign': 'center', 'color': '#940319'} ),
            dcc.Markdown(introducao_text),
    ], className="introducao"),
    #Filtros passa-baixa
    html.Div([
        html.H3("Filtros Passa-Baixa", style={'textAlign': 'center', 'color': '#de0224'} ),
            dcc.Markdown(passabaixa1_text),
        html.Img(src="assets/circ_passabaixa.png"),
            dcc.Markdown(passabaixa2_text),
        html.Img(src="assets/fig2_passabaixa.png"),
            dcc.Markdown(passabaixa3_text),
        html.Img(src="assets/eqq_fc_passabaixa.png"),
    ],className="passa_baixa"),
    #Filtros Passa-Alta
    html.Div([
        html.H3("Filtros Passa-Alta", style={'textAlign': 'center', 'color': '#de0224'} ),
            dcc.Markdown(passaalta1_text),
        html.Img(src="assets/cir_passaalta.png"),
            dcc.Markdown(passaalta2_text),
        html.Img(src="assets/resp_passaalta.png"),
            dcc.Markdown(passabaixa3_text),
        html.Img(src="assets/eqq_fc_passaalta.png"),
    ], className="passa_alta"),
    #Filtros Passa-Faixa
    html.Div([
        html.H3("Filtros Passa-Faixa", style={'textAlign': 'center', 'color': '#de0224'} ),
            dcc.Markdown(passafaixa1_text),
        html.Img(src="assets/circ_passafaixarlc.png"),
            dcc.Markdown(passafaixa2_text),
        html.Img(src="assets/resp_passafaixarlc.png"),
    ], className="passa_faixa"),
    #Filtros Rejeita-Faixa
    html.Div([
        html.H3("Filtros Rejeita-Faixa", style={'textAlign': 'center', 'color': '#de0224'} ),
            dcc.Markdown(rejeitafaixa1_text),
        html.Img(src="assets/circ_rejeitafaixa.png"),
            dcc.Markdown(rejeitafaixa2_text),
        html.Img(src="assets/resp_rejeitafaixa.png"),
    ],className="rejeita_faixa"),
    #Aplicação
    html.Div([
        html.H3("Aplicação de um Filtro Passa-Baixa", style={'textAlign': 'center', 'color': '#de0224'} ),
        html.Img(src="assets/circ_passabaixa.png"),
        html.Br(),
        dcc.Markdown(aplicacao_text),

            dcc.Input(id="resistencia", type="number", placeholder="Resistência", value=''), #entrada do valor da resistencia
            dcc.Input(id="capacitancia", type="number", placeholder="Capacitância", value=''), #entrada do valor da capacitância
            dcc.Input(id="frequencia", type="number", placeholder="Frequência", value=''), #entrada do valor da frequência
            dcc.Input(id="tensaoin", type="number", placeholder="Tensão de Entrada", value=''), #entrada do valor da tensão de entrada
        html.Div(id="number-out"),
    ], className="aplicacao"),
    #Referencia
        html.Div([
            dcc.Markdown(referencia_text),
    ], className="referencia"),
])

@app.callback(
    Output("number-out", "children"),
    [Input("resistencia", "value"), Input("capacitancia", "value"), Input("frequencia", "value"), Input("tensaoin", "value")],
)
def number_render(resistencia, capacitancia, frequencia, tensaoin):
    if resistencia >= 0:
        freqcorte = (1 / (resistencia * capacitancia * 2 * 3.14))  #frequencia de corte
        impcapacitiva = (1 / (2 * 3.14 * frequencia * capacitancia))  #impedancia capacitiva
        vout = (tensaoin / (math.sqrt(((resistencia / impcapacitiva) * (resistencia / impcapacitiva)) + 1)))  #tensão de saida
    else:
        return ("Insira Valores Válidos")
    #saida dos valores
    return "||Frequência de Corte(Hz): {} ||Impedância Capacitiva(Ohms): {} ||Tensão de Saída(Volts): {} ||".format(freqcorte, impcapacitiva, vout),


if __name__ == '__main__':
    app.run_server(debug=True)