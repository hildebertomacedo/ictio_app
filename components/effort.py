from dash import html, dcc, ctx
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app
import geopandas as gpd
import json

# =========  Dataframe  =========== #

df_ictio = pd.read_excel("Base de dados.xlsx")
df_date = df_ictio.get(["obs_date_yyyymmdd", "upload_date_yyyymmdd"])
df_date_obs = pd.to_datetime(df_date["obs_date_yyyymmdd"], format = '%Y%m%d')
df_date_upload = pd.to_datetime(df_date["upload_date_yyyymmdd"], format = '%Y%m%d')
df_ictio = df_ictio.drop(['obs_date_yyyymmdd', 'upload_date_yyyymmdd'], axis=1)
df_ictio = pd.concat([df_ictio, df_date_obs, df_date_upload], axis=1)

# =========  Shapefile  =========== #

# BL1 - Use WGS 84 (epsg:4326) as the geographic coordinate system

bl1 = gpd.read_file("BL_All/bl_01.shp")
bl1 = bl1.to_crs(epsg=4326)
bl1["rand"] = np.random.randint(1, 100, len(bl1))

fig_bl1 = go.Figure(go.Choroplethmapbox(geojson=json.loads(bl1.to_json()), 
                                    locations=bl1.index, z=bl1['rand'],
                                    colorscale="Viridis", marker_line_width=.5)
                                    )

fig_bl1.update_layout(mapbox_style="open-street-map",
                        #height = 1000,
                        autosize=True,
                        margin={"r":0,"t":0,"l":0,"b":0},
                        paper_bgcolor="#FFFEFE",
                        plot_bgcolor="#FFFEFE",
                        showlegend = False,
                        mapbox=dict(center=dict(lat=-5.643527317547974, lon=-61.367682135789416),zoom=3),
                        )

#--------------------------------------------------------------------------------------------------------------------------

#BL2 - Use WGS 84 (epsg:4326) as the geographic coordinate system
bl2 = gpd.read_file("BL_All/bl_02.shp")
bl2 = bl2.to_crs(epsg=4326)
bl2["rand"] = np.random.randint(1, 100, len(bl2))
fig_bl2 = go.Figure(go.Choroplethmapbox(geojson=json.loads(bl2.to_json()), 
                                    locations=bl2.index, z=bl2['rand'],
                                    colorscale="Viridis", marker_line_width=.5)
                                    )

fig_bl2.update_layout(mapbox_style="open-street-map",
                        #height = 1000,
                        autosize=True,
                        margin={"r":0,"t":0,"l":0,"b":0},
                        paper_bgcolor="#FFFEFE",
                        plot_bgcolor="#FFFEFE",
                        showlegend = False,
                        mapbox=dict(center=dict(lat=-5.643527317547974, lon=-61.367682135789416),zoom=3),
                        )

#-------------------------------------------------------------------------------------------------------------------------

# BL3 - Use WGS 84 (epsg:4326) as the geographic coordinate system
bl3 = gpd.read_file("BL_All/bl_03.shp")
bl3 = bl3.to_crs(epsg=4326)
bl3["rand"] = np.random.randint(1, 100, len(bl3))
fig_bl3 = go.Figure(go.Choroplethmapbox(geojson=json.loads(bl3.to_json()), 
                                    locations=bl3.index, z=bl3['rand'],
                                    colorscale="Viridis", marker_line_width=.5)
                                    )

fig_bl3.update_layout(mapbox_style="open-street-map",
                        #height = 1000,
                        autosize=True,
                        margin={"r":0,"t":0,"l":0,"b":0},
                        paper_bgcolor="#FFFEFE",
                        plot_bgcolor="#FFFEFE",
                        showlegend = False,
                        mapbox=dict(center=dict(lat=-5.643527317547974, lon=-61.367682135789416),zoom=3),
                        )

#-------------------------------------------------------------------------------------------------------------------------

