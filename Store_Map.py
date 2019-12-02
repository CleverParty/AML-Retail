import plotly.graph_objects as go  # we use plotly to faciltitate the display of the warehouse locations on the map
import pandas as pd

df = pd.read_csv(r'C:\Users\Downloads\q3dbscan.csv') # Fill username

fig = go.Figure(data=go.Scattergeo(
        lon = -df['Long'],
        lat = df['Lat'],
        text = df['Store ID'],
        mode = 'markers',
        marker_color = 'black',
        ))

fig.update_layout(
        title = 'Store Locations',
        geo_scope='usa',
    )

fig.show()