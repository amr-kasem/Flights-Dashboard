import dash_bootstrap_components as dbc
from dash import html


def create_ban(id_number,id_year):
    dropdown = dbc.Col(
                [
                    html.Div(
                        [
                            html.H5('Year with Max Accidents:'),
                            html.Div(
                                '',
                                id=id_number,
                                className='text'
                                
                            ),
                            html.H5(
                                '',
                                id=id_year,
                                className='subtext'
                            )
                        ],
                        className='ban',  
                    ),
                ], 
                sm=4,
            )

    return dropdown