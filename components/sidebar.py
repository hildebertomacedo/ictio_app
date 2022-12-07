import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

# ========= Layout ========= #
layout = dbc.Col([
                html.H1("Dashboard Ictio", className="text-primay"),
                html.P("By Ictio", className="text-info"),
                html.Hr(),
#Seção BL --------------------
                dbc.Row([
                    dbc.Col([
                        dbc.Button(id="button1", children="BL1",color = "primary")], width = 3),
                    dbc.Col([
                        dbc.Button(id="button2", children="BL2",color = "primary", className="ms-2")], width = 3),                
                    dbc.Col([
                        dbc.Button(id="button3", children="BL3",color = "primary", className="ms-2")], width = 3),
                    dbc.Col([
                        dbc.Button(id="button4", children="BL4",color = "primary", className="ms-2")], width = 3)]),

#Seção NAV --------------------
                html.Hr(),
                dbc.Nav([
                    dbc.NavLink("Effort", href = "/effort", active = "exact"),
                    dbc.NavLink("Species composition", href = "/species_composition", active = "exact"),
                    dbc.NavLink("Taxa information", href = "/taxa_information", active = "exact")
                ], vertical = True, pills = True, id='nav-buttons', style={'margin-bottom': "50px"})
#Finaliza --------------------
], id = 'sidebar_complete')

# =========  Callbacks  =========== #
# Pop-up receita
