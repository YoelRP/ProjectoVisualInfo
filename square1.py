import plotly.graph_objects as go



fig = go.Figure(go.Scatter(x=[3,3,5,5,3], y=[0.5,1.5,1.5,0.5,0.5], fill="toself"))
fig.show()