import dash_bootstrap_components as dbc
from dash import html


def create_ban(id_number,id_country):
    dropdown = dbc.Col(
                [
                    html.Div(
                        [
                            html.H5('Country with Max Accidents:'),
                            html.Div(
                                '',
                                id=id_number,
                                className='text'
                                
                            ),
                            html.H5(
                                '',
                                id=id_country,
                                className='subtext'
                            )
                        ],
                        className='ban',  
                    ),
                ], 
                sm=4,
            )

    return dropdown