from urllib.request import urlopen
import json

with urlopen(
    "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/geojson/Text3.json"
) as response:
    counties = json.load(response)

import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/fips.csv",
    dtype={"fips": str},
)

import plotly.express as px

fig = px.choropleth_mapbox(
    df,
    geojson=counties,
    locations="fips",
    color="2000",
    color_continuous_scale="Viridis",
    range_color=(0, 12),
    mapbox_style="carto-positron",
    zoom=8,
    center={"lat": 9.9281, "lon": -84.0907},
    opacity=0.5,
    labels={"unemp": "unemployment rate"},
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
