import pandas as pd
import plotly.express as px

# # Load your own data into a DataFrame
# your_data = pd.read_csv('file.csv')
#
# # Create scatter map with custom center and zoom
# fig = px.scatter_mapbox(your_data, lat="Latitude", lon=" Longitude", size=" count",
#                         color=" count", hover_name=" count",
#                         mapbox_style="carto-positron", center={"lat": 25.4282896, "lon": 81.8838676}, zoom=9)
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# fig.show()

# --------------------------------------------
# ok

print('getting data..')
# df = px.data.carshare()
df = pd.read_csv('file.csv')
print(df.head(10))
print(df.tail(10))
fig = px.scatter_mapbox(df, lon=df[' Longitude'], lat=df['Latitude'], zoom = 10, color = df[' count'], size = df[' count'], width = 1200, height = 900, title='Crowd Density HeatMap')
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50, "l":0, "b":10})

fig.show()
print('plot complete.')


# -------------------------------------------