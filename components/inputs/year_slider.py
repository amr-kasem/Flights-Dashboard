from dash import dcc ,html
import dash_bootstrap_components as dbc
import plotly.express as px

def create_slider(id,data):
    year_range = range(min(data['year_i'] ),max(data['year_i'] )+1,1)
    markers = {x*10:str(x*10) for x in year_range}
    slider = dcc.RangeSlider(
        id=id,
        min=min(data['year_i'] )*10,
        max=max(data['year_i'] )*10+6,
        value = [1900, 2010],
        step=1,
        marks=markers,
        tooltip={"placement": "bottom", "always_visible": True}
    )

    hist = px.histogram(data, x="year", height=100,)\
             .update_xaxes(title_text = "",range=[1900,2010],showticklabels=False)\
             .update_yaxes(title_text = "",showticklabels=False).update_traces(marker_color='orange')
    hist.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        'margin': {
            'l': 0,
            'r': 0,
            'b': 0,
            't': 0,
            'pad': 0
        },
        'xaxis_showgrid':False,
        'yaxis_showgrid':False,
        'xaxis': {'fixedrange':True},
        'yaxis': {'fixedrange':True},

    })


    hist_graph = dcc.Graph(id='year_hist',figure=hist,config={'displayModeBar' :False})
    slider_div = html.Div([slider],style={'margin-top':-32})
    return dbc.Col([hist_graph,slider_div])