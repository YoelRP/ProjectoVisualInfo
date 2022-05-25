from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)
app.layout = html.Div([
    html.H4('Live data control'),
    dcc.Graph(id="graph"),
    html.P("Change the position of the right-most data point:"),
    html.Button("Move Up", n_clicks=0, 
                id='btn-up'),
    html.Button("Move Down", n_clicks=0,
                id='btn-down'),
])

@app.callback(
    Output("graph", "figure"), 
    Input("btn-up", "n_clicks"),
    Input("btn-down", "n_clicks"))
def make_shape_taller(n_up, n_down):
    n = n_up-n_down
    fig = go.Figure(go.Scatter(
        x=[1, 0, 2, 1], y=[2, 0, n, 2], # replace with your own data source
        fill="toself"
    ))
    return fig


app.run_server(debug=True)