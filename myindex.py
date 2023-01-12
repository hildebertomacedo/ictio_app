from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, effort, species_composition, taxa_information




# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ],md = 2, style={'backgroud-color': 'red', 'height':'1080px'}),
        dbc.Col([
            content
        ],md = 10, style={'backgroud-color': 'blue', 'height':'1080px'}),
    ])
], fluid=True,)
@app.callback(Output('page-content', 'children'), [Input ('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/effort':
        return effort.layout

    if pathname == '/species_composition':
        return species_composition.layout

    if pathname == '/taxa_information':
        return taxa_information.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
