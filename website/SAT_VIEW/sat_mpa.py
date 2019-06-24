import folium
import folium
import pandas as pd
import os
#
# states = os.path.join('india_state.json')
# state_data = pd.read_csv('rice_prod.csv')

m = folium.Map(location=[22.5937, 78.9629], zoom_start=5)

folium.TileLayer('MapQuestOpenAerial').add_to(m)




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


