from dash import dcc
import plotly.express as px
def generate_fig(data,decade,_type):

    return px.histogram(
        data_frame=data,
        x='year',
        template='plotly_dark',
        title='{} accidents histogram over {} <br>in the selected region'.format(_type,decade)
        )\
        .update_traces(marker_color='white')
def plot_graph(data):
    graph = generate_fig(data,2000,'All')
    graph_area = dcc.Graph(id='accidents_time',figure=graph)
    return graph_area