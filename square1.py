import plotly.graph_objects as go


def square(side):
    fig = go.Figure(go.Scatter())
    fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=-side/2, y0=-side/2,
    x1=side/2, y1=side/2,
    line=dict(
        color="RoyalBlue",
        width=3,
    ),
    fillcolor="LightSkyBlue",
)
    fig.update_layout(
                showlegend=False,
                plot_bgcolor = '#FFFFFF',
                width=150,
                height=150,
                yaxis=dict(range=[-10, 10]),
                xaxis=dict(range=[-10, 10]),
                margin=dict(l=0, r=0, t=0, b=10),
                
                
                )
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    
    return fig
