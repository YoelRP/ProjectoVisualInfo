from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import pandas as pd


with urlopen(
    "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/geojson/Text3.json"
) as response:
    counties = json.load(response)



df = pd.read_csv(
    "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/fips.csv",
    dtype={"fips": str},
)

figMap = px.choropleth_mapbox(
    df,
    geojson=counties,
    locations="fips",
    color="2001",
    color_continuous_scale="Viridis",
    range_color=(0, 12),
    mapbox_style="carto-positron",
    zoom=4,
    center={"lat": 9.9281, "lon": -84.0907},
    opacity=0.5,
    labels={"unemp": "unemployment rate"},
)





figSquare = go.Figure(go.Scatter(x=[0,0,5,5,0], y=[0,5,5,0,0], fill="toself"))




# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App
df = px.data.gapminder()
print(df.head())



# Build the scatter plot
fig = px.scatter(data_frame=df, x="gdpPercap", y="lifeExp", size="pop",
                 color="continent", hover_name="country", log_x=True,
                 size_max=60, range_y=[30, 90], animation_frame='year')

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Life Expectancy vs. GDP", style={'textAlign': 'center'})
        ], width=12)
    ]),
   # dbc.Row([
        # dbc.Col([
        #     dcc.Graph(id='our-figMap', figure=figMap)
        # ], width=6),
        # dbc.Col([
        #     dcc.Graph(id='our-figMap', figure=figMap)
        # ], width=12)
   # ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='our-figMap', figure=figMap)
        ], width=6),
        dbc.Col([
            dcc.Graph(id='our-figSquare', figure=figSquare)
        ], width=6)
    ]),


    dbc.Row([
        dbc.Col([
            dcc.Graph(id='our-plot', figure=fig)
        ], width=12)
    ])
])


# callback is used to create app interactivity
#@callback()

# Run the App
if __name__ == '__main__':
    app.run_server()