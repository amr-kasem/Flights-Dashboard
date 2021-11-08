from dash.dependencies import Input, Output
from ..graphs.accident_over_time import generate_fig as generate_hist
from ..graphs.accident_map import generate_fig as generate_map
import pandas as pd


def activate(app,data):
    @app.callback(
        [
            Output('accidents_map','figure'),
            Output('accidents_time','figure'),
            Output('year_number','children'),
            Output('year_name','children'),
            Output('country_number','children'),
            Output('country_name','children'),
        ],
        [
            Input('year_slider','value'),
            Input('ismil_dropdown','value'),
            Input('accidents_map',"selectedData"),
        ],
    )
    def _updateGraph(sliderValue,dropdownValue,selected_data):
        
        temp_data = data[data.year >= sliderValue[0]]
        temp_data = temp_data[data.year <= sliderValue[1]]
        temp_data.set_index(['lat','lon'],inplace=True)
        temp_data.loc[:,'selected'] = True
        if(dropdownValue == 'Military'):
            temp_data = temp_data[temp_data.isMil]
        elif(dropdownValue == 'Non-Militray'):
            temp_data = temp_data[temp_data.isMil != True]
        print(selected_data)
        if selected_data:
            index_points = [(x['lat'],x['lon']) for x in selected_data['points']]
            selected_data = False            
            if len(index_points) > 0 :
                temp_data.loc[:,'selected'] = False #.diffuse_color ='red'
                
                
                try:
                    temp_data.loc[index_points,'selected'] = True #.diffuse_color ='blue'
                    
                    
                except:
                    pass

        map_fig = generate_map(temp_data,sliderValue,dropdownValue)
        hist_fig = generate_hist(temp_data[temp_data.selected == True],sliderValue,dropdownValue)
        # return fig
        year_agg = temp_data[temp_data.selected == True].groupby('year').count()
        max_x_year = year_agg.Location.max()
        max_year = year_agg.Location.idxmax()
        country_agg = temp_data[temp_data.selected == True].groupby('coordinates').count()
        max_x_country = country_agg.Location.max()
        max_country = country_agg.Location.idxmax()
        return map_fig, hist_fig,max_x_year,max_year,max_x_country,max_country
