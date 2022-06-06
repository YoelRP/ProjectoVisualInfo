import plotly.express as px
df = px.data.medals_long()
df = pd.read_csv("./SCATERRPLOTV5.csv")
fig = px.scatter(df, y="nation", x="count", color="medal", symbol="medal")
fig.update_traces(marker_size=10)
fig.show()