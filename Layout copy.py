from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import pandas as pd

from dash import html
from dash.dependencies import Input, Output
#mis dependecias 
from square1 import square 


#datos geograficos socioeconomicos de Costa Rica  de costa Rica
with urlopen(
    "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/geojson/Text3.json"
) as response:
    counties = json.load(response)


#abre los valores que salen del INEC
df = pd.read_csv(
    "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/fips.csv",
    dtype={"fips": str},
)
#crea la figura del mapa 
figMap = px.choropleth_mapbox(
    df,
    geojson=counties,
    locations="fips",
    color="2001",
    color_continuous_scale="Viridis",
    range_color=(0, 12),
    mapbox_style="carto-positron",
    zoom=6,
    center={"lat": 9.9281, "lon": -84.0907},
    opacity=0.5,
    labels={"unemp": "unemployment rate"},
)

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App
df = px.data.gapminder()
print(df.head())


app.layout = dbc.Container([
    dcc.Graph(id='our-figMap', figure=figMap)]
    

    )

@app.callback(
    [Input('our-figMap', 'clickData')])
def display_click_data(clickData):
    print("start")
    if clickData is None:
        return 'Click on any bubble'
    else:
        print (clickData)
        the_link=clickData['points'][0]['customdata']
        # if the_link is None:
        #     return 'No Website Available'
        # else:
        #     return html.A(the_link, href=the_link, target="_blank")
# callback is used to create app interactivity
#@callback()

# Run the App
if __name__ == '__main__':
    app.run_server()