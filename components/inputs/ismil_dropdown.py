import dash_bootstrap_components as dbc
from dash import html


def create_dropdown(id):
    dropdown =dbc.Select(
                id=id,
                options=[
                    {'label': 'Military', 'value': 'Military'},
                    {'label': 'Non-Militray', 'value': 'Non-Militray'},
                    {'label': 'All', 'value': 'All'},
                ],
                value='All',
            ),

    return html.Div(dropdown)