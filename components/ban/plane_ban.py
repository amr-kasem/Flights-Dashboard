import dash_bootstrap_components as dbc
from dash import html


def create_ban(number,plane_type):
    dropdown = dbc.Col(
                [
                    html.Div(
                        [
                            html.H5('Plane Type with Max Accidents:'),
                            html.Div(
                                number,
                                className='text'
                                
                            ),
                            html.H5(
                                plane_type,
                                className='subtext'
                            )
                        ],
                        className='ban',  
                    ),
                ], 
                sm=4,
            )

    return dropdown