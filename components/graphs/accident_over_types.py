import dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import pandas as pd 
import plotly.express as px

def plot_graph(data):
    data.Type = data.Type.astype('category')
    title = 'Accidents over Types'
    hist = pd.DataFrame(data.Type.value_counts())
    hist['Count'] = hist.Type.copy()
    hist['Type'] = hist.index
    hist['Type'].cat.rename_categories({'de Havilland Canada DHC-6 Twin Otter 300':'DHC-6'},inplace=True)
    graph = px.bar(data_frame=hist[:10][::-1],
                    y='Type',x='Count',
                    title=title,text='Count',
                    template='plotly_dark',
               )\
              .update_traces(marker_color='orange')\
              .update_traces(texttemplate='%{text:.2s}', textposition='outside')\
              .update_layout(barmode='group', yaxis_tickangle=-45)\
              .update_yaxes(title_text = "Types",title_standoff = 0,ticks = "outside", tickcolor='white', ticklen=10)\
              .update_xaxes(title_text = "Counts",range=[0,400])

    graph_area = dcc.Graph(id='accidents_type',figure=graph)
    return graph_area