from dash import dcc
import plotly.express as px
import pandas as pd
def generate_fig(data,value,_type):
    px.set_mapbox_access_token('pk.eyJ1IjoiYW1yLWthc2VtLWI1NyIsImEiOiJja3VtZW52aHgwc2RmMnFtb2ljYm56aWFwIn0.PBQ3U_2nlEgoqtcnzIrMDw')

    agg_data = data.groupby(['lat','lon']).agg(count=('selected','count'),selected =('selected',pd.Series.mode),coordinates =('coordinates',pd.Series.mode))
    agg_data = agg_data.sort_values('selected',ascending=False) #to fix the selection color
    agg_data.selected.replace({True:'Selected',False:'Not_Selected'},inplace=True)   #to change the true to selected in map legend
    agg_data.reset_index(inplace=True)
    
    return px.scatter_mapbox(agg_data,  lat='lat',#agg_data.index.get_level_values(0),
                                        lon='lon',#agg_data.index.get_level_values(1),
                                        size='count',
                                        mapbox_style='carto-positron',
                                        size_max=15, zoom=1,
                                        color='selected',
                                        color_discrete_sequence=['orange','blue'], #to fix the selection colors 
                                        hover_name='coordinates', #to display the locations
                                        hover_data={'lat':False,'lon':False,'selected':False},
                                        template='plotly_dark',
                                        title='{} accidents around the world over {}'.format(_type,value),
                            ).update_layout( legend_title="",)
                             
def plot_graph(data):
    graph = generate_fig(data,2000,'All')
    graph_area = dcc.Graph(id='accidents_map',figure=graph)
    return graph_area