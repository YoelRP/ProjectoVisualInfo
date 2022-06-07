from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import pandas as pd
from square1 import square 
from dash.dependencies import Input, Output, State




styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}







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
#df = px.data.gapminder()
df = pd.read_csv("D:\TEC\infoVis\Projecto\ProjectoVisualInfo\SCATERRPLOTV5.csv")
print(df)


# Build the scatter plot
fig = px.scatter(data_frame=df, x="Region", y="Cantidad_de_presonas", size="ABSCANT",
                 color="Tipo",
                 size_max=60, range_y=[-8850, 60940], animation_frame='Año')

app.layout =html.Div([
    dbc.Row([            html.H1("Life Expectancy vs. GDP", style={'textAlign': 'center'})
       
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='ID-figMap')
        ]),
        dcc.Store(id='CountClicks-value'),
        dbc.Col([
            dbc.Row([
                html.H2("Natural  International Domestic   Cambio ", style={'textAlign': 'center'}),
                dbc.Col([
                        html.Div([
                            html.Pre(id='click-data1',children =["text"]),
                        ]),
                ]),
                dcc.Store(id='Select1-value'),
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
                        html.Div([
                            html.Pre(id='click-data2',children =["text"]),
                        ]),
                ]),
                dcc.Store(id='Select2-value'),
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
                        html.Div([
                            html.Pre(id='click-data3',children =["Diferencia"]),
                        ]),
                ]),
                
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
            dcc.Graph(id='Bubbles', figure=fig)
        ]),
        dcc.Slider(
        df['Año'].min(),
        df['Año'].max(),
        step=None,
        id='AñoSlider',
        value=df['Año'].max(),
        marks={str(year): str(year) for year in df['Año'].unique()},

    )
    ])
],
    style={"height": "200vh"},
    )


# callback is used to create app interactivity
#@callback()
@app.callback(
    Output('click-data1', 'children'),
    Output('click-data2', 'children'),
    Output('CountClicks-value','data'),
    Output('Select1-value','data'),
    Output('Select2-value','data'),
    Input('ID-figMap', 'clickData'),
    State('AñoSlider', 'value'),
    State('CountClicks-value','data'),
    State('click-data1', 'children'),
    State('click-data2', 'children'),
    State('Select1-value','data'),
    State('Select2-value','data'),
    )
def update_text_squares(clickData,Año,data,old1,old2,old1Dic,oldDic2):
    
    if data is None:
        data = 0
    data = data+1
    if data%2 == 0 :
        value1 = clickData['points'][0]['location']+'\n'+'('+ str(Año) +')'
        value1Dic = {'Region':clickData['points'][0]['location'] , 'año':Año}
        value2Dic=oldDic2
        value2 = old2        
    if data%2 == 1 :
        value2 = clickData['points'][0]['location']+'\n'+'('+ str(Año) +')'
        value2Dic = {'Region':clickData['points'][0]['location'] , 'año':Año}
        value1Dic= old1Dic
        value1 = old1
    print (value1Dic)
    print (value2Dic)
    return value1,value2,data,value1Dic,value2Dic

@app.callback(
    Output('ID-figMap','figure'),
    Input('AñoSlider', 'value')
    )
def create_fig_map(año):
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
        color=str(año),
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=6,
        center={"lat": 9.9281, "lon": -84.0907},
        opacity=0.5,
        labels={"unemp": "unemployment rate"},
    )

# Run the App
if __name__ == '__main__':
    app.run_server()