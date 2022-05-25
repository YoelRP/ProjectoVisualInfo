import plotly.graph_objects as go



fig = go.Figure(go.Scatter(x=[0,0,5,5,0], y=[0,5,5,0,0], fill="toself"))
fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False),
              showlegend=False,
              plot_bgcolor = '#FFFFFF'
              )
fig.update_xaxes(visible=False)
fig.update_yaxes(visible=False)
fig.show()
