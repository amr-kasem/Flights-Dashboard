import dash
from dash import html

import dash_bootstrap_components as dbc
import pandas as pd 
from components.layout.footer import footer
from components.layout.header import title
from components.inputs.ismil_dropdown import create_dropdown as create_ismil_dropdown
from components.inputs.year_slider import create_slider as create_year_slider
from components.graphs.accident_map import plot_graph as accident_map_plot
from components.graphs.accident_over_time import plot_graph as accident_time_plot
from components.graphs.accident_over_types import plot_graph as accident_type_plot
from components.controllers.map_hist_controller import activate as activate_map_hist_controller
from components.ban.year_ban import create_ban as create_year_ban
from components.ban.country_ban import create_ban as create_country_ban
from components.ban.plane_ban import create_ban as create_plane_ban
df = pd.read_csv('./data/full_data.csv',parse_dates=['Date'])
df['isMil'] = df.Operator.str.contains('MILITARY', case=False)
df.isMil.fillna(False,inplace=True)
df['year'] = df.Date.dt.year
df['year_i'] = (df.year / 10).astype(int)
df.loc[:,'selected'] = True
plane_agg = df.Type.value_counts()
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY,'./assets/style.css'])
app.layout = dbc.Container(
    [
        title,
        html.Hr(),
        dbc.Row(
            [
                create_year_ban('year_number','year_name'),
                create_country_ban('country_number','country_name'),
                create_plane_ban(plane_agg.iloc[0],plane_agg.index[0]),
            ],
            className=['padded_container']
        ),
        dbc.Row(
            [
                dbc.Col(create_year_slider('year_slider',df),md=8),
                dbc.Col([
                    dbc.Label('Operator Type: ',style={'padding-top':'10px'}),
                    create_ismil_dropdown('ismil_dropdown')
                ],md=4),
            
            ],
            className=['padded_container']
        ),
        dbc.Row(
            [
                dbc.Col(accident_map_plot(df), md=6,lg=8),
                dbc.Col(accident_time_plot(df), md=6,lg=4),
            ],
            className=['padded_container']
        ),
        dbc.Row(
            [
                dbc.Col(accident_type_plot(df))
            ],
            className=['padded_container']
        ),
        footer
    ],
    fluid=True,
)


if __name__ == '__main__':
    activate_map_hist_controller(app,df)
    app.run_server(debug=True)