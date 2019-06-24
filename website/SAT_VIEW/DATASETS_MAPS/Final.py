import folium
import os
import pandas as pd

g_map= 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'
m = folium.Map(location=[22.5937, 78.9629], zoom_start=5,
               tiles=g_map,
               attr='Google Map'
               )

states = os.path.join('india_state.json')
state_data = pd.read_csv('rice_prod.csv')

folium.TileLayer('Mapbox Control Room').add_to(m)

folium.Choropleth(
    geo_data=states,
    name='Production',
    data=state_data,
    columns=['State', 'Avg_rice'],
    key_on='feature.properties.NAME_1',
    fill_color='YlGn',
    fill_opacity=0.4,
    line_opacity=0.9,
    legend_name='Production Rate (%)'
).add_to(m)

folium.LayerControl().add_to(m)

m.save('sat_view.html')

#http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}


# folium.Choropleth(
#     geo_data=states,
#     name='Production',
#     data=state_data,
#     columns=['State', 'Avg_rice'],
#     key_on='feature.properties.NAME_1',
#     fill_color='YlGn',
#     fill_opacity=0.7,
#     line_opacity=0.9,
#     legend_name='Production Rate (%)'
# ).add_to(m)


