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



df = pd.read_csv("D:\TEC\infoVis\Projecto\ProjectoVisualInfo\SCATERRPLOTV5.csv")

figSquare1 = square(19)
figSquare2 = square(20)
figSquare22 = square(17)
figSquare23 = square(19)
figSquare3 = square(13)
figSquare4 = square(1)
figSquare5 = square(6)
figSquare6 = square(4)

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App
#df = px.data.gapminder()

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
                    dcc.Graph(id='figSquareNatural1')
                ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquareInter1')
                    ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom',})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquareDomestic1')
                    ]),
                dbc.Col([
                    html.Div("=", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquareNetChange1')
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
                    dcc.Graph(id='figSquareNatural2')
                ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquareInter2')
                    ]),
                dbc.Col([
                    html.Div("+", style={'vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquareDomestic2')
                    ]),
                dbc.Col([
                    html.Div("=", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquareNetChange2')
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
                    dcc.Graph(id='figSquare5', figure=figSquare5)
                ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquare6', figure=figSquare6)
                    ]),
                dbc.Col([
                    html.Div("+", style={'textAlign': 'center','vertical-align':'text-bottom'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquare41', figure=figSquare22)
                    ]),
                dbc.Col([
                    html.Div("=", style={'textAlign': 'center'})
                    ]),
                dbc.Col([
                    dcc.Graph(id='figSquare42', figure=figSquare23)
                    ])
            ],className="g-0"
                    )
        ])
    ],className="g-0"),


    dbc.Row([
            dcc.Graph(id='Bubbles')
        ]),
    dbc.Row([
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
    if data%2 == 1 :
        print('************Primer click-**************')
        value1 = clickData['points'][0]['location']+'\n'+'('+ str(Año) +')'
        value1Dic = {'Region':clickData['points'][0]['location'] , 'Año':Año}
        value2Dic=oldDic2
        value2 = old2
    if data%2 == 0 :
        print('************Segundo click-**************')
        value2 = clickData['points'][0]['location']+'\n'+'('+ str(Año) +')'
        value2Dic = {'Region':clickData['points'][0]['location'] , 'Año':Año}
        value1Dic= old1Dic
        value1 = old1
    # print (value1Dic)
    # print (value2Dic)
    return value1,value2,data,value1Dic,value2Dic

@app.callback(
    Output('Bubbles','figure'),
    Input('AñoSlider', 'value')
    )
def create_fig_scatter(año):
    #df = pd.read_csv("D:\TEC\infoVis\Projecto\ProjectoVisualInfo\SCATERRPLOTV5.csv")
    global df
    # print(df)
    dfAño = df[df['Año'] == año]
    # print(dfAño)
    # Build the scatter plot
    fig_scatter= px.scatter(data_frame=dfAño, x="Region", y="Cantidad_de_presonas", size="ABSCANT",
                    color="Tipo",
                    size_max=60, range_y=[-8850, 60940])
    return fig_scatter






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
    dfMap = pd.read_csv(
        "https://raw.githubusercontent.com/YoelRP/ProjectoVisualInfo/main/fips.csv",
        dtype={"fips": str},
    )
    # print(df)
    #crea la figura del mapa 
    figMap = px.choropleth_mapbox(
        dfMap,
        geojson=counties,
        locations="fips",
        color=str(año),
        color_continuous_scale="Plotly3",
        range_color=(0, 70000),
        mapbox_style="carto-positron",
        zoom=6,
        center={"lat": 9.9281, "lon": -84.0907},
        opacity=0.7,
        labels={"unemp": "unemployment rate"},
    )
    return figMap


@app.callback(
    Output('figSquareNatural1','figure'),
    Output('figSquareInter1','figure'),
    Output('figSquareDomestic1','figure'),
    Output('figSquareNetChange1','figure'),
    Input('Select1-value','data')
    )
def create_fig_Squares(Select1):
    global df
    
    print(Select1)
    
    print("Año seleccionado")
    print(Select1['Año'])
    dfAño = df[df['Año'] == Select1['Año']]
    dfAñoReguion = dfAño[dfAño['Region'] == Select1['Region']]
    dfAñoReguionMig = dfAñoReguion[dfAñoReguion['Tipo'] == 'Migracioninterna']
    print(dfAñoReguionMig)
    migrates= dfAñoReguionMig['Cantidad_de_presonas'].values[0]
    dfAñoReguionInt = dfAñoReguion[dfAñoReguion['Tipo'] == 'International']
    print(dfAñoReguionInt)
    extrangeros= dfAñoReguionInt['Cantidad_de_presonas'].values[0]
    dfAñoReguionNat = dfAñoReguion[dfAñoReguion['Tipo'] == 'Natural']
    print(dfAñoReguionNat)
    crecimiento_natural = dfAñoReguionNat['Cantidad_de_presonas'].values[0]
    dfAñoReguionNetC = dfAñoReguion[dfAñoReguion['Tipo'] == 'NetChange']
    print(dfAñoReguionNetC)
    cambioGeneral= dfAñoReguionNetC['Cantidad_de_presonas'].values[0]
    migratesNorm = migrates*20/61000
    extrangerosNorm = extrangeros*20/61000
    crecimiento_naturalNorm = crecimiento_natural*20/61000
    cambioGeneralNorm = cambioGeneral*20/61000
    figMigrates= square(migratesNorm)
    figExtrangeros= square(extrangerosNorm)
    figCrecimientoNormal = square(crecimiento_naturalNorm)
    figCambioGeneral=square(cambioGeneralNorm)
    return figCrecimientoNormal,figExtrangeros,figMigrates,figCambioGeneral

@app.callback(
    Output('figSquareNatural2','figure'),
    Output('figSquareInter2','figure'),
    Output('figSquareDomestic2','figure'),
    Output('figSquareNetChange2','figure'),
    Input('Select2-value','data')
    )
def create_fig_Squares(Select2):
    global df
    print(Select2)
    print(Select2['Año'])
    dfAño = df[df['Año'] == Select2['Año']]
    dfAñoReguion = dfAño[dfAño['Region'] == Select2['Region']]
    dfAñoReguionMig = dfAñoReguion[dfAñoReguion['Tipo'] == 'Migracioninterna']
    migrates= dfAñoReguionMig['Cantidad_de_presonas'].values[0]
    dfAñoReguionInt = dfAñoReguion[dfAñoReguion['Tipo'] == 'International']
    extrangeros= dfAñoReguionInt['Cantidad_de_presonas'].values[0]
    dfAñoReguionNat = dfAñoReguion[dfAñoReguion['Tipo'] == 'Natural']
    crecimiento_natural = dfAñoReguionNat['Cantidad_de_presonas'].values[0]
    dfAñoReguionNetC = dfAñoReguion[dfAñoReguion['Tipo'] == 'NetChange']
    cambioGeneral= dfAñoReguionNetC['Cantidad_de_presonas'].values[0]
    migratesNorm = migrates*20/61000
    extrangerosNorm = extrangeros*20/61000
    crecimiento_naturalNorm = crecimiento_natural*20/61000
    cambioGeneralNorm = cambioGeneral*20/61000
    figMigrates= square(migratesNorm)
    figExtrangeros= square(extrangerosNorm)
    figCrecimientoNormal = square(crecimiento_naturalNorm)
    figCambioGeneral=square(cambioGeneralNorm)
    return figCrecimientoNormal,figExtrangeros,figMigrates,figCambioGeneral

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)