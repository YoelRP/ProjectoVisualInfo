from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import pandas as pd
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





figSquare1 = square(5)
figSquare2 = square(2)
figSquare22 = square(2)
figSquare23 = square(2)
figSquare3 = square(3)
figSquare4 = square(1)
figSquare5 = square(6)
figSquare6 = square(4)

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App
df = px.data.gapminder()
#df = pd.read_csv("finalrecycling.csv")
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
        ])
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
        ]),
        dbc.Col([
            dbc.Row([
                html.H2("Natural  International Domestic   Cambio ", style={'textAlign': 'center'}),
                dbc.Col([
                    dcc.Graph(id='our-figSquare1', figure=figSquare1)
                ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare2', figure=figSquare2)
                    ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom',})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare22', figure=figSquare22)
                    ]),
                dbc.Col([
                    html.Div("=", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare23', figure=figSquare23)
                    ])
                
                ],className="g-0"),
            dbc.Row([
                 dbc.Col([
                    dcc.Graph(id='our-figSquare3', figure=figSquare3)
                ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare32', figure=figSquare4)
                    ]),
                dbc.Col([
                    html.Div("+", style={'vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare31', figure=figSquare22)
                    ]),
                dbc.Col([
                    html.Div("=", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare34', figure=figSquare23)
                    ])
                
                ],className="g-0"),
            dbc.Row([
                 html.Div("Comparacion", style={'textAlign': 'center'})
                ]),
            dbc.Row([
                 dbc.Col([
                    dcc.Graph(id='our-figSquare5', figure=figSquare5)
                ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare6', figure=figSquare6)
                    ]),
                 dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare41', figure=figSquare22)
                    ]),
                dbc.Col([
                    html.Div("=", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='our-figSquare42', figure=figSquare23)
                    ])
            ],className="g-0"
                    )
        ])
    ],className="g-0"),


    dbc.Row([
        dbc.Col([
            dcc.Graph(id='our-plot', figure=fig)
        ])
    ])
],
    style={"height": "200vh"},
    )


# callback is used to create app interactivity
#@callback()

# Run the App
if __name__ == '__main__':
    app.run_server()