# BL4 - Use WGS 84 (epsg:4326) as the geographic coordinate system
bl4 = gpd.read_file("BL_All/bl_04.shp")
bl4 = bl4.to_crs(epsg=4326)
bl4["rand"] = np.random.randint(1, 100, len(bl4))
fig_bl4 = go.Figure(go.Choroplethmapbox(geojson=json.loads(bl4.to_json()), 
                                    locations=bl4.index, z=bl4['rand'],
                                    colorscale="Blues", marker_line_width=.5,
                                    hoverinfo = "text",
                                    hovertext = (df_ictio["watershed_name"],df_ictio["watershed_name"])
                                    ))
                                    

fig_bl4.update_layout(mapbox_style="open-street-map",
                        #height = 1000,
                        autosize=True,
                        margin={"r":0,"t":0,"l":0,"b":0},
                        paper_bgcolor="#FFFEFE",
                        plot_bgcolor="#FFFEFE",
                        showlegend = False,
                        mapbox=dict(center=dict(lat=-5.643527317547974, lon=-61.367682135789416),zoom=3),
                        )
#-------------------------------------------------------------------------------------------------------------------------
df_q1 = df_ictio.get(["obs_date_yyyymmdd"])
order_q1 = df_q1.groupby("obs_date_yyyymmdd").count()
ordem_q1 = df_q1.sort_values(by='obs_date_yyyymmdd',ascending=True)
graph_progress = go.Figure(layout={"template": "plotly"})
graph_progress.add_trace(go.Scatter(x = ordem_q1["obs_date_yyyymmdd"]))
graph_progress.update_layout(
    #paper_bgcolor = "#FFFEFE",
    #plot_bgcolor = "#FFFEFE",
    autosize = True,
    title="Progresso do Aplicativo",
    margin = dict(l=2, r=10, t=10, b=0))
#-------------------------------------------------------------------------------------------------------------------------
count_user = df_ictio.copy()
count_user = df_ictio.get(["user_id", "obs_date_yyyymmdd"])
count_user = pd.DataFrame(pd.value_counts(count_user["user_id"]))
date_user = len(count_user)

count_comments = df_ictio.copy()
count_comments = df_ictio.get(["obs_comments", "obs_date_yyyymmdd"])
count_comments = count_comments.dropna(subset=['obs_comments'])
date_comments = len(count_comments)


count_uploads = df_ictio.copy()
count_uploads = df_ictio.get(["user_id", "obs_date_yyyymmdd"])
date_uploads = len(count_uploads)

count_photos = df_ictio.copy()
count_photos = df_ictio.get(["num_photos", "obs_date_yyyymmdd"])
count_photos.replace(0, np.nan, inplace = True)
count_photos = count_photos.dropna()
count_photos = count_photos.groupby("obs_date_yyyymmdd").sum()
date_photos = len(count_photos)

count_species_app = df_ictio.copy()
count_species_app = df_ictio.get(["scientific_name"])
count_species_app = pd.DataFrame(pd.value_counts(count_species_app["scientific_name"]))
date_species_app = len(count_species_app)
#count_species_app

count_species_reg = df_ictio.copy()
count_species_reg = df_ictio.get(["scientific_name"])
count_species_reg = pd.DataFrame(pd.value_counts(count_species_reg["scientific_name"]))
date_species_reg = len(count_species_reg)
#count_species_reg


#-------------------------------------------------------------------------------------------------------------------------

# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Usuários"),
                            html.H3(style={"color":"#adfc92"}, id="Text1"),
                            html.Span("Comentários"),
                            html.H5(id="Subtext_1"),
                            ], #color="light", #outline = True,
                                            style={"margin-top":"10px",
                                            "box-shadow":"0 4px 4px 0 rgba(0,0,0,0.15), 0 4 px 20px 0 rgba(0,0,0.19)",
                                            "color":"#0A0A2A"})
                            ])]),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Span("Envios"),
                            html.H3(style={"color":"#389fd6"}, id="Text2"),
                            html.Span("Fotos enviadas"),
                            html.H5(id="Subtext_2"),
                            ], #color="light", #outline = True,
                                                style={"margin-top":"10px",
                                                "box-shadow":"0 4px 4px 0 rgba(0,0,0,0.15), 0 4 px 20px 0 rgba(0,0,0.19)",
                                                "color":"#0A0A2A"})
                            ])]),
                    dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Span("Espécies no app"),
                                    html.H3(style={"color":"#DF2935"}, id="Text3"),
                                    html.Span("Espécies registradas"),
                                    html.H5(id="Subtext_3"),
                                    ], #color="light", #outline = True,
                                    style={"margin-top":"10px",
                                    "box-shadow":"0 4px 4px 0 rgba(0,0,0,0.15), 0 4 px 20px 0 rgba(0,0,0.19)",
                                    "color":"#0A0A2A"})
                            ])
                        ])
                    ])
                ], style={'margin':'10px'})
            ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Filtrar dados", className="card-title"),
                html.Label("Categoria"),
                html.Div(
                    dcc.Dropdown(
                        id = "dropdown-receita",
                        clearable=False,
                        style={"width":"100%"},
                        persistence=True,
                        persistence_type="session",
                        multi=True)
                    ),
                 html.Legend("Período de Análise", style={"margin-top": "10px"}),
                        dcc.DatePickerRange(
                            month_format='Do MMM, YY',
                            end_date_placeholder_text='Data...',
                            start_date=datetime.today(),
                            end_date=datetime.today() + timedelta(days=31),
                            with_portal=True,
                            updatemode='singledate',
                            id='date-picker-config',
                            style={'z-index': '100'})],
                            style={"height": "100%", "padding": "25px"})
            ],width=4),

            dbc.Col(
                dbc.Card(dcc.Graph(figure = fig_bl4, id='graph1'), style={'height':'100%', 'padding':'10px'}), width=8
            )
        ], style={'margin': '10px'}),
        dbc.Row([
            dbc.Col(dbc.Card(dcc.Graph(figure = graph_progress, id='graph2'), style={'padding': '10px'}), width=6),
            dbc.Col(dbc.Card(dcc.Graph(id='graph3'), style={'padding': '10px'}), width=3),
            dbc.Col(dbc.Card(dcc.Graph(id='graph4'), style={'padding': '10px'}), width=3),
        ])
    ])





# =========  Callbacks  =========== #
#BUTTONS
@app.callback(
    Output("graph1", "figure"),
    Input("button1", "n_clicks"),
    Input("button2", "n_clicks"),
    Input("button3", "n_clicks"),
    Input("button4", "n_clicks"),
    prevent_initial_call=True,
 )
def greet(bl1,bl2,bl3,bl4):
    button_clicked = ctx.triggered_id
    if button_clicked == 'button1':
        return fig_bl1
    elif button_clicked == 'button2':
        return fig_bl2
    elif button_clicked == 'button3':
        return fig_bl3
    elif button_clicked == 'button4':
        return fig_bl4

@app.callback(
    [
        Output("Text1", "children"),
        Output("Subtext_1", "children"),
        Output("Text2", "children"),
        Output("Subtext_2", "children"),
        Output("Text3", "children"),
        Output("Subtext_3", "children"),

    ],
    [Input("date-picker-config", "date")]
)

def display_status (date):
    df_data_on_date = df_ictio["obs_date_yyyymmdd"] == date
    users = "-" if count_user["user_id"].isna().values[0] else f'{int(date_user):,}'.replace(",",".")
    comments = "-" if count_comments["obs_comments"].isna().values[0] else f'{int(date_comments):,}'.replace(",",".")
    uploads = "-" if count_uploads["user_id"].isna().values[0] else f'{int(date_uploads):,}'.replace(",",".")
    photos = "-" if count_photos["num_photos"].isna().values[0] else f'{int(date_photos):,}'.replace(",",".")
    species_app = "-" if count_species_app["scientific_name"].isna().values[0] else f'{int(date_species_app):,}'.replace(",",".")
    species_reg = "-" if count_species_reg["scientific_name"].isna().values[0] else f'{int(date_species_reg):,}'.replace(",",".")

    return (users,
            comments,
            uploads,
            photos,
            species_app,
            species_reg
    )
