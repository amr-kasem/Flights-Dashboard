import dash
from dash import dcc,html
from dash.html.Br import Br
import dash_bootstrap_components as dbc

text = "made by Eng. Ahmed Elbatawy & Eng. Amr Kasem"
footer = dbc.Row(
    children=[
        html.Br(),
        dbc.Col([
            html.P(children=text,className='text-center')
        ],sm=12)
    ],
    # className='fixed-bottom',
)